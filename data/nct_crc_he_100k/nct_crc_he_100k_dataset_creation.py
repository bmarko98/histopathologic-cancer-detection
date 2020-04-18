import os
import zipfile
import shutil
import random
import logging


logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

current_dir = os.path.dirname(os.path.abspath(__file__))

tissue_types = ['adipose', 'background', 'debris', 'lymphocytes', 'mucus', 'smooth_muscle', 'normal_colon_mucosa',
                'cancer_associated_stroma', 'colorectal_adenocarcinoma_epithelium']

tissue_types_dict = {'adipose': 'ADI', 'background': 'BACK', 'debris': 'DEB', 'lymphocytes': 'LYM', 'mucus': 'MUC',
                     'smooth_muscle': 'MUS', 'normal_colon_mucosa': 'NORM', 'cancer_associated_stroma': 'STR',
                     'colorectal_adenocarcinoma_epithelium': 'TUM'}


def extract_and_create(archived_dataset):
    with zipfile.ZipFile(archived_dataset, 'r') as zip_ref:
        zip_ref.extractall(current_dir)

    os.remove(archived_dataset)

    os.mkdir('nct_crc_he_100k_train')
    os.mkdir('nct_crc_he_100k_validation')
    os.mkdir('nct_crc_he_100k_test')

    for directory in ['nct_crc_he_100k_train', 'nct_crc_he_100k_validation', 'nct_crc_he_100k_test']:
        for tissue_type in tissue_types:
            os.mkdir(directory + '/' + tissue_type)



def move_to_train():
    for tissue_type in tissue_types:
        source_directory = current_dir + '/NCT-CRC-HE-100K/' + tissue_types_dict[tissue_type] + '/'
        destination_directory = current_dir + '/nct_crc_he_100k_train/' + tissue_type
        if os.path.isdir(source_directory):
            images = os.listdir(source_directory)
            for image in images:
                shutil.move(source_directory + image, destination_directory)


def move_to_directory(directory, tissue_type, total, number_to_move):
    files = [f.path for f in os.scandir(current_dir + '/nct_crc_he_100k_train/' + tissue_type)]
    random_list = random.sample(range(0, total-1), number_to_move)
    files_to_move = []
    for random_number in random_list:
        files_to_move.append(files[random_number])
    for file_path in files_to_move:
        shutil.move(file_path, current_dir + directory + tissue_type)


def main(archived_dataset):
    try:
        extract_and_create(archived_dataset)
        move_to_train()

        shutil.rmtree(current_dir + '/NCT-CRC-HE-100K')

        for tissue_type in tissue_types:
            total = len([name for name in os.listdir(current_dir + '/nct_crc_he_100k_train/' + tissue_type)])
            number_to_move = int(total*0.15)
            move_to_directory('/nct_crc_he_100k_validation/', tissue_type, total, number_to_move)
            move_to_directory('/nct_crc_he_100k_test/', tissue_type, total-number_to_move, number_to_move)
    except Exception as e:
        _logger.error('Exception caught in main: {}'.format(e), exc_info=True)
        return 1
    return 0


if __name__=='__main__':
    archived_dataset = 'NCT-CRC-HE-100K.zip'
    exit(main(archived_dataset))
