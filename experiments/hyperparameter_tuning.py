import logging
from models.cnn_simple import CNNSimple
from models.vgg19_simple import VGG19Simple


logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)


def create_cnn_simple(cnn_simple_parameter_dictonary):
    for i in range(cnn_simple_parameter_dictonary['model_number']):
        _logger.info('Creating CNNSimple object number ' + str(i) + '...')

        model = CNNSimple(network_name='CNNSimple',  # NOQA: F841
                          dataset_name='nct_crc_he_100k',
                          dataset_count=(70010, 14995, 14995),
                          classes=['ADI', 'BACK', 'CAS', 'CAE', 'DEB', 'LYM', 'MUC', 'NCM', 'SM'],
                          image_size=(150, 150),
                          data_augmentation=True,
                          batch_size=64,
                          loss='categorical_crossentropy',
                          learning_rate=cnn_simple_parameter_dictonary['learning_rate'][i],
                          optimizer=cnn_simple_parameter_dictonary['optimizer'][i],
                          metrics=['acc'],
                          epochs=cnn_simple_parameter_dictonary['epochs'][i])  # NOQA: F841

    return 0


def create_vgg19_simple(vgg19_simple_parameter_dictonary):
    for i in range(vgg19_simple_parameter_dictonary['model_number']):
        _logger.info('Creating VGG19Simple object number ' + str(i+1) + '...')

        model = VGG19Simple(network_name='VGG19Simple',  # NOQA: F841
                            dataset_name='break_his',
                            dataset_count=(1463, 309, 309),
                            classes=['ADE', 'DUC', 'FIB', 'LOB', 'MUC', 'PAP', 'PHY', 'TUB'],
                            image_size=(150, 150),
                            data_augmentation=True,
                            batch_size=64,
                            weights='imagenet',
                            include_top=False,
                            loss='categorical_crossentropy',
                            learning_rate=vgg19_simple_parameter_dictonary['learning_rate'][i],
                            optimizer=vgg19_simple_parameter_dictonary['optimizer'][i],
                            metrics=['acc'],
                            epochs=vgg19_simple_parameter_dictonary['epochs'][i],
                            skip_filters=True,
                            fine_tune=True,
                            first_trainable_block=vgg19_simple_parameter_dictonary['first_trainable_block'][i],
                            fine_tune_learning_rate=vgg19_simple_parameter_dictonary['fine_tune_learning_rate'][i],
                            fine_tune_epochs=vgg19_simple_parameter_dictonary['fine_tune_epochs'][i])

    return 0


def main(cnn_simple_parameter_dictonary, vgg19_simple_parameter_dictonary):
    try:
        create_cnn_simple(cnn_simple_parameter_dictonary)
        create_vgg19_simple(vgg19_simple_parameter_dictonary)
    except Exception as e:
        _logger.info('Exception caught in main: {}'.format(e), exc_info=True)
        return 1
    return 0


if __name__ == '__main__':
    cnn_simple_parameter_dictonary = {'model_number': 1,
                                      'learning_rate': [2e-5],
                                      'optimizer': ['rmsprop'],
                                      'epochs': [70]}

    vgg19_simple_parameter_dictonary = {'model_number': 4,
                                        'learning_rate': [1e-4, 1e-4, 1e-4, 1e-4],
                                        'optimizer': ['rmsprop', 'rmsprop', 'rmsprop', 'rmsprop'],
                                        'epochs': [75, 75, 75, 75],
                                        'first_trainable_block': [4, 4, 4, 4],
                                        'fine_tune_learning_rate': [2e-5, 2e-5, 3e-5, 3e-5],
                                        'fine_tune_epochs': [50, 100, 50, 100]}

    exit(main(cnn_simple_parameter_dictonary, vgg19_simple_parameter_dictonary))
