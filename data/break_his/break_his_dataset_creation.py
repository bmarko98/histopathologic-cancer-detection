import os
import tarfile
import shutil
import random


tar = tarfile.open('BreaKHis_v1.tar.gz')
tar.extractall()
tar.close()

os.remove('BreaKHis_v1.tar.gz')
os.mkdir('break_his_train')
os.mkdir('break_his_validation')
os.mkdir('break_his_test')

benign = ['adenosis', 'fibroadenoma', 'phyllodes_tumor', 'tubular_adenoma']
malignant = ['ductal_carcinoma', 'lobular_carcinoma', 'mucinous_carcinoma', 'papillary_carcinoma']

# create subdirectories for each cancer subtype
for directory in ['break_his_train', 'break_his_validation', 'break_his_test']:
    for cancer_type in [benign, malignant]:
        for cancer_subtype in cancer_type:
            os.mkdir(directory + '/' + cancer_subtype)

# move data to train directory
def move_to_train(cancer_type, cancer_subtypes):
    for cancer_subtype in cancer_subtypes:
        if cancer_type == 'benign':
            subdirectories = [ f.path for f in os.scandir(os.getcwd() + '/BreaKHis_v1/histology_slides/breast/benign/SOB/' + cancer_subtype) if f.is_dir() ]
        else:
            subdirectories = [ f.path for f in os.scandir(os.getcwd() + '/BreaKHis_v1/histology_slides/breast/malignant/SOB/' + cancer_subtype) if f.is_dir() ]
        for subdirectory in subdirectories:
            source_directory = subdirectory + '/100X/'
            destination_directory = os.getcwd() + '/break_his_train/' + cancer_subtype
            images = os.listdir(source_directory)
            for image in images:
                shutil.move(source_directory + image, destination_directory)

move_to_train('benign', benign)
move_to_train('malignant', malignant)

shutil.rmtree(os.getcwd() + '/BreaKHis_v1')

# move data to validation and test directories
def move_to_directory(directory, cancer_subtype, total, number_to_move):
    files = [ f.path for f in os.scandir(os.getcwd() + '/break_his_train/' + cancer_subtype)]
    random_list = random.sample(range(0, total-1), number_to_move)
    files_to_move = []
    for random_number in random_list:
        files_to_move.append(files[random_number])
    for file_path in files_to_move:
        shutil.move(file_path, os.getcwd() + directory + cancer_subtype)

for cancer_subtype in [*benign, *malignant]:
    total = len([name for name in os.listdir(os.getcwd() + '/break_his_train/' + cancer_subtype)])
    number_to_move = int(total*0.15)
    move_to_directory('/break_his_validation/', cancer_subtype, total, number_to_move)
    move_to_directory('/break_his_test/', cancer_subtype, total-number_to_move, number_to_move)
