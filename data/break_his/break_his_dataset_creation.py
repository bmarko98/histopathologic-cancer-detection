import os
import shutil
import logging
import tarfile
from utils.misc import move_to_directory


logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

benign = ['adenosis', 'fibroadenoma', 'phyllodes_tumor', 'tubular_adenoma']
malignant = ['ductal_carcinoma', 'lobular_carcinoma', 'mucinous_carcinoma', 'papillary_carcinoma']


def extract_and_create(archived_dataset, dir):
    _logger.info("Extracting images and creating directory structure...")
    tar = tarfile.open(archived_dataset)
    tar.extractall()
    tar.close()

    os.remove(archived_dataset)
    os.mkdir(os.path.join(dir, 'break_his_train'))
    os.mkdir(os.path.join(dir, 'break_his_validation'))
    os.mkdir(os.path.join(dir, 'break_his_test'))

    for dataset_dir in ['break_his_train', 'break_his_validation', 'break_his_test']:
        for cancer_type in [benign, malignant]:
            for cancer_subtype in cancer_type:
                os.mkdir(os.path.join(dir, dataset_dir, cancer_subtype))


def move_to_train(cancer_type, cancer_subtypes, dir):
    _logger.info("Moving {} images to train directory...".format(cancer_type))
    for cancer_subtype in cancer_subtypes:
        subdirectories = []
        if cancer_type == 'benign':
            benign_dir = os.path.join(dir, 'BreaKHis_v1/histology_slides/breast/benign/SOB', cancer_subtype)
            subdirectories = [f.path for f in os.scandir(benign_dir) if f.is_dir()]
        else:
            malignant_dir = os.path.join(dir, 'BreaKHis_v1/histology_slides/breast/malignant/SOB', cancer_subtype)
            subdirectories = [f.path for f in os.scandir(malignant_dir) if f.is_dir()]
        for subdirectory in subdirectories:
            source_directory = os.path.join(subdirectory, '100X')
            destination_directory = os.path.join(dir, 'break_his_train', cancer_subtype)
            images = os.listdir(source_directory)
            for image in images:
                shutil.move(os.path.join(source_directory, image), destination_directory)


def main(archived_dataset, dir):
    try:
        extract_and_create(archived_dataset, dir)

        move_to_train('benign', benign, dir)
        move_to_train('malignant', malignant, dir)

        shutil.rmtree(os.path.join(dir, 'BreaKHis_v1'))

        for cancer_subtype in [*benign, *malignant]:
            cancer_subtype_train_dir = os.path.join(dir, 'break_his_train', cancer_subtype)
            total = len([name for name in os.listdir(cancer_subtype_train_dir)])
            number_to_move = int(total*0.15)
            move_to_directory(dir, cancer_subtype_train_dir, 'break_his_validation', cancer_subtype, total, number_to_move)
            move_to_directory(dir, cancer_subtype_train_dir, 'break_his_test', cancer_subtype, total-number_to_move,
                              number_to_move)
    except Exception as e:
        _logger.error('Exception caught in main: {}'.format(e), exc_info=True)
        return 1
    return 0
