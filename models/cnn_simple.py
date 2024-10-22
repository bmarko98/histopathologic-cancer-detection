import os
import logging
from keras.models import Sequential
from models.base_cnn import BaseCNN
from utils.save_model import save_model
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dropout, Dense


# disable tensorflow logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)


class CNNSimple(BaseCNN):

    def __init__(self,
                 network_name='cnn_simple',
                 dataset_name='nct_crc_he_100k',
                 dataset_count=(70010, 14995, 14995),
                 classes=['ADI', 'BACK', 'CAS', 'CAE', 'DEB', 'LYM', 'MUC', 'NCM', 'SM'],
                 image_size=None,
                 data_augmentation=False,
                 batch_size=16,
                 loss='categorical_crossentropy',
                 learning_rate=1e-4,
                 optimizer='rmsprop',
                 metrics=['acc'],
                 epochs=100,
                 skip_filters=True):

        '''
        Arguments:
            network_name: string, name of the network, default: cnn_simple
            dataset_name: string, name of the dataset, default: nct_crc_he_100k
            dateset_count: (int, int, int), number of images in train, validation, test set, default: (70010, 14995, 14995)
            classes: list of strings, classes of dataset, default: ['ADI', 'BACK', 'CAS', 'CAE', 'DEB', 'LYM', 'MUC', 'NCM',
                                                                    'SM']
            image_size: (int, int), size of the input images, default: None
            data_augmentation: bool, whether to use data augmentation or not, default: False
            batch_size: int, batch size during network training, default: 16
            loss: string, loss function used as feedback signal for learning the weighs, default: 'categorical_crossentropy'
            learning_rate: float, optimizer learning rate (magnitude of the move), default: 1e-4
            optimizer: optimizer for model training (variant of SGD), options: rmsprop, adam, sgd, default: rmsprop
            metrics: list of strings, metrics to monitor during model training, default: ['acc']
            epochs: int, number of epochs to train, default: 100
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

        _logger.info('CNNSimple...')

        self.data_generators()
        self.build()
        self.compile(self.learning_rate)
        self.train(self.epochs)
        self.predict()
        save_model(self)

    def data_generators(self):
        _logger.info('Setting data generators...')
        train_datagen = ImageDataGenerator(rescale=1./255,
                                           rotation_range=45,
                                           width_shift_range=0.1,
                                           height_shift_range=0.1,
                                           shear_range=0.1,
                                           zoom_range=0.1,
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
        model.add(Flatten(name='flatten'))
        # fully connected layers
        model.add(Dense(512, activation='relu', name='dense1'))
        model.add(Dropout(0.5, name='dropout1'))
        model.add(Dense(1024, activation='relu', name='dense2'))
        model.add(Dropout(0.5, name='dropout2'))
        model.add(Dense(len(self.classes), activation='softmax', name='prediction'))

        self.model = model
