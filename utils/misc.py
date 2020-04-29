import os
import random
import shutil
import logging


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
