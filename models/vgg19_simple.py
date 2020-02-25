import os
import numpy as np
import sys
import logging

from keras.layers import Flatten, Dropout, Dense
from keras.models import Model
from keras.applications import VGG19
from keras.optimizers import SGD, RMSprop, Adam
from keras.preprocessing.image import ImageDataGenerator

sys.path.insert(1, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'utils'))
from save_model import save

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)


class VGG19Simple():

    def __init__(self,
                 network_name = 'vgg19_simple',
                 dataset_name = None,
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
                 epochs = 100):

        '''
        Arguments:
            network_name: string, name of the network, default: vgg19_simple
            dataset_name: string, name of the dataset, default: None
            image_size: (int, int), size of the input images, default: None
            data_augmentation: bool, whether to use data augmentation, default: False
            batch_size: int, batch size during network training, default: 32
            classes: int, number of classes in dataset, default: None
            weights: 'imagenet' (pre-training on ImageNet) or path to weights file to be loaded, defualt: 'imagenet'
            include_top: bool, whether to include the 3 fully-connected layers at the top of the network, default: False
            loss: string, loss function for model training, default: 'categorical_crossentropy'
            learning_rate: float, optimizer learning rate, default: 1e-4
            optimizer: optimizer for model training, options: rmsprop, adam, sgd, default: rmsprop
            metrics: list of strings, metrics for model training, default: ['acc']
            epochs: int, number of epochs to train
        '''
        _logger.info('VGG19Simple constructor...')

        self.network_name = network_name
        self.dataset_name = dataset_name

        if image_size is None:
            try:
                dataset_path = os.path.join(os.path.abspath(__file__), '..', 'data', dataset_name)
                category_path = [ f.path for f in os.scandir(os.path.join(dataset_path, 'train')) if f.is_dir() ][0]
                image_path = [im.path for im in os.scandir(category_path) if im.is_file()][0]
                image = Image.open(image_path)
                self.image_size = image.size
            except Exception as e:
                print('Error caught in constructor while getting image size: ', e)
        else:
            self.image_size = image_size

        self.data_augmentation = data_augmentation
        self.batch_size = batch_size
        if classes is None:
            try:
                dataset_path = os.path.join(os.path.abspath(__file__), '..', 'data', dataset_name)
                self.classes = len([ f.path for f in os.scandir(os.path.join(dataset_path, 'train')) if f.is_dir() ])
            except Exception as e:
                print('Error caught in constructor while getting number of classes: ', e)
        else:
            self.classes = classes
        self.data_generators()

        self.weights = weights
        self.include_top = include_top
        self.build()

        self.loss = loss
        self.learning_rate = learning_rate
        self.optimizer = optimizer
        self.metrics = metrics
        self.compile()

        self.epochs = epochs
        self.train()

        self.predict()

        save(self)


    def data_generators(self):
        _logger.info('Setting data generators...')
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
                os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', self.dataset_name, self.dataset_name + '_train'),
                target_size = self.image_size,
                batch_size = self.batch_size,
                class_mode = 'categorical' if self.classes>1 else 'binary')

        self.validation_generator = validation_test_datagen.flow_from_directory(
                os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', self.dataset_name, self.dataset_name + '_validation'),
                target_size = self.image_size,
                batch_size = self.batch_size,
                class_mode = 'categorical' if self.classes>1 else 'binary')

        self.test_generator = validation_test_datagen.flow_from_directory(
                os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', self.dataset_name, self.dataset_name + '_test'),
                target_size = self.image_size,
                batch_size = self.batch_size,
                class_mode = 'categorical' if self.classes>1 else 'binary')


    def build(self):
        _logger.info('Building the model...')
        input_shape = list(self.image_size)
        input_shape.insert(2, 3)
        input_shape = tuple(input_shape)
        convolutional_base = VGG19(weights = self.weights,
                                        include_top = self.include_top,
                                        input_shape = input_shape)

        if self.include_top is False:
            flatten = Flatten(name = 'flatten')(convolutional_base.outputs)
            dropout_1 = Dropout(0.5, name = 'dropout_1')(flatten)
            dense_1 = Dense(256, activation = 'relu', name = 'dense')(dropout_1)
            dropout_2 = Dropout(0.5, name = 'dropout_2')(dense_1)
            output = Dense(8, activation = 'softmax', name = 'predictions')(dropout_2)
            model = Model(inputs = convolutional_base.inputs, outputs = output)
            self.model = model
        else:
            self.model = convolutional_base


    def compile(self):
        _logger.info('Compiling the model...')
        optimizer_dict = {'sgd': SGD(learning_rate=self.learning_rate),
                          'rmsprop': RMSprop(learning_rate = self.learning_rate),
                          'adam': Adam(learning_rate = self.learning_rate)}
        self.model.compile(loss = self.loss,
                           optimizer = optimizer_dict[self.optimizer],
                           metrics = self.metrics)


    def train(self):
        _logger.info('Training the model...')
        self.history = self.model.fit_generator(self.train_generator,
                                                steps_per_epoch = 100,
                                                epochs = self.epochs,
                                                validation_data = self.validation_generator,
                                                validation_steps = 50)



    def predict(self):
        _logger.info('Predicting test dataset classes...')
        predictions = self.model.predict_generator(self.test_generator)
        self.predictions = np.argmax(predictions, axis=1)


def main():
    _logger.info('main()...')
    model = VGG19Simple(network_name = 'VGG19Test',
                        dataset_name = 'break_his',
                        image_size = (700, 460),
                        data_augmentation = True,
                        batch_size = 1,
                        classes = 8,
                        weights = 'imagenet',
                        include_top = False,
                        loss = 'categorical_crossentropy',
                        learning_rate = 1e-4,
                        optimizer = 'rmsprop',
                        metrics = ['acc'],
                        epochs = 1)

if __name__ == '__main__':
    _logger.info('Started the program...')
    main()
