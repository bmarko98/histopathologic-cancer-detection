import os
import numpy as np
import sys
import logging

from base_cnn import BaseCNN
from keras.layers import Flatten, Dropout, Dense
from keras.models import Sequential
from keras.applications import VGG19
from keras.optimizers import SGD, RMSprop, Adam
from keras.preprocessing.image import ImageDataGenerator

sys.path.insert(1, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'utils'))
from save_model import save_model

# disable tensorflow logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)


class VGG19Simple(BaseCNN):

    def __init__(self,
                 network_name = 'vgg19_simple',
                 dataset_name = None,
                 dataset_count = None,
                 image_size = None,
                 data_augmentation = False,
                 batch_size = 32,
                 classes = None,
                 weights = 'imagenet',
                 include_top = False,
                 loss = 'categorical_crossentropy',
                 learning_rate = 1e-4,
                 optimizer = 'rmsprop',
                 metrics = ['acc'],
                 epochs = 100,
                 skip_filters = True,
                 fine_tune = False,
                 first_trainable_block = 5,
                 fine_tune_learning_rate = 1e-5):

        '''
        Arguments:
            network_name: string, name of the network, default: vgg19_simple
            dataset_name: string, name of the dataset, default: None
            dateset_count: (int, int, int), number of images in train, validation, test set, default: None
            image_size: (int, int), size of the input images, default: None
            data_augmentation: bool, whether to use data augmentation, default: False
            batch_size: int, batch size during network training, default: 32
            classes: int, number of classes in dataset, default: None
            weights: 'imagenet' (pre-training on ImageNet) or path to weights file to be loaded, defualt: 'imagenet'
            include_top: bool, whether to include the 3 fully-connected layers at the top of the network, default: False
            loss: string, loss function used as feedback signal for learning the weighs, default: 'categorical_crossentropy'
            learning_rate: float, optimizer learning rate (magnitude of the move), default: 1e-4
            optimizer: optimizer for model training (variant of SGD), options: rmsprop, adam, sgd, default: rmsprop
            metrics: list of strings, metrics to monitor during model training, default: ['acc']
            epochs: int, number of epochs to train
            skip_filters: bool, whether to skip creation of filter patterns for separate conv layers, default: True
            fine_tune: bool, whether to fine tune the model, default: False
            first_trainable_block: 1-5, first block to set to trainable if fine tuning, default: 5
            fine_tune_learning_rate: float, optimizer learning rate if fine tuning, default: 1e-5
        '''

        super().__init__(network_name,
                         dataset_name,
                         dataset_count,
                         image_size,
                         data_augmentation,
                         batch_size,
                         classes,
                         loss,
                         learning_rate,
                         optimizer,
                         metrics,
                         epochs)

        _logger.info('VGG19Simple...')

        self.data_generators()

        self.weights = weights
        self.include_top = include_top
        self.build()

        self.compile(self.learning_rate)
        self.train()
        self.predict()
        save_model(self, skip_filters)

        self.fine_tune = fine_tune
        if self.fine_tune is True:
            if first_trainable_block >= 1 and first_trainable_block <= 5:
                self.first_trainable_block = first_trainable_block
            else:
                self.first_trainable_block = 5
            self.fine_tune_learning_rate = fine_tune_learning_rate
        else:
            self.first_trainable_block = None
            self.fine_tune_learning_rate = None

        if self.fine_tune is True:
            self.fine_tune_model()
            self.compile(self.fine_tune_learning_rate)
            self.train()
            self.predict()
            save_model(self, skip_filters)


    def data_generators(self):
        _logger.info('Setting data generators...')
        train_datagen = ImageDataGenerator(rescale=1./255,
                                           rotation_range=60,
                                           width_shift_range=0.2,
                                           height_shift_range=0.2,
                                           shear_range=0.2,
                                           zoom_range=0.2,
                                           fill_mode='nearest',
                                           horizontal_flip=True,
                                           vertical_flip=True)
        super().data_generators(train_datagen)


    def build(self):
        _logger.info('Building the model...')
        input_shape = list(self.image_size)
        input_shape.insert(2, 3)
        input_shape = tuple(input_shape)
        self.convolutional_base = VGG19(weights=self.weights,
                                        include_top=self.include_top,
                                        input_shape=input_shape)
        for layer in self.convolutional_base.layers:
            layer.trainable = False

        model = Sequential(name='sequential')
        model.add(self.convolutional_base)

        if self.include_top is False:
            model.add(Flatten(name = 'flatten'))
            model.add(Dense(512, activation = 'relu', name = 'dense_1'))
            model.add(Dropout(0.5, name = 'dropout_1'))
            model.add(Dense(1024, activation = 'relu', name = 'dense_2'))
            model.add(Dropout(0.5, name = 'dropout_2'))
            model.add(Dense(8, activation = 'softmax', name = 'predictions'))

        self.model = model


    def fine_tune_model(self):
        _logger.info('Fine tuning...')
        for layer in self.convolutional_base.layers:
            if layer.name[0:5] == 'block':
                if int(layer.name[5]) < self.first_trainable_block:
                    layer.trainable = False
                else:
                    layer.trainable = True
            elif layer.name[0:5] == 'input':
                layer.trainable = False
            else:
                layer.trainable = True


def main():
    _logger.info('Creating VGG19Simple object...')

    model2 = VGG19Simple(network_name = 'VGG19Test',
                         dataset_name = 'break_his',
                         dataset_count = (1463, 309, 309),
                         image_size = (150, 150),
                         data_augmentation = True,
                         batch_size = 32,
                         classes = 8,
                         weights = 'imagenet',
                         include_top = False,
                         loss = 'categorical_crossentropy',
                         learning_rate = 1e-3,
                         optimizer = 'rmsprop',
                         metrics = ['acc'],
                         epochs = 1,
                         skip_filters = True,
                         fine_tune = True,
                         first_trainable_block = 5,
                         fine_tune_learning_rate = 5e-4)


if __name__ == '__main__':
    _logger.info('Started the program...')
    main()
