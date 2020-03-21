import numpy as np
from keras.preprocessing import image
from PyQt5 import QtGui, QtWidgets
import gui.config as CONFIG
import gui.gui_components as GUI
from gui.window import Window
from gui.help.simple_window import SimpleWindow


class HeatmapWindow(Window):

    def set_heatmap_window(self, HeatmapWindow, HEATMAP_CONFIG):
        super().set_window(HeatmapWindow, HEATMAP_CONFIG)

    def create_central_widget(self, HeatmapWindow, HEATMAP_CONFIG):
        super().create_central_widget(HeatmapWindow, HEATMAP_CONFIG)
        self.imageTextLabel = GUI.get_label(self.centralwidget,
                                            *HEATMAP_CONFIG['IMAGE_TEXT_LABEL_POSITION'],
                                            CONFIG.FONT,
                                            False,
                                            HEATMAP_CONFIG['IMAGE_TEXT_LABEL_NAME'])
        self.heatmapTextLabel = GUI.get_label(self.centralwidget,
                                              *HEATMAP_CONFIG['HEATMAP_TEXT_LABEL_POSITION'],
                                              CONFIG.FONT,
                                              False,
                                              HEATMAP_CONFIG['HEATMAP_TEXT_LABEL_NAME'])
        self.inputImageLabel = GUI.get_image_label(self.centralwidget,
                                                   *HEATMAP_CONFIG['INPUT_IMAGE_LABEL_POSITION'],
                                                   CONFIG.FONT,
                                                   True,
                                                   HEATMAP_CONFIG['INPUT_IMAGE_LABEL_NAME'],
                                                   HEATMAP_CONFIG['INPUT_IMAGE_PATH'])
        self.heatmapImageLabel = GUI.get_image_label(self.centralwidget,
                                                     *HEATMAP_CONFIG['HEATMAP_IMAGE_LABEL_POSITION'],
                                                     CONFIG.FONT,
                                                     True,
                                                     HEATMAP_CONFIG['HEATMAP_IMAGE_LABEL_NAME'],
                                                     HEATMAP_CONFIG['HEATMAP_IMAGE_PATH'])
        HeatmapWindow.setCentralWidget(self.centralwidget)

    def retranslate(self, HeatmapWindow, HEATMAP_CONFIG):
        super().retranslate(HeatmapWindow, HEATMAP_CONFIG)
        self.imageTextLabel.setText(self._translate(HEATMAP_CONFIG['WINDOW_NAME'],
                                                    HEATMAP_CONFIG['IMAGE_TEXT_LABEL_TEXT']))
        self.heatmapTextLabel.setText(self._translate(HEATMAP_CONFIG['WINDOW_NAME'],
                                                      HEATMAP_CONFIG['HEATMAP_TEXT_LABEL_TEXT']))

    def simpleWindow(self, SIMPLE_CONFIG):
        self.SimpleWindow = QtWidgets.QMainWindow()
        self.simple_window = SimpleWindow()
        self.simple_window.setup(self.SimpleWindow, SIMPLE_CONFIG)
        self.SimpleWindow.show()

    def inputImageClickedEvent(self, event):
        self.imageClickedEvent(CONFIG.HEATMAP_CONFIG['INPUT_IMAGE_PATH'])

    def heatmapImageClickedEvent(self, event):
        self.imageClickedEvent(CONFIG.HEATMAP_CONFIG['HEATMAP_IMAGE_PATH'])

    def imageClickedEvent(self, image_path):
        print('PATH: ', image_path)
        img = image.load_img(image_path)
        np_img = image.img_to_array(img)
        np_img = np.expand_dims(np_img, axis=0)
        np_img /= 255.
        CONFIG.SIMPLE_CONFIG['IMAGE']['WINDOW_X'] = np_img.shape[2]
        CONFIG.SIMPLE_CONFIG['IMAGE']['WINDOW_Y'] = np_img.shape[1]
        CONFIG.SIMPLE_CONFIG['IMAGE']['SIMPLE_INFO_LABEL_POSITION'] = [0, 0, np_img.shape[2], np_img.shape[1]]
        CONFIG.SIMPLE_CONFIG['IMAGE']['SIMPLE_INFO_LABEL_IMAGE_PATH'] = image_path
        self.simpleWindow(CONFIG.SIMPLE_CONFIG['IMAGE'])

    def setup(self, HeatmapWindow, HEATMAP_CONFIG):
        super().setup(HeatmapWindow, HEATMAP_CONFIG)
        self.inputImageLabel.mousePressEvent = self.inputImageClickedEvent
        self.heatmapImageLabel.mousePressEvent = self.heatmapImageClickedEvent
