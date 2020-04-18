import os
import tarfile
import shutil
import random
import logging


logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

benign = ['adenosis', 'fibroadenoma', 'phyllodes_tumor', 'tubular_adenoma']
malignant = ['ductal_carcinoma', 'lobular_carcinoma', 'mucinous_carcinoma', 'papillary_carcinoma']


def extract_and_create(archived_dataset, current_dir):
    tar = tarfile.open(archived_dataset)
    tar.extractall()
    tar.close()

    os.remove(archived_dataset)
    os.mkdir(os.path.join(current_dir, 'break_his_train'))
    os.mkdir(os.path.join(current_dir, 'break_his_validation'))
    os.mkdir(os.path.join(current_dir, 'break_his_test'))

    for directory in ['break_his_train', 'break_his_validation', 'break_his_test']:
        for cancer_type in [benign, malignant]:
            for cancer_subtype in cancer_type:
                os.mkdir(os.path.join(current_dir, directory + '/' + cancer_subtype))


def move_to_train(cancer_type, cancer_subtypes, current_dir):
    for cancer_subtype in cancer_subtypes:
        subdirectories = []
        if cancer_type == 'benign':
            if os.path.isdir(current_dir + '/BreaKHis_v1/histology_slides/breast/benign/SOB/' + cancer_subtype):
                subdirectories = [f.path for f in os.scandir(current_dir + '/BreaKHis_v1/histology_slides/breast/benign/SOB/' +
                                  cancer_subtype) if f.is_dir()]
        else:
            if os.path.isdir(current_dir + '/BreaKHis_v1/histology_slides/breast/malignant/SOB/' + cancer_subtype):
                subdirectories = [f.path for f in os.scandir(current_dir + '/BreaKHis_v1/histology_slides/breast/malignant/SOB/' +
                                  cancer_subtype) if f.is_dir()]
        for subdirectory in subdirectories:
            source_directory = subdirectory + '/100X/'
            destination_directory = current_dir + '/break_his_train/' + cancer_subtype
            images = os.listdir(source_directory)
            for image in images:
                shutil.move(source_directory + image, destination_directory)


def move_to_directory(directory, cancer_subtype, total, number_to_move, current_dir):
    files = [f.path for f in os.scandir(current_dir + '/break_his_train/' + cancer_subtype)]
    random_list = random.sample(range(0, total-1), number_to_move)
    files_to_move = []
    for random_number in random_list:
        files_to_move.append(files[random_number])
    for file_path in files_to_move:
        shutil.move(file_path, current_dir + directory + cancer_subtype)


def main(archived_dataset, current_dir):
    try:
        extract_and_create(archived_dataset, current_dir)

        move_to_train('benign', benign, current_dir)
        move_to_train('malignant', malignant, current_dir)

        if os.path.isdir(current_dir + '/BreaKHis_v1'):
            shutil.rmtree(current_dir + '/BreaKHis_v1')

        for cancer_subtype in [*benign, *malignant]:
            if os.path.isdir(current_dir + '/break_his_train/' + cancer_subtype):
                total = len([name for name in os.listdir(current_dir + '/break_his_train/' + cancer_subtype)])
                number_to_move = int(total*0.15)
                move_to_directory('/break_his_validation/', cancer_subtype, total, number_to_move, current_dir)
                move_to_directory('/break_his_test/', cancer_subtype, total-number_to_move, number_to_move, current_dir)
    except Exception as e:
        _logger.error('Exception caught in main: {}'.format(e), exc_info=True)
        return 1
    return 0
