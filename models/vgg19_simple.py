import os
import logging
from keras.models import Model
from models.base_cnn import BaseCNN
from keras.applications import VGG19
from utils.save_model import save_model
from keras.layers import Input, Flatten, Dropout, Dense
from keras.preprocessing.image import ImageDataGenerator


# disable tensorflow logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)


class VGG19Simple(BaseCNN):

    def __init__(self,
                 network_name='vgg19_simple',
                 dataset_name='break_his',
                 dataset_count=(1463, 309, 309),
                 classes=['ADE', 'DUC', 'FIB', 'LOB', 'MUC', 'PAP', 'PHY', 'TUB'],
                 image_size=None,
                 data_augmentation=False,
                 batch_size=16,
                 weights='imagenet',
                 include_top=False,
                 loss='categorical_crossentropy',
                 learning_rate=1e-4,
                 optimizer='rmsprop',
                 metrics=['acc'],
                 epochs=100,
                 fine_tune=False,
                 first_trainable_block=5,
                 fine_tune_learning_rate=1e-5,
                 fine_tune_epochs=100,
                 skip_filters=True):

        '''
        Arguments:
            network_name: string, name of the network, default: vgg19_simple
            dataset_name: string, name of the dataset, default: break_his
            dateset_count: (int, int, int), number of images in train, validation, test set, default: (1463, 309, 309)
            classes: list of strings, classes of dataset, default: ['ADE', 'DUC', 'FIB', 'LOB', 'MUC', 'PAP', 'PHY', 'TUB']
            image_size: (int, int), size of the input images, default: None
            data_augmentation: bool, whether to use data augmentation, default: False
            batch_size: int, batch size during network training, default: 16
            weights: 'imagenet' (pre-training on ImageNet) or path to weights file to be loaded, defualt: 'imagenet'
            include_top: bool, whether to include the 3 fully-connected layers at the top of the network, default: False
            loss: string, loss function used as feedback signal for learning the weighs, default: 'categorical_crossentropy'
            learning_rate: float, optimizer learning rate (magnitude of the move), default: 1e-4
            optimizer: optimizer for model training (variant of SGD), options: rmsprop, adam, sgd, default: rmsprop
            metrics: list of strings, metrics to monitor during model training, default: ['acc']
            epochs: int, number of epochs to train
            fine_tune: bool, whether to fine tune the model, default: False
            first_trainable_block: 1-5, first block to set to trainable if fine tuning, default: 5
            fine_tune_learning_rate: float, optimizer learning rate if fine tuning, default: 1e-5
            fine_tune_epochs: int, number of epochs to train fine tunes model
            skip_filters: bool, whether to skip creation of filter patterns for separate conv layers, default: True
        '''

        super().__init__(network_name,
                         dataset_name,
                         dataset_count,
                         classes,
                         image_size,
                         data_augmentation,
                         batch_size,
                         loss,
                         learning_rate,
                         optimizer,
                         metrics,
                         epochs,
                         skip_filters)

        _logger.info('VGG19Simple...')

        self.data_generators()

        self.weights = weights
        self.include_top = include_top
        self.build()

        self.compile(self.learning_rate)
        self.train(self.epochs)
        self.predict()
        save_model(self)

        self.fine_tune = fine_tune
        if self.fine_tune is True:
            if first_trainable_block >= 1 and first_trainable_block <= 5:
                self.first_trainable_block = first_trainable_block
            else:
                self.first_trainable_block = 5
            self.fine_tune_learning_rate = fine_tune_learning_rate
            self.fine_tune_epochs = fine_tune_epochs
        else:
            self.first_trainable_block = None
            self.fine_tune_learning_rate = None
            self.fine_tune_epochs = None

        if self.fine_tune is True:
            self.fine_tune_model()
            self.compile(self.fine_tune_learning_rate)
            self.train(self.fine_tune_epochs)
            self.predict()
            save_model(self)

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

        input = Input(list(input_shape))
        self.convolutional_base = VGG19(weights=self.weights,
                                        include_top=self.include_top,
                                        input_tensor=input)
        for layer in self.convolutional_base.layers:
            layer.trainable = False

        if self.include_top is False:
            x = Flatten(name='flatten')(self.convolutional_base.output)
            x = Dense(512, activation='relu', name='dense_1')(x)
            x = Dropout(0.5, name='dropout_1')(x)
            x = Dense(1024, activation='relu', name='dense_2')(x)
            x = Dropout(0.5, name='dropout_2')(x)
            x = Dense(len(self.classes), activation='softmax', name='predictions')(x)

            model = Model(input, x)
            self.model = model
        else:
            model = Model(input, self.convolutional_base)

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
