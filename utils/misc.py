import os
import random
import shutil
import logging
import numpy as np
from keras.preprocessing import image


logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)


def file_get_contents(filename):
    with open(filename) as f:
        s = f.read()
    return s


def move_to_directory(dir, source_dir, destination_dir, cancer_subtype, total, number_to_move):
    _logger.info("Moving {t} images from {s} directory to {d} directory...".format(t=cancer_subtype,
                                                                                   s=source_dir,
                                                                                   d=destination_dir))
    files = [f.path for f in os.scandir(source_dir)]
    random_list = random.sample(range(0, total-1), number_to_move)
    files_to_move = []
    for random_number in random_list:
        files_to_move.append(files[random_number])
    for file_path in files_to_move:
        shutil.move(file_path, dir + destination_dir + cancer_subtype)


def load_image(image_path, image_size=None):
    img = image.load_img(image_path, target_size=image_size)
    np_img = image.img_to_array(img)
    np_img = np.expand_dims(np_img, axis=0)
    np_img /= 255.
    return np_img
