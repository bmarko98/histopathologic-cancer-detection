import os
import numpy as np
import sys
import logging

from base_cnn import BaseCNN
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dropout, Dense
from keras.models import Sequential
from keras.optimizers import SGD, RMSprop, Adam
from keras.preprocessing.image import ImageDataGenerator

sys.path.insert(1, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'utils'))
from save_model import save_model

# disable tensorflow logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)


class CNNSimple(BaseCNN):

    def __init__(self,
                 network_name = 'cnn_simple',
                 dataset_name = None,
                 dataset_count = None,
                 image_size = None,
                 data_augmentation = False,
                 batch_size = 32,
                 classes = None,
                 loss = 'categorical_crossentropy',
                 learning_rate = 1e-4,
                 optimizer = 'rmsprop',
                 metrics = ['acc'],
                 epochs = 100):

        '''
        Arguments:
            network_name: string, name of the network, default: cnn_simple
            dataset_name: string, name of the dataset, default: None
            dateset_count: (int, int, int), number of images in train, validation, test set, default: None
            image_size: (int, int), size of the input images, default: None
            data_augmentation: bool, whether to use data augmentation, default: False
            batch_size: int, batch size during network training, default: 32
            classes: int, number of classes in dataset, default: None
            loss: string, loss function used as feedback signal for learning the weighs, default: 'categorical_crossentropy'
            learning_rate: float, optimizer learning rate (magnitude of the move), default: 1e-4
            optimizer: optimizer for model training (variant of SGD), options: rmsprop, adam, sgd, default: rmsprop
            metrics: list of strings, metrics to monitor during model training, default: ['acc']
            epochs: int, number of epochs to train
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

        _logger.info('CNNSimple...')

        self.data_generators()
        self.build()
        self.compile(self.learning_rate)
        self.train()
        self.predict()
        save_model(self, skip_filters=True)


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

        model = Sequential()
        # block1
        model.add(Conv2D(32, (3, 3), activation='relu', input_shape=input_shape, name='block1_conv1'))
        model.add(Conv2D(32, (3, 3), activation='relu', name='block1_conv2'))
        model.add(MaxPooling2D((2, 2), name='block1_pool'))
        # block2
        model.add(Conv2D(64, (3, 3), activation='relu', name='block2_conv1'))
        model.add(Conv2D(64, (3, 3), activation='relu', name='block2_conv2'))
        model.add(MaxPooling2D((2, 2), name='block2_pool'))
        # block3
        model.add(Conv2D(128, (3, 3), activation='relu', name='block3_conv1'))
        model.add(Conv2D(128, (3, 3), activation='relu', name='block3_conv2'))
        model.add(Conv2D(128, (3, 3), activation='relu', name='block3_conv3'))
        model.add(MaxPooling2D((2, 2), name='block3_pool'))
        # block4
        model.add(Conv2D(256, (3, 3), activation='relu', name='block4_conv1'))
        model.add(Conv2D(256, (3, 3), activation='relu', name='block4_conv2'))
        model.add(Conv2D(256, (3, 3), activation='relu', name='block4_conv3'))
        model.add(MaxPooling2D((2, 2), name='block4_pool'))
        # flatten
        model.add(Flatten())
        # fully connected layers
        model.add(Dense(512, activation='relu', name='dense1'))
        model.add(Dropout(0.5, name='dropout1'))
        model.add(Dense(1024, activation = 'relu', name='dense2'))
        model.add(Dropout(0.5, name='dropout2'))
        model.add(Dense(9, activation='softmax', name='prediction'))
        model.summary()
        self.model = model


def main():
    _logger.info('Creating CNNSimple object...')

    model = CNNSimple(network_name = 'CNNSimpleTest',
                      dataset_name = 'nct_crc_he_100k',
                      dataset_count = (70010, 14995, 14995),
                      image_size = (150, 150),
                      data_augmentation = True,
                      batch_size = 32,
                      classes = 9,
                      loss = 'categorical_crossentropy',
                      learning_rate = 1e-4,
                      optimizer = 'rmsprop',
                      metrics = ['acc'],
                      epochs = 1)


if __name__ == '__main__':
    _logger.info('Started the program...')
    main()
