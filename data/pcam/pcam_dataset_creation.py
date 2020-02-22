import os
import zipfile
import shutil
import random
import pandas as pd


with zipfile.ZipFile('histopathologic-cancer-detection.zip', 'r') as zip_ref:
    zip_ref.extractall(os.getcwd())

os.remove('histopathologic-cancer-detection.zip')
os.remove('sample_submission.csv')
shutil.rmtree('test')

os.mkdir('pcam_train')
os.mkdir('pcam_validation')
os.mkdir('pcam_test')

tissue_types = ['non_tumor_tissue', 'tumor_tissue']

for directory in ['pcam_train', 'pcam_validation', 'pcam_test']:
    for tissue_type in tissue_types:
            os.mkdir(directory + '/' + tissue_type)

train_labels = pd.read_csv('train_labels.csv')

#move data to train directory (moves ~220000 images, takes ~45min)
for image in os.listdir(os.getcwd() + '/train'):
    label = int(train_labels.loc[train_labels['id'] == image[0:-4]]['label'])
    shutil.move(os.getcwd() + '/train/' + image, os.getcwd() + '/pcam_train/' + tissue_types[label])

os.remove('train_labels.csv')
shutil.rmtree('train')

#move data to validation and test directory
def move_to_directory(directory, tissue_type, total, number_to_move):
    files = [ f.path for f in os.scandir(os.getcwd() + '/pcam_train/' + tissue_type)]
    random_list = random.sample(range(0, total-1), number_to_move)
    files_to_move = []
    for random_number in random_list:
        files_to_move.append(files[random_number])
    for file_path in files_to_move:
        shutil.move(file_path, os.getcwd() + directory + tissue_type)

for tissue_type in tissue_types:
    total = len([name for name in os.listdir(os.getcwd() + '/pcam_train/' + tissue_type)])
    number_to_move = int(total*0.15)
    move_to_directory('/pcam_validation/', tissue_type, total, number_to_move)
    move_to_directory('/pcam_test/', tissue_type, total-number_to_move, number_to_move)
