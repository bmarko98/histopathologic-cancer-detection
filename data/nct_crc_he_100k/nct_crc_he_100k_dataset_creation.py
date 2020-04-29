import os
import zipfile
import shutil
import logging
from utils.misc import move_to_directory


logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

tissue_types = ['adipose', 'background', 'debris', 'lymphocytes', 'mucus', 'smooth_muscle', 'normal_colon_mucosa',
                'cancer_associated_stroma', 'colorectal_adenocarcinoma_epithelium']

tissue_types_dict = {'adipose': 'ADI', 'background': 'BACK', 'debris': 'DEB', 'lymphocytes': 'LYM', 'mucus': 'MUC',
                     'smooth_muscle': 'MUS', 'normal_colon_mucosa': 'NORM', 'cancer_associated_stroma': 'STR',
                     'colorectal_adenocarcinoma_epithelium': 'TUM'}


def extract_and_create(archived_dataset, dir):
    _logger.info("Extracting images and creating directory structure...")
    with zipfile.ZipFile(archived_dataset, 'r') as zip_ref:
        zip_ref.extractall(dir)

    os.remove(archived_dataset)

    os.mkdir(os.path.join(dir, 'nct_crc_he_100k_train'))
    os.mkdir(os.path.join(dir, 'nct_crc_he_100k_validation'))
    os.mkdir(os.path.join(dir, 'nct_crc_he_100k_test'))

    for dataset_dir in ['nct_crc_he_100k_train', 'nct_crc_he_100k_validation', 'nct_crc_he_100k_test']:
        for tissue_type in tissue_types:
            os.mkdir(os.path.join(dir, dataset_dir, tissue_type))


def move_to_train(dir):
    _logger.info("Moving images to train directory...")
    for tissue_type in tissue_types:
        source_dir = os.path.join(dir, 'NCT-CRC-HE-100K', tissue_types_dict[tissue_type])
        destination_dir = os.path.join(dir, 'nct_crc_he_100k_train', tissue_type)
        if os.path.isdir(source_dir):
            images = os.listdir(source_dir)
            for image in images:
                shutil.move(os.path.join(source_dir, image), destination_dir)


def main(archived_dataset, dir):
    try:
        extract_and_create(archived_dataset, dir)
        move_to_train(dir)

        shutil.rmtree(dir + '/NCT-CRC-HE-100K')

        for tissue_type in tissue_types:
            cancer_type_train_dir = os.path.join(dir, 'nct_crc_he_100k_train', tissue_type)
            total = len([name for name in os.listdir(cancer_type_train_dir)])
            number_to_move = int(total*0.15)
            move_to_directory(dir, cancer_type_train_dir, 'nct_crc_he_100k_validation', tissue_type, total, number_to_move)
            move_to_directory(dir, cancer_type_train_dir, 'nct_crc_he_100k_test', tissue_type, total-number_to_move,
                              number_to_move)
    except Exception as e:
        _logger.error('Exception caught in main: {}'.format(e), exc_info=True)
        return 1
    return 0
