import os
import pytest
import random
from PIL import Image
from utils.misc import load_image
import utils.save_model as save_model
import models.cnn_simple as cnn_simple
import models.vgg19_simple as vgg19_simple
import utils.predict_image as predict_image
import utils.dataset_overview as dataset_overview
import utils.visualize_filters as visualize_filters
from data.break_his.break_his_dataset_creation import benign, malignant
from data.nct_crc_he_100k.nct_crc_he_100k_dataset_creation import tissue_types
import utils.visualize_intermediate_activations_and_heatmaps as visualize_intermediate_activations_and_heatmaps


datasets = ['break_his', 'nct_crc_he_100k']

data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')


def test_dataset_numbers(tmpdir):
    txt_file_path = os.path.join(tmpdir, 'tmp_dataset_numbers.txt')

    for dataset in datasets:
        train_dir = os.path.join(data_dir, dataset, dataset + '_train')
        categories = [f.name for f in os.scandir(train_dir) if f.is_dir()]
        assert dataset_overview.dataset_numbers(dataset, categories, data_dir, txt_file_path) == 0


@pytest.mark.xfail
def test_sample_images(tmpdir):
    for dataset in datasets:
        train_dir = os.path.join(data_dir, dataset, dataset + '_train')
        categories = [f.name for f in os.scandir(train_dir) if f.is_dir()]
        image_path = [im.path for im in os.scandir(os.path.join(train_dir, categories[0])) if im.is_file()][0]
        image = Image.open(image_path)
        save_path = os.path.join(tmpdir, 'sample_images.jpg')
        number_of_images = 10
        assert dataset_overview.sample_images(data_dir, dataset, categories, number_of_images, image.size[0], image.size[1],
                                              save_path=save_path) == 0


def get_random_image(dataset):
    dataset_dir = os.path.join(data_dir, dataset, dataset + '_train')
    categories = [f.name for f in os.scandir(dataset_dir) if f.is_dir()]
    random_category = random.sample(range(0, len(categories) - 1), 1)
    random_images = os.listdir(os.path.join(dataset_dir, categories[random_category[0]]))
    random_image = random.sample(range(0, len(random_images) - 1), 1)

    return os.path.join(dataset_dir, categories[random_category[0]], random_images[random_image[0]])


def test_predict_image(tmpdir):
    for dataset in datasets:
        random_image_path = get_random_image(dataset)
        for dataset in datasets:
            model, image, image_class, plot_path, layers = predict_image.predict_image(random_image_path,
                                                                                       dataset,
                                                                                       temporary_plots_dir=tmpdir)
            assert model is not None
            assert image is not None
            assert image_class in [*benign, *malignant, *tissue_types]
            assert os.path.exists(plot_path)
            assert layers


@pytest.mark.slow
def test_save_model(monkeypatch, tmpdir):

    def dummy_save_model(*args, **kwargs):
        pass

    monkeypatch.setattr(cnn_simple, 'save_model', dummy_save_model, raising=True)
    cnn_simple_network = cnn_simple.CNNSimple(epochs=1, dataset_count=(70010, 14995, 14995))

    assert save_model.save_model(cnn_simple_network, save_dir=os.path.join(tmpdir, 'cnn_simple')) == 0

    monkeypatch.setattr(vgg19_simple, 'save_model', dummy_save_model, raising=True)
    vgg19_simple_network = vgg19_simple.VGG19Simple(epochs=1, dataset_count=(1463, 309, 309))

    assert save_model.save_model(vgg19_simple_network, save_dir=os.path.join(tmpdir, 'vgg19_simple')) == 0


def test_visualize_filters(tmpdir):
    for dataset in datasets:
        model = predict_image.load_keras_model(dataset)
        assert visualize_filters.create_layer_patterns(model, 'block1_conv1', 5, 150, 5, tmpdir) == 0


def test_visualize_intermediate_activations(tmpdir):
    for dataset in datasets:
        dummy_image = load_image(get_random_image(dataset), image_size=(150, 150, 3))
        model = predict_image.load_keras_model(dataset)

        path = visualize_intermediate_activations_and_heatmaps.visualize_intermediate_activations(dummy_image,
                                                                                                  model,
                                                                                                  'block1_conv1',
                                                                                                  5,
                                                                                                  tmpdir) == 0
        assert os.path.exists(path)

        path_2 = visualize_intermediate_activations_and_heatmaps.visualize_intermediate_activations(dummy_image,
                                                                                                    model,
                                                                                                    'block1_conv1',
                                                                                                    None,
                                                                                                    tmpdir) == 0
        assert os.path.exists(path_2)


def test_visualize_heatmaps(tmpdir):
    for dataset in datasets:
        dummy_image_path = get_random_image(dataset)
        dummy_image = load_image(dummy_image_path, image_size=(150, 150, 3))
        model = predict_image.load_keras_model(dataset)
        assert visualize_intermediate_activations_and_heatmaps.visualize_heatmaps(dummy_image_path,
                                                                                  dummy_image,
                                                                                  model,
                                                                                  tmpdir) == 0
