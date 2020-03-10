import os
import numpy as np
import logging
import matplotlib.pyplot as plt
from PIL import Image
from skimage import transform
from keras.models import load_model
from visualize_intermediate_activations_and_heatmaps import visualize_intermediate_activations, visualize_heatmaps


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

datasets = {'break_his': {'categories': ['mucinous_carcinoma', 'adenosis', 'ductal_carcinoma', 'fibroadenoma',
                                         'tubular_adenoma', 'phyllodes_tumor', 'papillary_carcinoma', 'lobular_carcinoma'],
                          'image_size': (150, 150, 3)},
            'nct_crc_he_100k': {'categories': ['cancer_associated_stroma', 'adipose', 'debris', 'mucus', 'background', 'smooth_muscle',
                                              'lymphocytes', 'colorectal_adenocarcinoma_epithelium', 'normal_colon_mucosa'],
                               'image_size': (150, 150, 3)},
            'pcam': {'categories': ['non_tumor_tissue', 'tumor_tissue'],
                     'image_size': (150, 150, 3)}}


def plot_class_probabilities(classes, class_probabilities):
    _logger.info('Plotting bar of classes and class probabilities...')
    index = np.arange(len(classes))
    plt.bar(classes, class_probabilities)
    plt.xticks(index, classes, fontsize=10, rotation=30)
    class_probabilities_plot_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'gui', 'temporary_plots', 'tmp.png')
    plt.savefig(fname = class_probabilities_plot_path)


def predict_image_class(image_URL, dataset, model):
    _logger.info('Predicting image class...')
    image = Image.open(image_URL)
    np_image = np.array(image).astype('float32')/255
    np_image = transform.resize(np_image, datasets[dataset]['image_size'])
    np_image = np.expand_dims(np_image, axis=0)
    class_probabilities = model.predict(np_image)
    classes = datasets[dataset]['categories']
    classes.sort()
    plot_class_probabilities(classes, class_probabilities[0])

    return datasets[dataset]['categories'][class_probabilities[0].argmax(axis=-1)]


def load_keras_model(dataset, model_path):
    _logger.info('Loading Keras model...')
    if model_path is None:
        assert(dataset in datasets)
        model_paths_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'experiments', dataset + '_models')
        model_paths = [ f.path for f in os.scandir(model_paths_dir) if f.is_dir() ]
        assert(len(model_paths) > 0)
        model_name = model_paths[0].split('/')[-1].split('_')[0]
        model = load_model(os.path.join(model_paths[0], model_name + '.h5'))
    else:
        model = load_model(model_path)

    return model


def predict_image(image_URL, dataset, model_path = None):
    model = load_keras_model(dataset, model_path)
    image_class = predict_image_class(image_URL, dataset, model)
    visualize_intermediate_activations()
    visualize_heatmaps()


def main():
    image_URL = "/home/lenovo/Desktop/test.png"
    dataset = "break_his"
    predict_image(image_URL, dataset)


if __name__ == "__main__":
    main()
