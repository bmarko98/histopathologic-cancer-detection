import numpy as np
from keras.preprocessing import image
from PyQt5 import QtCore, QtGui, QtWidgets
import gui.config as CONFIG
import gui.gui_components as GUI
from gui.window import Window
from gui.help.simple_window import SimpleWindow
from utils.misc import file_get_contents


class AboutDatasetsWindow(Window):

    def set_about_datasets_window(self, AboutDatasetsWindow, ABOUT_DATASETS_CONFIG):
        super().set_about_window(AboutDatasetsWindow, ABOUT_DATASETS_CONFIG)

    def create_central_widget(self, AboutDatasetsWindow, ABOUT_DATASETS_CONFIG):
        super().create_central_widget(AboutDatasetsWindow, ABOUT_DATASETS_CONFIG)
        self.datasetOverviewLabel = GUI.get_label(self.centralwidget,
                                                  *ABOUT_DATASETS_CONFIG['OVERVIEW_LABEL_POSITION'],
                                                  CONFIG.FONT,
                                                  False,
                                                  ABOUT_DATASETS_CONFIG['OVERVIEW_LABEL_NAME'],
                                                  QtCore.Qt.AlignLeft)
        self.datasetImagesLabel = GUI.get_image_label(self.centralwidget,
                                                      *ABOUT_DATASETS_CONFIG['IMAGES_LABEL_POSITIONS'],
                                                      CONFIG.FONT,
                                                      True,
                                                      ABOUT_DATASETS_CONFIG['IMAGES_LABEL_NAME'],
                                                      ABOUT_DATASETS_CONFIG['IMAGES_URL'])
        self.image_path = ABOUT_DATASETS_CONFIG['IMAGES_URL']
        AboutDatasetsWindow.setCentralWidget(self.centralwidget)

    def retranslate(self, AboutDatasetsWindow, ABOUT_DATASETS_CONFIG):
        super().retranslate(AboutDatasetsWindow, ABOUT_DATASETS_CONFIG)
        self.datasetOverviewLabel.setText(self._translate(ABOUT_DATASETS_CONFIG['WINDOW_NAME'],
                                                          file_get_contents(ABOUT_DATASETS_CONFIG['DATASET_OVERVIEW_PATH'])))

    def simpleWindow(self, SIMPLE_CONFIG):
        self.SimpleWindow = QtWidgets.QMainWindow()
        self.simple_window = SimpleWindow()
        self.simple_window.setup(self.SimpleWindow, SIMPLE_CONFIG)
        self.SimpleWindow.show()

    def datasetImageClickedEvent(self, event):
        img = image.load_img(self.image_path)
        np_img = image.img_to_array(img)
        np_img = np.expand_dims(np_img, axis=0)
        np_img /= 255.
        CONFIG.SIMPLE_CONFIG['IMAGE']['WINDOW_X'] = np_img.shape[2]
        CONFIG.SIMPLE_CONFIG['IMAGE']['WINDOW_Y'] = np_img.shape[1]
        CONFIG.SIMPLE_CONFIG['IMAGE']['SIMPLE_INFO_LABEL_POSITION'] = [0, 0, np_img.shape[2], np_img.shape[1]]
        CONFIG.SIMPLE_CONFIG['IMAGE']['SIMPLE_INFO_LABEL_IMAGE_PATH'] = self.image_path
        self.simpleWindow(CONFIG.SIMPLE_CONFIG['IMAGE'])

    def setup(self, AboutDatasetsWindow, ABOUT_DATASETS_CONFIG):
        super().setup(AboutDatasetsWindow, ABOUT_DATASETS_CONFIG)
        self.datasetImagesLabel.mousePressEvent = self.datasetImageClickedEvent
