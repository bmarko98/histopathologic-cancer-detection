import numpy as np
from keras.preprocessing import image
from PyQt5 import QtGui, QtWidgets
import gui.config as CONFIG
import gui.gui_components as GUI
from gui.window import Window
from gui.help.simple_window import SimpleWindow
from utils.misc import file_get_contents


class AboutModelsWindow(Window):

    def set_about_models_window(self, AboutModelsWindow, ABOUT_MODELS_CONFIG):
        super().set_window(AboutModelsWindow, ABOUT_MODELS_CONFIG)

    def create_central_widget(self, AboutModelsWindow, ABOUT_MODELS_CONFIG):
        super().create_central_widget(AboutModelsWindow, ABOUT_MODELS_CONFIG)
        self.modelNameLabel = GUI.get_label(self.centralwidget,
                                            *ABOUT_MODELS_CONFIG['MODEL_NAME_LABEL_POSITION'],
                                            CONFIG.FONT,
                                            False,
                                            ABOUT_MODELS_CONFIG['MODEL_NAME_LABEL_NAME'])
        self.modelSummaryLabel = GUI.get_label(self.centralwidget,
                                               *ABOUT_MODELS_CONFIG['MODEL_SUMMARY_LABEL_POSITION'],
                                               CONFIG.FONT,
                                               False,
                                               ABOUT_MODELS_CONFIG['MODEL_SUMMARY_LABEL_NAME'])
        self.accuracyLabel = GUI.get_image_label(self.centralwidget,
                                                 *ABOUT_MODELS_CONFIG['ACCURACY_LABEL_POSITION'],
                                                 CONFIG.FONT,
                                                 True,
                                                 ABOUT_MODELS_CONFIG['ACCURACY_LABEL_NAME'],
                                                 ABOUT_MODELS_CONFIG['ACCURACY_PATH'])
        self.lossLabel = GUI.get_image_label(self.centralwidget,
                                             *ABOUT_MODELS_CONFIG['LOSS_LABEL_POSITION'],
                                             CONFIG.FONT,
                                             True,
                                             ABOUT_MODELS_CONFIG['LOSS_LABEL_NAME'],
                                             ABOUT_MODELS_CONFIG['LOSS_PATH'])
        self.confMatrixLabel = GUI.get_image_label(self.centralwidget,
                                                   *ABOUT_MODELS_CONFIG['CONF_MATRIX_LABEL_POSITION'],
                                                   CONFIG.FONT,
                                                   True,
                                                   ABOUT_MODELS_CONFIG['CONF_MATRIX_LABEL_NAME'],
                                                   ABOUT_MODELS_CONFIG['CONF_MATRIX_PATH'])
        self.accuracy_path = ABOUT_MODELS_CONFIG['ACCURACY_PATH']
        self.loss_path = ABOUT_MODELS_CONFIG['LOSS_PATH']
        self.conf_matrix_path = ABOUT_MODELS_CONFIG['CONF_MATRIX_PATH']
        AboutModelsWindow.setCentralWidget(self.centralwidget)

    def retranslate(self, AboutModelsWindow, ABOUT_MODELS_CONFIG):
        super().retranslate(AboutModelsWindow, ABOUT_MODELS_CONFIG)
        self.modelNameLabel.setText(self._translate(ABOUT_MODELS_CONFIG['WINDOW_NAME'],
                                                    ABOUT_MODELS_CONFIG['MODEL_NAME']))
        self.modelSummaryLabel.setText(self._translate(ABOUT_MODELS_CONFIG['WINDOW_NAME'],
                                                       file_get_contents(ABOUT_MODELS_CONFIG['MODEL_SUMMARY_PATH'])))
    def simpleWindow(self, SIMPLE_CONFIG):
        self.SimpleWindow = QtWidgets.QMainWindow()
        self.simple_window = SimpleWindow()
        self.simple_window.setup(self.SimpleWindow, SIMPLE_CONFIG)
        self.SimpleWindow.show()

    def accuracyImageClickedEvent(self, event):
        self.imageClickedEvent(self.accuracy_path)

    def lossImageClickedEvent(self, event):
        self.imageClickedEvent(self.loss_path)

    def confMatrixImageClickedEvent(self, event):
        self.imageClickedEvent(self.conf_matrix_path)

    def imageClickedEvent(self, image_path):
        img = image.load_img(image_path)
        np_img = image.img_to_array(img)
        np_img = np.expand_dims(np_img, axis=0)
        np_img /= 255.
        CONFIG.SIMPLE_CONFIG['IMAGE']['WINDOW_X'] = np_img.shape[2]
        CONFIG.SIMPLE_CONFIG['IMAGE']['WINDOW_Y'] = np_img.shape[1]
        CONFIG.SIMPLE_CONFIG['IMAGE']['SIMPLE_INFO_LABEL_POSITION'] = [0, 0, np_img.shape[2], np_img.shape[1]]
        CONFIG.SIMPLE_CONFIG['IMAGE']['SIMPLE_INFO_LABEL_IMAGE_PATH'] = image_path
        self.simpleWindow(CONFIG.SIMPLE_CONFIG['IMAGE'])

    def setup(self, AboutModelsWindow, ABOUT_MODELS_CONFIG):
        super().setup(AboutModelsWindow, ABOUT_MODELS_CONFIG)
        self.accuracyLabel.mousePressEvent = self.accuracyImageClickedEvent
        self.lossLabel.mousePressEvent = self.lossImageClickedEvent
        self.confMatrixLabel.mousePressEvent = self.confMatrixImageClickedEvent
