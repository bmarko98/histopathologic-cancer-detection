import os
import logging
import pandas as pd
import seaborn as sns
from datetime import datetime
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from utils.visualize_filters import visualize_filters


logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

sns.set_style('darkgrid')


def create_directory_and_txt_file(network_name, dataset_name, save_dir=None):
    _logger.info('Creating output directories and .txt file...')

    current_time = datetime.now()
    current_time = current_time.strftime("_%d-%m-%Y_%H:%M:%S")
    base_directory = save_dir if save_dir is not None else os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                                        '..', 'experiments', dataset_name + '_models',
                                                                        network_name + current_time)
    plots_directory = os.path.join(base_directory, 'plots')
    filter_directory = os.path.join(base_directory, 'conv_filters')
    os.mkdir(base_directory)
    os.mkdir(plots_directory)
    os.mkdir(filter_directory)
    file_path = os.path.join(base_directory, network_name + '.txt')
    file = open(file_path, 'w+')
    file.close()

    return base_directory, plots_directory, filter_directory, file_path


def save_arguments(file, network):
    _logger.info('Saving the arguments...')

    for attribute, value in network.__dict__.items():
        if not callable(attribute):
            file.write('\n' + str(attribute) + ': ' + str(value))
    file.write('\n\n')


def save_model_architecture(file, model):
    _logger.info('Saving the model architecture...')
    file.write('\n')
    model.summary(print_fn=lambda x: file.write(x + '\n'))


def save_train_history(file, epochs, history):
    _logger.info('Saving the train history...')
    train_history = {'accuracy': history.history['acc'],
                     'loss': history.history['loss'],
                     'validation accuracy': history.history['val_acc'],
                     'validation loss': history.history['val_loss']}
    df = pd.DataFrame(train_history)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    file.write('\n\n' + 'training and validation accuracy and loss: \n\n' + str(df))


def save_train_history_plots(directory, history):
    _logger.info('Saving the accuracy and loss plots...')
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs = range(1, len(acc) + 1)

    plt.plot(epochs, acc, 'bo', label='Training acc')
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.title('Training and validation accuracy')
    accuracy_plot_path = os.path.join(directory, 'accuracy_plot.png')
    plt.savefig(fname=accuracy_plot_path, bbox_inches='tight')
    plt.legend()
    plt.figure()
    plt.plot(epochs, loss, 'bo', label='Training loss')
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    loss_plot_path = os.path.join(directory, 'loss_plot.png')
    plt.savefig(fname=loss_plot_path, bbox_inches='tight')
    plt.legend()
    plt.figure()
    plt.cla()
    plt.clf()
    plt.close('all')


def save_confusion_matrix_plot(directory, test_generator, predictions, classes):
    _logger.info('Saving the confusion matrix plot...')
    cm = confusion_matrix(test_generator.classes, predictions)
    df_cm = pd.DataFrame(cm, index=classes, columns=classes)
    plt.figure(figsize=(10, 7))
    ax = sns.heatmap(df_cm, annot=True, fmt='g')
    bottom, top = ax.get_ylim()
    ax.set_ylim(bottom + 0.5, top - 0.5)
    confusion_matrix_plot_path = os.path.join(directory, 'confusion_matrix.png')
    plt.savefig(fname=confusion_matrix_plot_path)
    plt.cla()
    plt.clf()
    plt.close('all')


def save_test_results(file, model, test_generator, dataset_count, batch_size):
    _logger.info('Saving the test dataset results...')
    result = model.evaluate_generator(test_generator,
                                      steps=int(dataset_count[2]/batch_size) if dataset_count is not None else 20)
    file.write('\n\ntest accuracy: ' + str(result[1]) + '\ntest loss: ' + str(result[0]))


def save_as_h5(directory, model, network_name):
    _logger.info('Saving the model as .h5 file...')
    model.save(os.path.join(directory, network_name + '.h5'))


def save_plots(directory, network):
    save_train_history_plots(directory, network.history)
    save_confusion_matrix_plot(directory, network.test_generator, network.predictions, network.classes)


def save_model(network, save_dir=None):
    _logger.info('Started saving the model...')

    base_directory, plots_directory, filter_directory, file_path = create_directory_and_txt_file(network.network_name,
                                                                                                 network.dataset_name,
                                                                                                 save_dir)
    file = open(file_path, 'a+')
    save_arguments(file, network)
    save_model_architecture(file, network.model)
    save_train_history(file, network.epochs, network.history)
    save_plots(plots_directory, network)
    save_test_results(file, network.model, network.test_generator, network.dataset_count, network.batch_size)
    if network.skip_filters is False:
        visualize_filters(network.model, filter_directory)
    save_as_h5(base_directory, network.model, network.network_name)
    file.close()

    return 0
