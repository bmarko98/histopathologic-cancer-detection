import os
import zipfile
import shutil
import random
import pandas as pd

'''
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
'''

tissue_types = ['non_tumor_tissue', 'tumor_tissue']

total = len([name for name in os.listdir(os.getcwd() + '/' + 'train')])
number_to_move = int(total*0.15)
train_labels = pd.read_csv('train_labels.csv')

#label = int(train_labels.loc[train_labels['id'] == 'a81f84895ddcd522302ddf34be02eb1b3e5af1cb']['label'])
#print(label)

def move_to_directory(directory, number_to_move):
    
