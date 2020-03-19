import logging

from models.cnn_simple import CNNSimple
from models.vgg19_simple import VGG19Simple


logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

cnn_simple_parameter_dictonary = {'model_number': 1,
                                  'learning_rate': [2e-5],
                                  'optimizer': ['rmsprop'],
                                  'epochs': [1]}


vgg19_simple_parameter_dictonary = {'model_number': 1,
                                    'learning_rate': [1e-4],
                                    'optimizer': ['rmsprop'],
                                    'epochs': [1],
                                    'first_trainable_block': [5],
                                    'fine_tune_learning_rate': [1e-4],
                                    'fine_tune_epochs': [1]}


def fine_tune_cnn_simple():
    for i in range(cnn_simple_parameter_dictonary['model_number']):
        _logger.info('Creating CNNSimple object number ' + str(i) + '...')

        model = CNNSimple(network_name='CNNSimpleTest',  # NOQA: F841
                          dataset_name='nct_crc_he_100k',
                          dataset_count=(70010, 14995, 14995),
                          classes=['ADI', 'BACK', 'CAS', 'CAE', 'DEB', 'LYM', 'MUC', 'NCM', 'SM'],
                          image_size=(150, 150),
                          data_augmentation=True,
                          batch_size=32,
                          loss='categorical_crossentropy',
                          learning_rate=cnn_simple_parameter_dictonary['learning_rate'][i],
                          optimizer=cnn_simple_parameter_dictonary['optimizer'][i],
                          metrics=['acc'],
                          epochs=cnn_simple_parameter_dictonary['epochs'][i])  # noqa: F841


def fine_tune_vgg19_simple():
    for i in range(vgg19_simple_parameter_dictonary['model_number']):
        _logger.info('Creating VGG19Simple object number ' + str(i) + '...')

        model = VGG19Simple(network_name='VGG19Test',  # NOQA: F841
                            dataset_name='break_his',
                            dataset_count=(1463, 309, 309),
                            classes=['ADE', 'DUC', 'FIB', 'LOB', 'MUC', 'PAP', 'PHY', 'TUB'],
                            image_size=(150, 150),
                            data_augmentation=True,
                            batch_size=32,
                            weights='imagenet',
                            include_top=False,
                            loss='categorical_crossentropy',
                            learning_rate=vgg19_simple_parameter_dictonary['learning_rate'][i],
                            optimizer=vgg19_simple_parameter_dictonary['optimizer'][i],
                            metrics=['acc'],
                            epochs=vgg19_simple_parameter_dictonary['epochs'][i],
                            skip_filters=False,
                            fine_tune=False,
                            first_trainable_block=vgg19_simple_parameter_dictonary['first_trainable_block'][i],
                            fine_tune_learning_rate=vgg19_simple_parameter_dictonary['fine_tune_learning_rate'][i],
                            fine_tune_epochs=vgg19_simple_parameter_dictonary['fine_tune_epochs'][i])


def main():
    fine_tune_cnn_simple()
    fine_tune_vgg19_simple()


if __name__ == '__main__':
    _logger.info('Started the program...')
    main()
