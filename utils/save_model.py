import os
import matplotlib.pyplot as plt
import logging
import pandas as pd
from datetime import datetime

from sklearn.metrics import confusion_matrix


logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)


def create_directory_and_txt_file(network_name):
    _logger.info('Creating output directory and .txt file...')
    current_time = datetime.now()
    current_time = current_time.strftime("_%d-%m-%Y_%H:%M:%S")
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'experiments', network_name + current_time)
    os.mkdir(directory)
    file_path = os.path.join(directory, network_name + current_time + '.txt')
    file = open(file_path, 'w+')
    file.close()
    return directory, file_path


def save_arguments(file, network):
    _logger.info('Saving the arguments...')

    for attribute, value in network.__dict__.items():
        if not callable(attribute):
            file.write('\n' + str(attribute) + ': ' + str(value))
    file.write('\n\n')


def save_model_architecture(file, model):
    _logger.info('Saving the model architecture...')
    model.summary(print_fn = lambda x: file.write(x + '\n'))


def save_train_history(file, epochs, history):
    _logger.info('Saving the train history...')
    train_history = {'accuracy': history.history['acc'],
                     'loss': history.history['loss'],
                     'validation accuracy': history.history['val_acc'],
                     'validation loss': history.history['val_loss']}
    df = pd.DataFrame(train_history)
    file.write('\n\n' + 'training and validation accuracy and loss: \n\n' + str(df))


def save_train_plots(directory, history):
    _logger.info('Saving the accuracy and loss plots...')
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs = range(1, len(acc) + 1)

    plt.plot(epochs, acc, 'bo', label='Training acc')
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.savefig(fname = directory + '/accuracy_plot.png', bbox_inches = 'tight')
    plt.legend()
    plt.figure()
    plt.plot(epochs, loss, 'bo', label='Training loss')
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.savefig(fname = directory + '/loss_plot.png', bbox_inches = 'tight')
    plt.legend()
    plt.figure()
    plt.cla()
    plt.clf()
    plt.close('all')


def save_confusion_matrix(file, validation_generator, predictions):
    _logger.info('Saving the confusion matrix...')
    confusion_matrix_text = str(confusion_matrix(validation_generator.classes, predictions))
    file.write('\n\n' + 'confusion matrix: \n\n' + confusion_matrix_text)


def save_test_results(file, model, test_generator, dataset_count, batch_size):
    _logger.info('Saving the test dataset results...')
    result = model.evaluate_generator(test_generator,
                                      steps=int(dataset_count[2]/batch_size) if dataset_count is not None else 20)
    file.write('\n\ntest accuracy: ' + str(result[1]) + '\ntest loss: ' + str(result[0]))


def save_as_h5(directory, model, name):
    _logger.info('Saving the model as .h5 file...')
    model.save(os.path.join(directory, name + '.h5'))


def save_model(network):
    _logger.info('Started saving the model...')
    directory, file_path = create_directory_and_txt_file(network.network_name)
    file = open(file_path, 'a+')

    save_arguments(file, network)
    save_model_architecture(file, network.model)
    save_train_history(file, network.epochs, network.history)
    save_train_plots(directory, network.history)
    save_confusion_matrix(file, network.validation_generator, network.predictions)
    save_test_results(file, network.model, network.test_generator, network.dataset_count, network.batch_size)
    save_as_h5(directory, network.model, network.network_name)

    file.close()
