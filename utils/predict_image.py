import os
import numpy as np
import logging
import matplotlib.pyplot as plt
from keras.models import load_model
from keras.preprocessing import image
from utils.visualize_intermediate_activations_and_heatmaps import visualize_intermediate_activations, visualize_heatmaps


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
    index = np.arange(len(classes))
    plt.bar(classes, class_probabilities)
    plt.xticks(index, classes, fontsize=12, rotation=45)
    class_probabilities_plot_path = os.path.join(dir, 'class_probabilities.png')
    plt.savefig(fname=class_probabilities_plot_path)
    plt.cla()
    plt.clf()
    plt.close('all')
    return class_probabilities_plot_path


def predict_image_class(image_URL, dataset, model, dir):
    _logger.info('Predicting image class...')

    img = image.load_img(image_URL, target_size=datasets[dataset]['image_size'])
    np_img = image.img_to_array(img)
    np_img = np.expand_dims(np_img, axis=0)
    np_img /= 255.
    class_probabilities = model.predict(np_img)
    classes = datasets[dataset]['categories']
    classes.sort()
    plot_path = plot_class_probabilities(classes, class_probabilities[0], dir)

    return np_img, datasets[dataset]['categories'][class_probabilities[0].argmax(axis=-1)], plot_path


def load_keras_model(dataset, model_path):
    _logger.info('Loading Keras model...')
    if model_path is None:
        assert(dataset in datasets)
        model_paths_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'experiments', dataset + '_models')
        model_paths = [f.path for f in os.scandir(model_paths_dir) if f.is_dir()]
        assert(len(model_paths) > 0)
        model_name = model_paths[0].split('/')[-1].split('_')[0]
        model = load_model(os.path.join(model_paths[0], model_name + '.h5'))
    else:
        model = load_model(model_path)

    return model


def predict_image(image_URL, dataset, model_path=None, transfer_learning=False):
    temporary_plots_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'gui', 'temporary_plots')
    if not os.path.exists(temporary_plots_dir):
        os.mkdir(temporary_plots_dir)
    model = load_keras_model(dataset, model_path)
    image, image_class, plot_path = predict_image_class(image_URL, dataset, model, temporary_plots_dir)
    layers = visualize_intermediate_activations(image, model, transfer_learning, temporary_plots_dir)
    visualize_heatmaps(image_URL, image, model, transfer_learning, temporary_plots_dir)
    return image_class, plot_path, layers


'''
def main():
    image_URL = "/home/lenovo/Desktop/test.png"
    model_path = "/home/lenovo/Documents/bachelors_thesis/histopathologic-cancer-detection/experiments/break_his_models/" + \
                 "VGG19Test_03-03-2020_09:38:50/VGG19Test.h5"
    model_path_2 = "/home/lenovo/Documents/bachelors_thesis/histopathologic-cancer-detection/experiments/" + \
                   "nct_crc_he_100k_models/CNNSimpleTest_12-03-2020_15:49:03/CNNSimpleTest.h5"
    predict_image(image_URL, 'nct_crc_he_100k', model_path_2, False)
    predict_image(image_URL, 'break_his', model_path, True)

if __name__ == '__main__':
    main()
'''
