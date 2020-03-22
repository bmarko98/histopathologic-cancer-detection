import os
import numpy as np
from keras.preprocessing import image
from PyQt5 import QtGui, QtWidgets
import gui.config as CONFIG
import gui.gui_components as GUI
from gui.window import Window
from gui.help.simple_window import SimpleWindow
from utils.visualize_filters import create_pattern
from utils.visualize_intermediate_activations_and_heatmaps import visualize_intermediate_activations


class InspectConvWindow(Window):

    def create_central_widget(self, InspectConvWindow, INSPECT_CONV_CONFIG):
        self.centralwidget = GUI.get_widget(InspectConvWindow, 'centralwidget')
        self.convLayerLabel = GUI.get_label(self.centralwidget,
                                            *INSPECT_CONV_CONFIG['CONV_LAYER_LABEL_POSITION'],
                                            CONFIG.FONT,
                                            False,
                                            INSPECT_CONV_CONFIG['CONV_LAYER_LABEL_NAME'])
        self.numberLabel = GUI.get_label(self.centralwidget,
                                         *INSPECT_CONV_CONFIG['NUMBER_LABEL_POSITION'],
                                         CONFIG.FONT,
                                         False,
                                         INSPECT_CONV_CONFIG['NUMBER_LABEL_NAME'])
        self.imageLabel = GUI.get_image_label(self.centralwidget,
                                              *INSPECT_CONV_CONFIG['IMAGE_LABEL_POSITION'],
                                              CONFIG.FONT,
                                              True,
                                              INSPECT_CONV_CONFIG['IMAGE_LABEL_NAME'],
                                              None)
        self.showButton = GUI.get_button(self.centralwidget,
                                         *INSPECT_CONV_CONFIG['BUTTON_POSITION'],
                                         CONFIG.FONT,
                                         INSPECT_CONV_CONFIG['BUTTON_NAME'])
        self.layerComboBox = GUI.get_combo_box(self.centralwidget,
                                               *INSPECT_CONV_CONFIG['COMBO_BOX_POSITION'],
                                               CONFIG.FONT,
                                               INSPECT_CONV_CONFIG['COMBO_BOX_ITEMS'],
                                               INSPECT_CONV_CONFIG['COMBO_BOX_NAME'])
        self.numberEdit = GUI.get_line_edit(self.centralwidget,
                                            *INSPECT_CONV_CONFIG['LINE_EDIT_POSITION'],
                                            CONFIG.FONT,
                                            INSPECT_CONV_CONFIG['LINE_EDIT_NAME'])
        InspectConvWindow.setCentralWidget(self.centralwidget)

    def retranslate(self, InspectConvWindow, INSPECT_CONV_CONFIG):
        super().retranslate(InspectConvWindow, INSPECT_CONV_CONFIG)
        self.convLayerLabel.setText(self._translate(INSPECT_CONV_CONFIG['WINDOW_NAME'],
                                                    INSPECT_CONV_CONFIG['CONV_LAYER_LABEL_TEXT']))
        self.numberLabel.setText(self._translate(INSPECT_CONV_CONFIG['WINDOW_NAME'],
                                                 INSPECT_CONV_CONFIG['NUMBER_LABEL_TEXT']))
        self.showButton.setText(self._translate(INSPECT_CONV_CONFIG['WINDOW_NAME'],
                                                INSPECT_CONV_CONFIG['BUTTON_TEXT']))
        for index, item in enumerate(INSPECT_CONV_CONFIG['COMBO_BOX_ITEMS']):
            self.layerComboBox.setItemText(index, self._translate(INSPECT_CONV_CONFIG['WINDOW_NAME'], item))

    def showButtonEvent(self):
        line_edit_text = self.numberEdit.text()
        combo_box_text = self.layerComboBox.currentText()
        if line_edit_text and combo_box_text:
            if self.showButton.objectName() == 'showActivationButton':
                if line_edit_text == 'all':
                    self.image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'temporary_plots',
                                                  'layer_activations', combo_box_text + '.png')
                    #self.imageLabel.setPixmap(QtGui.QPixmap(self.image_path))
                    self.labelClickedEvent()
                elif line_edit_text.isdigit():
                    channel_number = int(line_edit_text)
                    self.image_path = visualize_intermediate_activations(self.input_image, self.model, False, combo_box_text,
                                                                         channel_number, CONFIG.TEMPORARY_PLOTS_DIR)
                    #self.imageLabel.setPixmap(QtGui.QPixmap(self.image_path))
                    self.labelClickedEvent()
            elif self.showButton.objectName() == 'showFilterButton':
                if line_edit_text == 'all':
                    self.image_path = os.path.join(CONFIG.INSPECT_CONV_CONFIG['FILTER_PATTERNS']['FILTERS_DIR_PATH'],
                                                   combo_box_text + '_filter_patterns.png')
                    #self.imageLabel.setPixmap(QtGui.QPixmap(self.image_path))
                    self.labelClickedEvent()
                elif line_edit_text.isdigit():
                    filter_number = int(line_edit_text)
                    self.image_path = create_pattern(self.model, combo_box_text, filter_number, save=True)
                    #self.imageLabel.setPixmap(QtGui.QPixmap(self.image_path))
                    self.labelClickedEvent()

    def simpleWindow(self, SIMPLE_CONFIG):
        self.SimpleWindow = QtWidgets.QMainWindow()
        self.simple_window = SimpleWindow()
        self.simple_window.setup(self.SimpleWindow, SIMPLE_CONFIG)
        self.SimpleWindow.show()

    def labelClickedEvent(self):
        img = image.load_img(self.image_path)
        np_img = image.img_to_array(img)
        np_img = np.expand_dims(np_img, axis=0)
        np_img /= 255.
        CONFIG.SIMPLE_CONFIG['IMAGE']['WINDOW_X'] = np_img.shape[2]
        CONFIG.SIMPLE_CONFIG['IMAGE']['WINDOW_Y'] = np_img.shape[1]
        CONFIG.SIMPLE_CONFIG['IMAGE']['SIMPLE_INFO_LABEL_POSITION'] = [0, 0, np_img.shape[2], np_img.shape[1]]
        CONFIG.SIMPLE_CONFIG['IMAGE']['SIMPLE_INFO_LABEL_IMAGE_PATH'] = self.image_path
        self.simpleWindow(CONFIG.SIMPLE_CONFIG['IMAGE'])

    def setup(self, InspectConvWindow, INSPECT_CONV_CONFIG):
        super().setup(InspectConvWindow, INSPECT_CONV_CONFIG)
        self.showButton.clicked.connect(self.showButtonEvent)
        #self.imageLabel.mousePressEvent = self.labelClickedEvent
