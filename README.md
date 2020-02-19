# Histopathologic Cancer Detection

Tensorflow and Keras implementation of Deep Convolutional Neural Networks for classification of histopathologic slides of tissue in order to determine whether the patient has metastatic cancer or not.

## Prerequisites (Dependencies)

 - TensorFlow
 - keras
 - NumPy
 - pandas
 - matplotlib
 - Pillow
 - Sacred
 - HDF5
 - tqdm

## Datasets

### 1. Breast Cancer Histopathological Dataset (BreakHis) using 100X magnifying factor

BreakHis is composed of 9,109 microscopic images of breast tumor tissue collected from 82 patients using different magnifying factors (40X, 100X, 200X, and 400X). It contains 2,480 benign and 5,429 malignant samples (700X460 pixels, 3-channel RGB, 8-bit depth in each channel, PNG format).
Dataset is divided into two main groups: benign tumors (adenosis, fibroadenoma, tubular adenoma and phyllodes tumor) and malignant tumors (mucinous carcinoma, ductal carcinoma, papillary carcinoma and lobular carcinoma). Histologically benign is a term referring to a lesion that does not match any criteria of malignancy – e.g., marked cellular atypia, mitosis, disruption of basement membranes, metastasize, etc. Normally, benign tumors are relatively “innocents”, presents slow growing and remains localized. Malignant tumor is a synonym for cancer: lesion can invade and destroy adjacent structures (locally invasive) and spread to distant sites (metastasize) to cause death.

First, download the dataset:
 - [Download BreakHis](https://www.kaggle.com/ambarish/breakhis)
Next, in order to get necessary directory structure, move *BreaKHis_v1.tar.gz* into data/break_his directory and run:
'''
$ python3 break_his_dataset_creation.py
'''

### 2. PatchCamelyon Dataset (PCam)

PCam is composed of 327.680 color images (96x96 pixels) extracted from histopathologic scans of lymph node sections. Each image is annoted with a binary label indicating presence of metastatic tissue, where a positive label indicates that the center 32x32px region of a patch contains at least one pixel of tumor tissue.

First, download the dataset:
 - [Download PCam](https://www.kaggle.com/c/histopathologic-cancer-detection/data)
 Next, in order to get necessary directory structure, move *histopathologic-cancer-detection.zip* into data/pcam directory and run:
     $ python3 pcam_dataset_creation.py

### 3. NCT-CRC-HE-100K Dataset

NCT-CRC-HE-100K Dataset is composed of 100,000 non-overlapping image patches (224x224 pixels) from hematoxylin & eosin (H&E) stained histological images of human colorectal cancer and normal tissue.
Tissue classes are: adipose, background, debris, lymphocytes, mucus, smooth muscle, normal colon mucosa, cancer-associated stroma, colorectal adenocarcinoma epithelium.

First, download the dataset:
 - [Download NCT-CRC-HE-100K](https://zenodo.org/record/1214456#.Xk2d2-l7nqo)
 Next, in order to get necessary directory structure, move *NCT-CRC-HE-100K.zip* into data/nct_crc_he_100k directory and run:
     $ python3 nct_crc_he_100k_dataset_creation.py

## Author

Marko Bauer / [@bmarko98](https://github.com/bmarko98)
