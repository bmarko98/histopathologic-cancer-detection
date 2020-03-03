import os
import numpy as np
import sys
import logging

from keras.layers import Conv2D, MaxPooling2D, Flatten, Dropout, Dense
from keras.models import Sequential
from keras.optimizers import SGD, RMSprop, Adam
from keras.preprocessing.image import ImageDataGenerator

sys.path.insert(1, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'utils'))
from save_model import save_model


logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)


class BaseCNN():

    def __init__(self,
                 network_name = None,
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

        _logger.info('BaseCNN...')

        self.network_name = network_name
        self.dataset_name = dataset_name
        self.dataset_count = dataset_count

        if image_size is None:
            try:
                dataset_path = os.path.join(os.path.abspath(__file__), '..', 'data', dataset_name)
                category_path = [ f.path for f in os.scandir(os.path.join(dataset_path, 'train')) if f.is_dir() ][0]
                image_path = [im.path for im in os.scandir(category_path) if im.is_file()][0]
                image = Image.open(image_path)
                self.image_size = image.size
            except Exception as e:
                _logger.error('Error caught in constructor while getting image size: ', e)
        else:
            self.image_size = image_size

        self.data_augmentation = data_augmentation
        self.batch_size = batch_size
        if classes is None:
            try:
                dataset_path = os.path.join(os.path.abspath(__file__), '..', 'data', dataset_name)
                self.classes = len([ f.path for f in os.scandir(os.path.join(dataset_path, 'train')) if f.is_dir() ])
            except Exception as e:
                _logger.error('Error caught in constructor while getting number of classes: ', e)
        else:
            self.classes = classes

        self.loss = loss
        self.learning_rate = learning_rate
        self.optimizer = optimizer
        self.metrics = metrics

        self.epochs = epochs


    def data_generators(self, image_data_generator):
        _logger.info('Setting data generators...')
        if self.data_augmentation is True:
            train_datagen = image_data_generator
        else:
            train_datagen = ImageDataGenerator(rescale=1./255)

        validation_test_datagen = ImageDataGenerator(rescale=1./255)

        self.train_generator = train_datagen.flow_from_directory(
                os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', self.dataset_name, self.dataset_name + '_train'),
                target_size = self.image_size,
                batch_size = self.batch_size,
                class_mode = 'categorical')

        self.validation_generator = validation_test_datagen.flow_from_directory(
                os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', self.dataset_name, self.dataset_name + '_validation'),
                target_size = self.image_size,
                batch_size = self.batch_size,
                class_mode = 'categorical')

        self.test_generator = validation_test_datagen.flow_from_directory(
                os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', self.dataset_name, self.dataset_name + '_test'),
                target_size = self.image_size,
                batch_size = self.batch_size,
                class_mode = 'categorical')


    def build(self):
        pass

    def compile(self, learning_rate):
        _logger.info('Compiling the model...')
        optimizer_dict = {'sgd': SGD(learning_rate=learning_rate),
                          'rmsprop': RMSprop(learning_rate = learning_rate),
                          'adam': Adam(learning_rate = learning_rate)}
        self.model.compile(loss = self.loss,
                           optimizer = optimizer_dict[self.optimizer],
                           metrics = self.metrics)


    def train(self):
        _logger.info('Training the model...')
        self.history = self.model.fit_generator(self.train_generator,
                                                steps_per_epoch = int(self.dataset_count[0]/self.batch_size) if self.dataset_count is not None else 100,
                                                epochs = self.epochs,
                                                validation_data = self.validation_generator,
                                                validation_steps = int(self.dataset_count[1]/self.batch_size) if self.dataset_count is not None else 20)


    def predict(self):
        _logger.info('Predicting test dataset classes...')
        predictions = self.model.predict_generator(self.test_generator)
        predictions = np.argmax(predictions, axis=1)
        self.predictions = predictions