# Histopathologic Cancer Detection using CNNs

Tensorflow & Keras implementation of Deep Convolutional Neural Networks for classification of histopathologic slides of tissue in order to determine whether the patient has metastatic cancer or not.

## Prerequisites (Dependencies)

 - h5py
 - Keras
 - matplotlib
 - numpy
 - pandas
 - Pillow
 - PyQt5
 - scikit-image
 - scikit-learn
 - seaborn
 - tensorflow

You can install dependencies by executing following command in terminal:
```
$ pip3 install -r requirements.txt
```

## Datasets

### 1. Breast Cancer Histopathological Dataset (BreakHis), using 100X magnifying factor

BreakHis is composed of 9,109 microscopic images of breast tumor tissue collected from 82 patients using different magnifying factors (40X, 100X, 200X, and 400X). It contains 2,480 benign and 5,429 malignant samples (700X460 pixels, 3-channel RGB, 8-bit depth in each channel, PNG format). Dataset is divided into two main groups: benign tumors (adenosis, fibroadenoma, tubular adenoma and phyllodes tumor) and malignant tumors (mucinous carcinoma, ductal carcinoma, papillary carcinoma and lobular carcinoma).

 - [Download BreakHis](https://www.kaggle.com/ambarish/breakhis)

### 2. PatchCamelyon Dataset (PCam)

PCam is composed of 327.680 color images (96x96 pixels) extracted from histopathologic scans of lymph node sections. Each image is annoted with a binary label indicating presence of metastatic tissue, where a positive label indicates that the center 32x32px region of a patch contains at least one pixel of tumor tissue.

 - [Download PCam](https://www.kaggle.com/c/histopathologic-cancer-detection/data)

### 3. NCT-CRC-HE-100K Dataset

NCT-CRC-HE-100K Dataset is composed of 100,000 non-overlapping image patches (224x224 pixels) from hematoxylin & eosin (H&E) stained histological images of human colorectal cancer and normal tissue. Tissue classes are: adipose, background, debris, lymphocytes, mucus, smooth muscle, normal colon mucosa, cancer-associated stroma, colorectal adenocarcinoma epithelium.

 - [Download NCT-CRC-HE-100K](https://zenodo.org/record/1214456#.Xk2d2-l7nqo)

### Copying images to Training, Validation and Test sets
 - In order to create training, validation and test sets, first:
   - move *BreaKHis_v1.tar.gz* into data/break_his directory
   - move *histopathologic-cancer-detection.zip*  into data/pcam directory
   - move *NCT-CRC-HE-100K.zip* into data/nct_crc_he_100k directory
 - Next, execute following commands:
```
$ python3 data/break_his/break_his_dataset_creation.py
$ python3 data/pcam/pcam_dataset_creation.py
$ python3 data/nct_crc_he_100k/nct_crc_he_100k_dataset_creation.py
```
 - In order to plot sample images and obtain basic dataset information, run following command:
 ```
$ python3 data/dataset_overview.py
 ```

## Models

### BaseCNN

BaseCNN is parent model of all subsequent models. It contains creation of data generators, as well as build, compile, train and predict methods, some of which are overridden in its children classes.

### 1. CNNSimple

CNNSimple is model trained on NCT_CRC_HE_100K dataset. It's architecture consists of 4 convolutional blocks (each of which contain several convolutional layers, followed by max pooling layer), and 3 fully-connected (dense) layers on top.
 - In order to train the model from scratch on NCT_CRC_HE_100K dataset, set up the parameters dictionary in and run following command:
 ```
$ python3 experiments/hyperparameter_tuning.py
 ```

### 2. VGG19Simple

VGG19Simple is model trained on BreakHis dataset. It's architecture consists of VGG19 network as convolutional base and 3 fully-connected (dense) layers on top. It uses transfer learning in order to overcome small size of the dataset.
- In order to train the model from scratch on BreakHis dataset, set up the parameters dictionary in and run following command:
```
$ python3 experiments/hyperparameter_tuning.py
```

## Graphical User Interface

GUI is implemented using PyQt5 library, and it consists of several window classes, all derived from Window class. In order to run the Application, run the following command:
```
$ python3 gui/main_window.py
```

## Author

Marko Bauer / [@bmarko98](https://github.com/bmarko98)
