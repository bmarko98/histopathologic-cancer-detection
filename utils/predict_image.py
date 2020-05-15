import os
import logging
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from utils.misc import load_image
from keras.models import load_model
from utils.visualize_intermediate_activations_and_heatmaps import visualize_heatmaps


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

datasets = {'break_his': {'categories': ['mucinous_carcinoma', 'adenosis', 'ductal_carcinoma', 'fibroadenoma',
                                         'tubular_adenoma', 'phyllodes_tumor', 'papillary_carcinoma', 'lobular_carcinoma'],
                          'image_size': (150, 150, 3)},
            'nct_crc_he_100k': {'categories': ['cancer_associated_stroma', 'adipose', 'debris', 'mucus', 'background',
                                'smooth_muscle', 'lymphocytes', 'colorectal_adenocarcinoma_epithelium', 'normal_colon_mucosa'],
                                'image_size': (150, 150, 3)}}


def plot_class_probabilities(classes, class_probabilities, dir):
    _logger.info('Plotting bar of classes and class probabilities...')
    sns.set_style('darkgrid')
    transformed_classes = []
    for subclass in classes:
        transformed_classes.append(subclass.replace('_', ' ').title())
    index = np.arange(len(classes))
    plt.gcf().subplots_adjust(bottom=0.47 if len(classes) == 9 else 0.3)
    plt.bar(classes, class_probabilities)
    plt.xticks(index, transformed_classes, fontsize=12, rotation=45, ha='right')
    class_probabilities_plot_path = os.path.join(dir, 'class_probabilities.png')
    plt.savefig(fname=class_probabilities_plot_path)
    plt.cla()
    plt.clf()
    plt.close('all')

    return class_probabilities_plot_path


def predict_image_class(image_path, dataset, model, dir):
    _logger.info('Predicting image class...')

    np_img = load_image(image_path, datasets[dataset]['image_size'])
    class_probabilities = model.predict(np_img)
    classes = datasets[dataset]['categories']
    classes.sort()
    plot_path = plot_class_probabilities(classes, class_probabilities[0], dir)

    return np_img, datasets[dataset]['categories'][class_probabilities[0].argmax(axis=-1)], plot_path


def get_model_path(dataset):
    assert(dataset in datasets)
    model_paths_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'experiments', dataset + '_models')
    model_paths = [f.path for f in os.scandir(model_paths_dir) if f.is_dir()]
    assert(len(model_paths) > 0)
    model_name = model_paths[0].split('/')[-1].split('_')[0]

    return os.path.join(model_paths[0], model_name + '.h5')


def load_keras_model(dataset, model_path=None):
    _logger.info('Loading Keras model...')

    if model_path is None:
        model_path = get_model_path(dataset)
    model = load_model(model_path)

    return model


def predict_image(image_path, dataset, model_path=None, temporary_plots_dir=None):
    if temporary_plots_dir is None:
        temporary_plots_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'gui', 'temporary_plots')
    if not os.path.exists(temporary_plots_dir):
        os.mkdir(temporary_plots_dir)
    filters_dir = os.path.join(temporary_plots_dir, 'filters')
    if not os.path.exists(filters_dir):
        os.mkdir(filters_dir)
    model = load_keras_model(dataset, model_path)
    layers = []
    for layer in model.layers:
        layers.append(layer.name)
    image, image_class, plot_path = predict_image_class(image_path, dataset, model, temporary_plots_dir)
    visualize_heatmaps(image_path, image, model, temporary_plots_dir)

    return model, image, image_class, plot_path, layers
