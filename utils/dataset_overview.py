import os
import random
import logging
import numpy as np
import seaborn as sns
from PIL import Image
import matplotlib.pyplot as plt


logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)


def get_image_paths(data_dir, dataset, category, number_of_images):
    category_path = os.path.join(data_dir, dataset, dataset + '_train', category)
    all_image_paths = [im.path for im in os.scandir(category_path) if im.is_file()]
    random_image_numbers = random.sample(range(0, len(all_image_paths) - 1), number_of_images)
    image_paths = []
    for random_image_number in random_image_numbers:
        image_paths.append(all_image_paths[random_image_number])

    return image_paths


def sample_images(data_dir, dataset, categories, number_of_images, image_width, image_height, margin=0, save_path=None):
    results = np.zeros((len(categories) * image_height + len(categories) * margin, number_of_images * image_width, 3))
    for i in range(len(categories)):
        image_paths = get_image_paths(data_dir, dataset, categories[i], number_of_images)
        for j in range(number_of_images):
            img = Image.open(image_paths[j])
            img.resize(size=(image_width, image_height), resample=Image.NEAREST)
            img = np.asarray(img)
            horizontal_start = i * image_height + i * margin
            horizontal_end = horizontal_start + image_height
            vertical_start = j * image_width
            vertical_end = vertical_start + image_width
            results[horizontal_start: horizontal_end, vertical_start: vertical_end, :] = img
    sns.set_style('darkgrid')
    plt.figure(figsize=(20, 20))
    plt.imshow((results).astype(np.uint8))
    plt.axis('off')
    image_name = dataset + '_sample_images.jpg'
    image_path = os.path.join(data_dir, dataset, image_name)
    save_path = image_path if save_path is None else save_path
    plt.savefig(fname=save_path, bbox_inches='tight', pad_inches=0)

    return 0


def category_numbers(dataset, categories, dir):
    category_dictionary = {}
    total = 0
    categories.sort()
    for category in categories:
        category_path = os.path.join(dir, category)
        number_of_images_in_directory = len([im.path for im in os.scandir(category_path) if im.is_file()])
        category_dictionary[category] = number_of_images_in_directory
        total += number_of_images_in_directory
    return category_dictionary, total


def write_dataset_numbers(txt_file, total, dictionary):
    txt_file.write('Total number of images: ' + str(total) + '\n')
    txt_file.write('Number of images per class: \n')
    for category, number in dictionary.items():
        txt_file.write('\t' + category.replace('_', ' ').title() + ': ' + str(number) + '\n')
    txt_file.write('\n')


def dataset_numbers(dataset, categories, data_dir, txt_file_path):
    _logger.info(dataset + ' dataset numbers...')
    dataset_dict = {'break_his': 'BreakHis', 'nct_crc_he_100k': 'NCT-CRC-HE-100K'}
    train_dictionary, train_total = category_numbers(dataset,
                                                     categories,
                                                     os.path.join(data_dir, dataset, dataset + '_train'))
    validation_test_dictionary, validation_test_total = category_numbers(dataset,
                                                                         categories,
                                                                         os.path.join(data_dir, dataset,
                                                                                      dataset + '_validation'))

    total_dictionary = {}
    for category in categories:
        total_dictionary[category] = train_dictionary[category] + 2 * validation_test_dictionary[category]

    txt_file = open(txt_file_path, "w+")
    txt_file.write('\n')
    txt_file.write('Dataset: ' + dataset_dict[dataset] + '\n')
    txt_file.write('Categories: \n')
    for category in categories:
        txt_file.write('\t ' + category.replace('_', ' ').title() + '\n')
    txt_file.write('\n')
    write_dataset_numbers(txt_file, train_total + 2*validation_test_total, total_dictionary)
    txt_file.write('Training set: \n')
    write_dataset_numbers(txt_file, train_total, train_dictionary)
    txt_file.write('Validation and Test set (each): \n')
    write_dataset_numbers(txt_file, validation_test_total, validation_test_dictionary)
    txt_file.close()

    return 0


def main(data_dir, datasets, number_of_images=10, save_dir=None):
    save_dir = data_dir if save_dir is None else save_dir
    try:
        for dataset in datasets:
            _logger.info(dataset + ' dataset...')
            train_dir = os.path.join(data_dir, dataset, dataset + '_train')
            categories = [f.name for f in os.scandir(train_dir) if f.is_dir()]
            image_path = [im.path for im in os.scandir(os.path.join(train_dir, categories[0])) if im.is_file()][0]
            image = Image.open(image_path)
            txt_file_path = os.path.join(save_dir, dataset, dataset + '_dataset_overview.txt')
            dataset_numbers(dataset, categories, data_dir, txt_file_path)
            sample_images(data_dir, dataset, categories, number_of_images, image.size[0], image.size[1])
    except Exception as e:
        _logger.info('Exception caught in main: {}'.format(e), exc_info=True)
        return 1
    return 0
