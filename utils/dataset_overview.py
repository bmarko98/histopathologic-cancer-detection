import os
import random
import logging

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)


def get_image_paths(dataset, category, number_of_images, data_dir):
    category_path = os.path.join(data_dir, dataset, dataset + '_train', category)
    all_image_paths = [im.path for im in os.scandir(category_path) if im.is_file()]
    random_image_numbers = random.sample(range(0, len(all_image_paths) - 1), number_of_images)
    image_paths = []
    for random_image_number in random_image_numbers:
        image_paths.append(all_image_paths[random_image_number])

    return image_paths


def sample_images(dataset, categories, number_of_images, image_width, image_height, data_dir):
    margin = 7
    results = np.zeros((len(categories) * image_height + len(categories) * margin, number_of_images * image_width, 3))
    for i in range(len(categories)):
        image_paths = get_image_paths(dataset, categories[i], number_of_images, data_dir)
        for j in range(number_of_images):
            img = Image.open(image_paths[j])
            img = np.asarray(img)
            horizontal_start = i * image_height + i * margin
            horizontal_end = horizontal_start + image_height
            vertical_start = j * image_width
            vertical_end = vertical_start + image_width
            results[horizontal_start: horizontal_end, vertical_start: vertical_end, :] = img
    figsize = (20, 20)
    plt.figure(figsize=figsize)
    plt.imshow((results).astype(np.uint8))
    plt.axis('off')
    image_name = dataset + '_sample_images.jpg'
    image_path = os.path.join(data_dir, dataset, image_name)
    plt.savefig(fname=image_path, bbox_inches='tight', pad_inches=0)


def category_numbers(dataset, categories, dir):
    category_dictionary = {}
    total = 0
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
        txt_file.write('\t' + category + ': ' + str(number) + '\n')
    txt_file.write('\n')


def dataset_numbers(dataset, categories, data_dir):
    _logger.info(dataset + ' dataset numbers...')
    train_dictionary, train_total = category_numbers(dataset,
                                                     categories,
                                                     os.path.join(data_dir, dataset, dataset + '_train'))
    validation_dictionary, validation_total = category_numbers(dataset,
                                                               categories,
                                                               os.path.join(data_dir, dataset, dataset + '_validation'))
    test_dictionary, test_total = category_numbers(dataset,
                                                   categories,
                                                   os.path.join(data_dir, dataset, dataset + '_test'))

    total_dictionary = {}
    for category in categories:
        total_dictionary[category] = train_dictionary[category] + validation_dictionary[category] + test_dictionary[category]

    txt_file_path = os.path.join(data_dir, dataset, dataset + '_dataset_overview.txt')
    txt_file = open(txt_file_path, "w+")
    txt_file.write('\n')
    txt_file.write('Dataset: ' + dataset + '\n')
    txt_file.write('Categories: \n')
    for category in categories:
        txt_file.write('\t ' + category + '\n')
    txt_file.write('\n')
    write_dataset_numbers(txt_file, train_total + validation_total + test_total, total_dictionary)
    txt_file.write('Training set: \n')
    write_dataset_numbers(txt_file, train_total, train_dictionary)
    txt_file.write('Validation set: \n')
    write_dataset_numbers(txt_file, validation_total, validation_dictionary)
    txt_file.write('Test set: \n')
    write_dataset_numbers(txt_file, test_total, test_dictionary)
    txt_file.close()


def main():
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
    datasets = [f.name for f in os.scandir(data_dir) if f.is_dir()]
    for dataset in datasets:
        _logger.info(dataset + ' dataset...')
        train_dir = os.path.join(data_dir, dataset, dataset + '_train')
        categories = [f.name for f in os.scandir(train_dir) if f.is_dir()]
        number_of_images = 10
        image_path = [im.path for im in os.scandir(os.path.join(train_dir, categories[0])) if im.is_file()][0]
        image = Image.open(image_path)
        dataset_numbers(dataset, categories, data_dir)
        sample_images(dataset, categories, number_of_images, image.size[0], image.size[1], data_dir)


if __name__ == "__main__":
    main()
