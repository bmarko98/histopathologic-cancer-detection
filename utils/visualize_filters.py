import os
import math
import logging
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from keras import backend as K


logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)


def deprocess_image(x):
    x -= x.mean()
    x /= (x.std() + 1e-5)
    x *= 0.1
    x += 0.5
    x = np.clip(x, 0, 1)
    x *= 255
    x = np.clip(x, 0, 255).astype('uint8')
    return x


def create_pattern(model, layer_name, filter_index, size=300, save=False):
    _logger.info('Creating filter patterns for ' + str(layer_name) + ', filter number ' + str(filter_index))
    layer_output = model.get_layer(layer_name).output
    if layer_output.shape[-1] < filter_index:
        return ''
    loss = K.mean(layer_output[:, :, :, filter_index])
    grads = K.gradients(loss, model.inputs[-1])[0]
    grads /= (K.sqrt(K.mean(K.square(grads))) + 1e-5)
    iterate = K.function([model.inputs[-1]], [loss, grads])
    input_img_data = np.random.random((1, size, size, 3)) * 20 + 128
    rate = 1
    steps = 40
    for i in range(steps):
        loss_value, grads_value = iterate([input_img_data])
        input_img_data += grads_value * rate
    img = input_img_data[0]
    if save:
        filter_plot_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'gui', 'temporary_plots',
                                        'filters', layer_name + '_filter_' + str(filter_index) + '.png')
        matplotlib.image.imsave(filter_plot_path, deprocess_image(img))
        return filter_plot_path
    else:
        return deprocess_image(img)


def create_layer_patterns(model, layer_name, N, size, margin, directory):
    results = np.zeros((N * size + (N-1) * margin, N * size + (N-1) * margin, 3))
    for i in range(N):
        for j in range(N):
            filter_img = create_pattern(model, layer_name, j + (i*N), size)
            horizontal_start = i * size + i * margin
            horizontal_end = horizontal_start + size
            vertical_start = j * size + j * margin
            vertical_end = vertical_start + size
            results[horizontal_start: horizontal_end, vertical_start: vertical_end, :] = filter_img
    figsize = (20, 20)
    plt.figure(figsize=figsize)
    plt.title('Filter patterns for ' + str(layer_name))
    plt.imshow((results).astype(np.uint8))
    plt.axis('off')
    image_name = layer_name + '_filter_patterns.png'
    image_path = os.path.join(directory, image_name)
    plt.savefig(fname=image_path, bbox_inches='tight')

    return 0


def visualize_filters(model, directory):
    _logger.info('Creating model patterns...')
    image_size = 150
    margin_size = 5

    for layer in model.layers:
        if layer.name.find('conv') >= 0:
            create_layer_patterns(model=model,
                                  layer_name=layer.name,
                                  N=int(math.sqrt(32*2**(int(layer.name[5])-1))),
                                  size=image_size,
                                  margin=margin_size,
                                  directory=directory)

    return 0
