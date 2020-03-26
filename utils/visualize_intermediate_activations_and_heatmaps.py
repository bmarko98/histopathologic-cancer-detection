import os
import cv2
import logging
import numpy as np
import matplotlib.pyplot as plt
from keras import backend as K
from keras.models import Model


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)


def visualize_intermediate_activations(image, model, requested_layer_name, channel_number, dir):
    _logger.info("Visualizing intermediate activations...")
    activation_plots_dir = os.path.join(dir, 'layer_activations')
    if not os.path.exists(activation_plots_dir):
        os.mkdir(activation_plots_dir)

    n = 0
    for layer in model.layers:
        if layer.name[0:7] != 'flatten':
            n = n+1
        else:
            break

    layer_names = []
    layer_outputs = [layer.output for layer in model.layers[:(n-1)]]
    activation_model = Model(inputs=model.input, outputs=layer_outputs)
    for layer in model.layers[:(n-1)]:
        layer_names.append(layer.name)

    activations = activation_model.predict(image)

    if channel_number:
        for layer_name in layer_names:
            if layer_name == requested_layer_name:
                layer_number = layer_names.index(requested_layer_name)
                requested_layer_activations = activations[layer_number]
                if requested_layer_activations.shape[-1] >= channel_number:
                    plt.title(requested_layer_name + ' ' + str(channel_number))
                    plt.grid(False)
                    plt.axis('off')
                    plt.imshow(requested_layer_activations[0, :, :, channel_number], aspect='auto', cmap='viridis')
                    requested_layer_channel_path = os.path.join(activation_plots_dir, layer_name + '_' + str(channel_number) + '.png')
                    plt.savefig(fname=requested_layer_channel_path, bbox_inches='tight')
                    plt.close('all')
                    return requested_layer_channel_path
        return ''

    else:
        images_per_row = 16

        for layer_name, layer_activation in zip(layer_names, activations):
            if (layer_name == requested_layer_name):
                _logger.info("Visualizing activations for layer: " + layer_name)
                n_features = layer_activation.shape[-1]
                size = layer_activation.shape[1]
                n_cols = n_features // images_per_row
                display_grid = np.zeros((size * n_cols, images_per_row * size))
                for col in range(n_cols):
                    for row in range(images_per_row):
                        channel_image = layer_activation[0, :, :, col * images_per_row + row]
                        channel_image -= channel_image.mean()
                        channel_image /= channel_image.std() + 1e-5
                        channel_image *= 64
                        channel_image += 128
                        channel_image = np.clip(channel_image, 0, 255).astype('uint8')
                        display_grid[col * size: (col + 1) * size, row * size: (row + 1) * size] = channel_image

                scale = 1. / size
                plt.figure(figsize=(scale*display_grid.shape[1], scale*display_grid.shape[0]))
                plt.title(layer_name)
                plt.grid(False)
                plt.axis('off')
                plt.imshow(display_grid, aspect='auto', cmap='viridis')
                plot_path = os.path.join(activation_plots_dir, layer_name + '.png')
                plt.savefig(fname=plot_path, bbox_inches='tight')
                plt.close('all')
        return plot_path


def get_heatmap(image, model):
    _logger.info('Producing heatmap of class activation over input image...')
    class_probabilities = model.predict(image)
    class_output = model.output[:, np.argmax(class_probabilities[0])]

    for i, layer in enumerate(model.layers):
        if layer.name[0:7] == 'flatten':
            last_conv_layer_name = model.layers[i-2].name
    last_conv_layer = model.get_layer(last_conv_layer_name)

    grads = K.gradients(class_output, last_conv_layer.output)[0]
    pooled_grads = K.mean(grads, axis=(0, 1, 2))
    iterate = K.function([model.input], [pooled_grads, last_conv_layer.output[0]])
    pooled_grads_value, conv_layer_output_value = iterate([image])
    for i in range(256):
        conv_layer_output_value[:, :, i] *= pooled_grads_value[i]

    heatmap = np.mean(conv_layer_output_value, axis=-1)
    heatmap = np.maximum(heatmap, 0)
    heatmap /= np.max(heatmap)

    return heatmap


def visualize_heatmaps(image_URL, image, model, dir):
    heatmap = get_heatmap(image, model)
    img = cv2.imread(image_URL)
    heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[0]))
    heatmap = np.uint8(255 * heatmap)
    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    superimposed_img = heatmap * 0.4 + img
    heatmap_path = os.path.join(dir, 'heatmap.jpg')
    cv2.imwrite(heatmap_path, superimposed_img)
