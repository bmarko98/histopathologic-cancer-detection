import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

import shutil
import numpy as np
from datetime import datetime
from keras.preprocessing import image
from PyQt5 import QtCore, QtWidgets, QtGui
import gui.config as CONFIG
import gui.gui_components as GUI
from gui.window import Window
from gui.help.simple_window import SimpleWindow
from gui.help.about_models_window import AboutModelsWindow
from gui.help.about_author_window import AboutAuthorWindow
from gui.help.about_datasets_window import AboutDatasetsWindow
from gui.further_analysis.inspect_conv_window import InspectConvWindow
from utils.predict_image import predict_image


class MainWindow(Window):

    def set_main_window(self, MainWindow, MAIN_CONFIG):
        super().set_window(MainWindow, MAIN_CONFIG)

    def create_central_widget(self, MainWindow, MAIN_CONFIG):
        super().create_central_widget(MainWindow, MAIN_CONFIG)
        self.loadImageButton = GUI.get_button(self.centralwidget,
                                              *MAIN_CONFIG['LOAD_IMAGE_BUTTON_POSITION'],
                                              CONFIG.FONT,
                                              MAIN_CONFIG['LOAD_IMAGE_BUTTON_NAME'])
        self.inputImageLabel = GUI.get_image_label(self.centralwidget,
                                                   *MAIN_CONFIG['INPUT_IMAGE_POSITION'],
                                                   CONFIG.FONT,
                                                   True,
                                                   MAIN_CONFIG['INPUT_IMAGE_NAME'],
                                                   None)
        self.image_path = ''
        self.breastTissueRadioButton = GUI.get_radio_button(self.centralwidget,
                                                            *MAIN_CONFIG['BREAST_TISSUE_RADIO_BUTTON_POSITION'],
                                                            CONFIG.FONT,
                                                            MAIN_CONFIG['BREAST_TISSUE_RADIO_BUTTON_NAME'])
        self.colorectalTissueRadioButton = GUI.get_radio_button(self.centralwidget,
                                                                *MAIN_CONFIG['COLORECTAL_TISSUE_RADIO_BUTTON_POSITION'],
                                                                CONFIG.FONT,
                                                                MAIN_CONFIG['COLORECTAL_TISSUE_RADIO_BUTTON_NAME'])
        self.classifyButton = GUI.get_button(self.centralwidget,
                                             *MAIN_CONFIG['CLASSIFY_BUTTON_POSITION'],
                                             CONFIG.FONT,
                                             MAIN_CONFIG['CLASSIFY_BUTTON_NAME'])
        self.predictedClassLabel = GUI.get_label(self.centralwidget,
                                                 *MAIN_CONFIG['PREDICTED_CLASS_LABEL_POSITION'],
                                                 CONFIG.FONT,
                                                 False,
                                                 MAIN_CONFIG['PREDICTED_CLASS_LABEL_NAME'])
        self.classificationProgressBar = GUI.get_progress_bar(self.centralwidget,
                                                              *MAIN_CONFIG['PROGRESS_BAR_POSITION'],
                                                              MAIN_CONFIG['PROGRESS_BAR_NAME'])
        self.classProbabilitiesPlot = GUI.get_image_label(self.centralwidget,
                                                          *MAIN_CONFIG['CLASS_PROBABILITIES_PLOT_POSITION'],
                                                          CONFIG.FONT,
                                                          True,
                                                          MAIN_CONFIG['CLASS_PROBABILITIES_PLOT_NAME'],
                                                          None)
        self.image = None
        self.model = None
        self.plot_path = None
        self.heatmap_path = None
        self.layer_activations = False
        self.filter_patterns = False
        MainWindow.setCentralWidget(self.centralwidget)

    def create_menu(self, MainWindow, MAIN_CONFIG):
        self.menubar = GUI.get_menu_bar(MainWindow,
                                        *MAIN_CONFIG['MENU_BAR_POSITION'],
                                        CONFIG.FONT,
                                        MAIN_CONFIG['MENU_BAR_NAME'])
        self.menuFile = GUI.get_menu(self.menubar, MAIN_CONFIG['MENU']['FILE_NAME'])
        self.menuFurtherAnalysis = GUI.get_menu(self.menubar, MAIN_CONFIG['MENU']['FURTHER_ANALYSIS_NAME'])
        self.menuAbout = GUI.get_menu(self.menubar, MAIN_CONFIG['MENU']['ABOUT_NAME'])
        self.menuApplication = GUI.get_menu(self.menubar, MAIN_CONFIG['MENU']['APPLICATION_NAME'])
        self.menuDatasets = GUI.get_menu(self.menubar, MAIN_CONFIG['MENU']['DATASETS_NAME'])
        self.menuModels = GUI.get_menu(self.menubar, MAIN_CONFIG['MENU']['MODELS_NAME'])

        MainWindow.setMenuBar(self.menubar)

        self.actionAuthor = GUI.get_action(MainWindow, MAIN_CONFIG['ACTION']['AUTHOR_NAME'])
        self.actionHowTo = GUI.get_action(MainWindow, MAIN_CONFIG['ACTION']['HOW_TO_NAME'])
        self.actionBreakHis = GUI.get_action(MainWindow, MAIN_CONFIG['ACTION']['BREAK_HIS_NAME'])
        self.actionNCT_CRC_HE_100K = GUI.get_action(MainWindow, MAIN_CONFIG['ACTION']['NCT_CRC_HE_100K_NAME'])
        self.actionCNNSimple = GUI.get_action(MainWindow, MAIN_CONFIG['ACTION']['CNN_SIMPLE_NAME'])
        self.actionVGG19Simple = GUI.get_action(MainWindow, MAIN_CONFIG['ACTION']['VGG19_SIMPLE_NAME'])
        self.actionNetworkFilters = GUI.get_action(MainWindow, MAIN_CONFIG['ACTION']['MODELS_NAME'])
        self.actionIntermediateActivations = GUI.get_action(MainWindow, MAIN_CONFIG['ACTION']['INTERMEDIATE_ACTIVATIONS_NAME'])
        self.actionHeatmap = GUI.get_action(MainWindow, MAIN_CONFIG['ACTION']['HEATMAP_NAME'])
        self.actionExit = GUI.get_action(MainWindow, MAIN_CONFIG['ACTION']['EXIT_NAME'])
        self.actionSave = GUI.get_action(MainWindow, MAIN_CONFIG['ACTION']['SAVE_NAME'])
        self.actionGeneral = GUI.get_action(MainWindow, MAIN_CONFIG['ACTION']['GENERAL_NAME'])

    def add_actions(self):
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuFurtherAnalysis.addAction(self.actionIntermediateActivations)
        self.menuFurtherAnalysis.addAction(self.actionHeatmap)
        self.menuFurtherAnalysis.addSeparator()
        self.menuFurtherAnalysis.addAction(self.actionNetworkFilters)
        self.menuApplication.addAction(self.actionGeneral)
        self.menuApplication.addAction(self.actionHowTo)
        self.menuApplication.addSeparator()
        self.menuApplication.addAction(self.actionAuthor)
        self.menuDatasets.addAction(self.actionBreakHis)
        self.menuDatasets.addAction(self.actionNCT_CRC_HE_100K)
        self.menuModels.addAction(self.actionCNNSimple)
        self.menuModels.addAction(self.actionVGG19Simple)
        self.menuAbout.addAction(self.menuApplication.menuAction())
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.menuDatasets.menuAction())
        self.menuAbout.addAction(self.menuModels.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuFurtherAnalysis.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

    def retranslate(self, MainWindow, MAIN_CONFIG):
        super().retranslate(MainWindow, MAIN_CONFIG)
        self.loadImageButton.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['LOAD_IMAGE_BUTTON_TEXT']))
        self.breastTissueRadioButton.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'],
                                                             MAIN_CONFIG['BREAST_TISSUE_RADIO_BUTTON_TEXT']))
        self.colorectalTissueRadioButton.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'],
                                                                 MAIN_CONFIG['COLORECTAL_TISSUE_RADIO_BUTTON_TEXT']))
        self.classifyButton.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['CLASSIFY_BUTTON_TEXT']))
        self.menuFile.setTitle(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['MENU']['FILE_TEXT']))
        self.menuFurtherAnalysis.setTitle(self._translate(MAIN_CONFIG['WINDOW_NAME'],
                                                          MAIN_CONFIG['MENU']['FURTHER_ANALYSIS_TEXT']))
        self.menuAbout.setTitle(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['MENU']['ABOUT_TEXT']))
        self.menuApplication.setTitle(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['MENU']['APPLICATION_TEXT']))
        self.menuDatasets.setTitle(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['MENU']['DATASETS_TEXT']))
        self.menuModels.setTitle(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['MENU']['MODELS_TEXT']))
        self.actionHowTo.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['ACTION']['HOW_TO_TEXT']))
        self.actionAuthor.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['ACTION']['AUTHOR_TEXT']))
        self.actionBreakHis.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['ACTION']['BREAK_HIS_TEXT']))
        self.actionNCT_CRC_HE_100K.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'],
                                                           MAIN_CONFIG['ACTION']['NCT_CRC_HE_100K_TEXT']))
        self.actionCNNSimple.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['ACTION']['CNN_SIMPLE_TEXT']))
        self.actionVGG19Simple.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['ACTION']['VGG19_SIMPLE_TEXT']))
        self.actionNetworkFilters.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'],
                                                          MAIN_CONFIG['ACTION']['NETWORK_FILTERS_TEXT']))
        self.actionIntermediateActivations.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'],
                                                                   MAIN_CONFIG['ACTION']['INTERMEDIATE_ACTIVATIONS_TEXT']))
        self.actionHeatmap.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['ACTION']['HEATMAP_TEXT']))
        self.actionExit.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['ACTION']['EXIT_TEXT']))
        self.actionSave.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['ACTION']['SAVE_TEXT']))
        self.actionGeneral.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['ACTION']['GENERAL_TEXT']))

    def inspectConvWindow(self, INSPECT_CONV_CONFIG):
        self.InspectConvWindow = QtWidgets.QMainWindow()
        self.inspect_conv_window = InspectConvWindow()
        self.inspect_conv_window.input_image = self.image
        self.inspect_conv_window.model = self.model
        self.inspect_conv_window.setup(self.InspectConvWindow, INSPECT_CONV_CONFIG)
        self.InspectConvWindow.show()

    def layerActivationsWindow(self):
        if self.layer_activations:
            self.inspectConvWindow(CONFIG.INSPECT_CONV_CONFIG['LAYER_ACTIVATIONS'])

    def filterPatternsWindow(self):
        if self.filter_patterns:
            self.inspectConvWindow(CONFIG.INSPECT_CONV_CONFIG['FILTER_PATTERNS'])

    def heatmapWindow(self):
        if self.heatmap_path:
            img = image.load_img(self.heatmap_path)
            np_img = image.img_to_array(img)
            np_img = np.expand_dims(np_img, axis=0)
            np_img /= 255.
            CONFIG.SIMPLE_CONFIG['HEATMAP']['WINDOW_X'] = np_img.shape[2]
            CONFIG.SIMPLE_CONFIG['HEATMAP']['WINDOW_Y'] = np_img.shape[1]
            CONFIG.SIMPLE_CONFIG['HEATMAP']['SIMPLE_INFO_LABEL_POSITION'] = [0, 0, np_img.shape[2], np_img.shape[1]]
            CONFIG.SIMPLE_CONFIG['HEATMAP']['SIMPLE_INFO_LABEL_IMAGE_PATH'] = self.heatmap_path
            self.simpleWindow(CONFIG.SIMPLE_CONFIG['HEATMAP'])

    def aboutAuthorWindow(self):
        self.AboutAuthorWindow = QtWidgets.QMainWindow()
        self.about_author_window = AboutAuthorWindow()
        self.about_author_window.setup(self.AboutAuthorWindow, CONFIG.ABOUT_AUTHOR_CONFIG)
        self.AboutAuthorWindow.show()

    def aboutDatasetsWindow(self, DATASETS_CONFIG):
        self.AboutDatasetsWindow = QtWidgets.QMainWindow()
        self.about_datasets_window = AboutDatasetsWindow()
        self.about_datasets_window.setup(self.AboutDatasetsWindow, DATASETS_CONFIG)
        self.AboutDatasetsWindow.show()

    def aboutDatasetNCT_CRC_HE_100K(self):
        self.aboutDatasetsWindow(CONFIG.ABOUT_DATASETS_CONFIG['NCT_CRC_HE_100K'])

    def aboutDatasetBreakHis(self):
        self.aboutDatasetsWindow(CONFIG.ABOUT_DATASETS_CONFIG['BREAK_HIS'])

    def aboutModelsWindow(self, MODELS_CONFIG):
        self.AboutModelsWindow = QtWidgets.QMainWindow()
        self.about_models_window = AboutModelsWindow()
        self.about_models_window.setup(self.AboutModelsWindow, MODELS_CONFIG)
        self.AboutModelsWindow.show()

    def aboutModelVGG19Simple(self):
        self.aboutModelsWindow(CONFIG.ABOUT_MODELS_CONFIG['VGG19_SIMPLE'])

    def aboutModelCNNSimple(self):
        self.aboutModelsWindow(CONFIG.ABOUT_MODELS_CONFIG['CNN_SIMPLE'])

    def simpleWindow(self, SIMPLE_CONFIG):
        self.SimpleWindow = QtWidgets.QMainWindow()
        self.simple_window = SimpleWindow()
        self.simple_window.setup(self.SimpleWindow, SIMPLE_CONFIG)
        self.SimpleWindow.show()

    def generalWindow(self):
        self.simpleWindow(CONFIG.SIMPLE_CONFIG['GENERAL'])

    def howToWindow(self):
        self.simpleWindow(CONFIG.SIMPLE_CONFIG['HOWTO'])

    def exit(self):
        if os.path.exists(CONFIG.TEMPORARY_PLOTS_DIR):
            shutil.rmtree(CONFIG.TEMPORARY_PLOTS_DIR)
        sys.exit()

    def save(self):
        dir_name = QtWidgets.QFileDialog.getExistingDirectory(None, 'Save Images')
        current_time = datetime.now()
        current_time = current_time.strftime("_%d-%m-%Y_%H:%M:%S")
        shutil.copytree(CONFIG.TEMPORARY_PLOTS_DIR, os.path.join(dir_name, 'hpd' + current_time))

    def triggers(self):
        self.actionNetworkFilters.triggered.connect(self.filterPatternsWindow)
        self.actionIntermediateActivations.triggered.connect(self.layerActivationsWindow)
        self.actionHeatmap.triggered.connect(self.heatmapWindow)
        self.actionAuthor.triggered.connect(self.aboutAuthorWindow)
        self.actionNCT_CRC_HE_100K.triggered.connect(self.aboutDatasetNCT_CRC_HE_100K)
        self.actionBreakHis.triggered.connect(self.aboutDatasetBreakHis)
        self.actionVGG19Simple.triggered.connect(self.aboutModelVGG19Simple)
        self.actionCNNSimple.triggered.connect(self.aboutModelCNNSimple)
        self.actionGeneral.triggered.connect(self.generalWindow)
        self.actionHowTo.triggered.connect(self.howToWindow)
        self.actionExit.triggered.connect(self.exit)
        self.actionSave.triggered.connect(self.save)

        self.loadImageButton.clicked.connect(self.loadImageButtonEvent)
        self.classifyButton.clicked.connect(self.classifyButtonEvent)
        self.inputImageLabel.mousePressEvent = self.inputImageClickedEvent
        self.classProbabilitiesPlot.mousePressEvent = self.classProbabilitiesPlotClickedEvent

    def loadImageButtonEvent(self):
        image_path = QtWidgets.QFileDialog.getOpenFileName(None, 'Select Image', '',
                                                           "Image File Types(*.jpg *.png *.tif *.tiff)")
        self.image_path = image_path[0]
        self.inputImageLabel.setPixmap(QtGui.QPixmap(self.image_path))

    def classifyButtonEvent(self):
        if self.image_path != '':
            if self.breastTissueRadioButton.isChecked():
                dataset, model_path = 'break_his', CONFIG.MAIN_CONFIG['VGG19_SIMPLE_MODEL_PATH']
            elif self.colorectalTissueRadioButton.isChecked():
                dataset, model_path = 'nct_crc_he_100k', CONFIG.MAIN_CONFIG['CNN_SIMPLE_MODEL_PATH']
            self.model, self.image, self.image_class, self.plot_path, self.layers = predict_image(self.image_path,
                                                                                                  dataset,
                                                                                                  model_path)
            self.predictedClassLabel.setText(self._translate(CONFIG.MAIN_CONFIG['WINDOW_NAME'], self.image_class))
            self.classProbabilitiesPlot.setPixmap(QtGui.QPixmap(self.plot_path))
            self.heatmap_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                             'temporary_plots', 'heatmap.jpg')
            self.layer_activations = True
            self.filter_patterns = True
            CONFIG.INSPECT_CONV_CONFIG['LAYER_ACTIVATIONS']['COMBO_BOX_ITEMS'] = []
            CONFIG.INSPECT_CONV_CONFIG['FILTER_PATTERNS']['COMBO_BOX_ITEMS'] = []
            for layer in self.layers:
                if layer.find('conv') >= 0 or layer.find('pool') >= 0:
                    CONFIG.INSPECT_CONV_CONFIG['LAYER_ACTIVATIONS']['COMBO_BOX_ITEMS'].append(layer)
                if layer.find('conv') >= 0:
                    CONFIG.INSPECT_CONV_CONFIG['FILTER_PATTERNS']['COMBO_BOX_ITEMS'].append(layer)

    def inputImageClickedEvent(self, event):
        if self.image_path:
            self.imageClickedEvent(self.image_path)

    def classProbabilitiesPlotClickedEvent(self, event):
        if self.plot_path:
            self.imageClickedEvent(self.plot_path)

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

    def setup(self, MainWindow, MAIN_CONFIG):
        self.set_main_window(MainWindow, MAIN_CONFIG)
        self.create_central_widget(MainWindow, MAIN_CONFIG)
        self.create_menu(MainWindow, MAIN_CONFIG)
        self.add_actions()
        self.retranslate(MainWindow, MAIN_CONFIG)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.triggers()


def main():
    app = QtWidgets.QApplication(sys.argv)
    HistopathologicCancerDetection = QtWidgets.QMainWindow()
    main_window = MainWindow()
    main_window.setup(HistopathologicCancerDetection, CONFIG.MAIN_CONFIG)
    HistopathologicCancerDetection.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
