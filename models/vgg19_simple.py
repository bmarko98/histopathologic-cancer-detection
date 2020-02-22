import os
from datetime import datetime

from keras.layers import Flatten, Dropout, Dense
from keras.models import Model
from keras.applications import VGG19
from keras.optimizers import RMSprop
from keras.preprocessing.image import ImageDataGenerator


class VGG19Simple():

    def __init__(self,
                 network_name = 'VGG19Simple',
                 dataset_name = None,
                 image_size = None,
                 data_augmentation = False,
                 batch_size = 32,
                 classes = None,
                 weights = 'imagenet',
                 include_top = False,
                 loss = 'categorical_crossentropy',
                 optimizer = RMSprop(1e-4),
                 metrics = ['acc'],
                 epochs = 100):

        '''
        Arguments:
            network_name: string, name of the network, default: 'VGG19Simple'
            dataset_name: string, name of the dataset, default: 'None'
            image_size: (int, int), size of the input images, default: None
            data_augmentation: bool, whether to use data augmentation, default: False
            batch_size: int, batch size during network training, default: 32
            classes: int, number of classes in dataset, default: None
            weights: 'imagenet' (pre-training on ImageNet) or path to weights file to be loaded, defualt: 'imagenet'
            include_top: bool, whether to include the 3 fully-connected layers at the top of the network, default: False

        '''

        self.network_name = network_name
        self.dataset_name = dataset_name

        if image_shape is None:
            try:
                dataset_path = os.path.join(os.path.abspath(__file__), '..', 'data', dataset_name)
                category_path = [ f.path for f in os.scandir(os.path.join(dataset_path, 'train')) if f.is_dir() ][0]
                image_path = [im.path for im in os.scandir(category_path) if im.is_file()][0]
                image = Image.open(image_path)
                self.image_size = image.size
            except Exception as e:
                print('Error caught in constructor: ', e)
        else:
            self.image_size = image_size

        self.data_augmentation = data_augmentation
        self.batch_size = batch_size
        if classes is None:
            try:
                dataset_path = os.path.join(os.path.abspath(__file__), '..', 'data', dataset_name)
                self.classes = len([ f.path for f in os.scandir(os.path.join(dataset_path, 'train')) if f.is_dir() ])
            except Exception as e:
                print('Error caught in constructor: ', e)
        self.data_generators()

        self.weights = weights
        self.include_top = include_top
        self.build()
        self.compile()


    def data_generators():
        if self.data_augmentation is True:
            train_datagen = ImageDataGenerator(rescale=1./255,
                                               rotation_range=45,
                                               width_shift_range=0.2,
                                               height_shift_range=0.2,
                                               shear_range=0.2,
                                               zoom_range=0.2,
                                               fill_mode='nearest',
                                               horizontal_flip=True)
        else:
            train_datagen = ImageDataGenerator(rescale=1./255)

        validation_test_datagen = ImageDataGenerator(rescale=1./255)

        self.train_generator = train_datagen.flow_from_directory(
                os.path.join(os.path.abspath(__file__), '..', 'data', self.dataset_name, 'train'),
                target_size = self.image_size,
                batch_size = self.batch_size,
                class_mode = 'categorical' if self.classes>1 else 'binary')

        self.validation_generator = validation_test_datagen.flow_from_directory(
                os.path.join(os.path.abspath(__file__), '..', 'data', self.dataset_name, 'validation'),
                target_size = self.image_size,
                batch_size = self.batch_size,
                class_mode = 'categorical' if self.classes>1 else 'binary')

        self.test_generator = validation_test_datagen.flow_from_directory(
                os.path.join(os.path.abspath(__file__), '..', 'data', self.dataset_name, 'test'),
                target_size = self.image_size,
                batch_size = self.batch_size,
                class_mode = 'categorical' if self.classes>1 else 'binary')


        def build():
            convolutional_base = VGG19(weights = self.weights,
                                       include_top = self.include_top,
                                       input_shape = (self.image_size, 3))

            if self.include is False:
                flatten = Flatten(name = 'flatten')(convolutional_base.outputs)
                dropout_1 = Dropout(0.5, name = 'dropout_1')(flatten)
                dense_1 = Dense(256, activation = 'relu', name = 'dense')(dropout_1)
                dropout_2 = Dropout(0.5, name = 'dropout_2')(dense_1)
                output = Dense(10, activation = 'softmax', name = 'predictions')(dropout_2)
                model = Model(inputs = convolutional_base.inputs, outputs = output)
                self.model = model
            else:
                self.model = convolutional_base


        def compile():
            convolutional_base = 5
