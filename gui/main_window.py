import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

import shutil                                                                 # NOQA E402
import gui.config as CONFIG                                                   # NOQA E402
from gui.window import Window                                                 # NOQA E402
from datetime import datetime                                                 # NOQA E402
import gui.gui_components as GUI                                              # NOQA E402
from utils.misc import load_image                                             # NOQA E402
from PyQt5 import QtCore, QtWidgets, QtGui                                    # NOQA E402
from utils.predict_image import predict_image                                 # NOQA E402
from gui.help.simple_window import SimpleWindow                               # NOQA E402
from gui.help.about_models_window import AboutModelsWindow                    # NOQA E402
from gui.help.about_author_window import AboutAuthorWindow                    # NOQA E402
from gui.help.about_datasets_window import AboutDatasetsWindow                # NOQA E402
from gui.further_analysis.inspect_conv_window import InspectConvWindow        # NOQA E402


class MainWindow(Window):

    def set_main_window(self, MainWindow, MAIN_CONFIG):
        super().set_window(MainWindow, MAIN_CONFIG)

    def create_central_widget(self, MainWindow, MAIN_CONFIG):
        super().create_central_widget(MainWindow, MAIN_CONFIG)
        self.load_image_button = GUI.get_button(self.centralwidget,
                                                *MAIN_CONFIG['LOAD_IMAGE_BUTTON_POSITION'],
                                                CONFIG.FONT,
                                                MAIN_CONFIG['LOAD_IMAGE_BUTTON_NAME'])
        self.input_image_label = GUI.get_image_label(self.centralwidget,
                                                     *MAIN_CONFIG['INPUT_IMAGE_POSITION'],
                                                     CONFIG.FONT,
                                                     True,
                                                     MAIN_CONFIG['INPUT_IMAGE_NAME'],
                                                     None)
        self.image_path = ''
        self.breast_tissue_radio_button = GUI.get_radio_button(self.centralwidget,
                                                               *MAIN_CONFIG['BREAST_TISSUE_RADIO_BUTTON_POSITION'],
                                                               CONFIG.FONT,
                                                               MAIN_CONFIG['BREAST_TISSUE_RADIO_BUTTON_NAME'])
        self.colorectal_tissue_radio_button = GUI.get_radio_button(self.centralwidget,
                                                                   *MAIN_CONFIG['COLORECTAL_TISSUE_RADIO_BUTTON_POSITION'],
                                                                   CONFIG.FONT,
                                                                   MAIN_CONFIG['COLORECTAL_TISSUE_RADIO_BUTTON_NAME'])
        self.classify_button = GUI.get_button(self.centralwidget,
                                              *MAIN_CONFIG['CLASSIFY_BUTTON_POSITION'],
                                              CONFIG.FONT,
                                              MAIN_CONFIG['CLASSIFY_BUTTON_NAME'])
        self.predicted_class_label = GUI.get_label(self.centralwidget,
                                                   *MAIN_CONFIG['PREDICTED_CLASS_LABEL_POSITION'],
                                                   CONFIG.FONT,
                                                   False,
                                                   MAIN_CONFIG['PREDICTED_CLASS_LABEL_NAME'])
        self.class_probabilities_plot = GUI.get_image_label(self.centralwidget,
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
        self.menu_file = GUI.get_menu(self.menubar, MAIN_CONFIG['MENU']['FILE_NAME'])
        self.menu_further_analysis = GUI.get_menu(self.menubar, MAIN_CONFIG['MENU']['FURTHER_ANALYSIS_NAME'])
        self.menu_about = GUI.get_menu(self.menubar, MAIN_CONFIG['MENU']['ABOUT_NAME'])
        self.menu_application = GUI.get_menu(self.menubar, MAIN_CONFIG['MENU']['APPLICATION_NAME'])
        self.menu_datasets = GUI.get_menu(self.menubar, MAIN_CONFIG['MENU']['DATASETS_NAME'])
        self.menu_models = GUI.get_menu(self.menubar, MAIN_CONFIG['MENU']['MODELS_NAME'])

        MainWindow.setMenuBar(self.menubar)

        self.action_author = GUI.get_action(MainWindow, MAIN_CONFIG['ACTION']['AUTHOR_NAME'])
        self.action_how_to = GUI.get_action(MainWindow, MAIN_CONFIG['ACTION']['HOW_TO_NAME'])
        self.action_breakhis = GUI.get_action(MainWindow, MAIN_CONFIG['ACTION']['BREAK_HIS_NAME'])
        self.action_nctcrche100k = GUI.get_action(MainWindow, MAIN_CONFIG['ACTION']['NCT_CRC_HE_100K_NAME'])
        self.action_cnnsimple = GUI.get_action(MainWindow, MAIN_CONFIG['ACTION']['CNN_SIMPLE_NAME'])
        self.action_vgg19simple = GUI.get_action(MainWindow, MAIN_CONFIG['ACTION']['VGG19_SIMPLE_NAME'])
        self.action_network_filters = GUI.get_action(MainWindow, MAIN_CONFIG['ACTION']['MODELS_NAME'])
        self.action_intermediate_activations = GUI.get_action(MainWindow,
                                                              MAIN_CONFIG['ACTION']['INTERMEDIATE_ACTIVATIONS_NAME'])
        self.action_heatmap = GUI.get_action(MainWindow, MAIN_CONFIG['ACTION']['HEATMAP_NAME'])
        self.action_exit = GUI.get_action(MainWindow, MAIN_CONFIG['ACTION']['EXIT_NAME'])
        self.action_save = GUI.get_action(MainWindow, MAIN_CONFIG['ACTION']['SAVE_NAME'])
        self.action_general = GUI.get_action(MainWindow, MAIN_CONFIG['ACTION']['GENERAL_NAME'])

    def add_actions(self):
        self.menu_file.addAction(self.action_save)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_exit)
        self.menu_further_analysis.addAction(self.action_intermediate_activations)
        self.menu_further_analysis.addAction(self.action_heatmap)
        self.menu_further_analysis.addSeparator()
        self.menu_further_analysis.addAction(self.action_network_filters)
        self.menu_application.addAction(self.action_general)
        self.menu_application.addAction(self.action_how_to)
        self.menu_application.addSeparator()
        self.menu_application.addAction(self.action_author)
        self.menu_datasets.addAction(self.action_breakhis)
        self.menu_datasets.addAction(self.action_nctcrche100k)
        self.menu_models.addAction(self.action_cnnsimple)
        self.menu_models.addAction(self.action_vgg19simple)
        self.menu_about.addAction(self.menu_application.menuAction())
        self.menu_about.addSeparator()
        self.menu_about.addAction(self.menu_datasets.menuAction())
        self.menu_about.addAction(self.menu_models.menuAction())
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_further_analysis.menuAction())
        self.menubar.addAction(self.menu_about.menuAction())

    def retranslate(self, MainWindow, MAIN_CONFIG):
        super().retranslate(MainWindow, MAIN_CONFIG)
        self.load_image_button.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['LOAD_IMAGE_BUTTON_TEXT']))
        self.breast_tissue_radio_button.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'],
                                                                MAIN_CONFIG['BREAST_TISSUE_RADIO_BUTTON_TEXT']))
        self.colorectal_tissue_radio_button.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'],
                                                                    MAIN_CONFIG['COLORECTAL_TISSUE_RADIO_BUTTON_TEXT']))
        self.classify_button.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['CLASSIFY_BUTTON_TEXT']))
        self.menu_file.setTitle(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['MENU']['FILE_TEXT']))
        self.menu_further_analysis.setTitle(self._translate(MAIN_CONFIG['WINDOW_NAME'],
                                                            MAIN_CONFIG['MENU']['FURTHER_ANALYSIS_TEXT']))
        self.menu_about.setTitle(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['MENU']['ABOUT_TEXT']))
        self.menu_application.setTitle(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['MENU']['APPLICATION_TEXT']))
        self.menu_datasets.setTitle(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['MENU']['DATASETS_TEXT']))
        self.menu_models.setTitle(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['MENU']['MODELS_TEXT']))
        self.action_how_to.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['ACTION']['HOW_TO_TEXT']))
        self.action_author.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['ACTION']['AUTHOR_TEXT']))
        self.action_breakhis.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['ACTION']['BREAK_HIS_TEXT']))
        self.action_nctcrche100k.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'],
                                                         MAIN_CONFIG['ACTION']['NCT_CRC_HE_100K_TEXT']))
        self.action_cnnsimple.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['ACTION']['CNN_SIMPLE_TEXT']))
        self.action_vgg19simple.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'],
                                                        MAIN_CONFIG['ACTION']['VGG19_SIMPLE_TEXT']))
        self.action_network_filters.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'],
                                                            MAIN_CONFIG['ACTION']['NETWORK_FILTERS_TEXT']))
        self.action_intermediate_activations.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'],
                                                                     MAIN_CONFIG['ACTION']['INTERMEDIATE_ACTIVATIONS_TEXT']))
        self.action_heatmap.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['ACTION']['HEATMAP_TEXT']))
        self.action_exit.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['ACTION']['EXIT_TEXT']))
        self.action_save.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['ACTION']['SAVE_TEXT']))
        self.action_general.setText(self._translate(MAIN_CONFIG['WINDOW_NAME'], MAIN_CONFIG['ACTION']['GENERAL_TEXT']))

    def inspect_conv_window_fun(self, INSPECT_CONV_CONFIG):
        self.InspectConvWindow = QtWidgets.QMainWindow()
        self.inspect_conv_window = InspectConvWindow()
        self.inspect_conv_window.input_image = self.image
        self.inspect_conv_window.model = self.model
        self.inspect_conv_window.setup(self.InspectConvWindow, INSPECT_CONV_CONFIG)
        self.InspectConvWindow.show()

    def layer_activations_window_fun(self):
        if self.layer_activations:
            self.inspect_conv_window_fun(CONFIG.INSPECT_CONV_CONFIG['LAYER_ACTIVATIONS'])

    def filter_patterns_window_fun(self):
        if self.filter_patterns:
            self.inspect_conv_window_fun(CONFIG.INSPECT_CONV_CONFIG['FILTER_PATTERNS'])

    def heatmap_window_fun(self):
        if self.heatmap_path:
            np_img = load_image(self.heatmap_path)
            CONFIG.SIMPLE_CONFIG['HEATMAP']['WINDOW_X'] = np_img.shape[2]
            CONFIG.SIMPLE_CONFIG['HEATMAP']['WINDOW_Y'] = np_img.shape[1]
            CONFIG.SIMPLE_CONFIG['HEATMAP']['SIMPLE_INFO_LABEL_POSITION'] = [0, 0, np_img.shape[2], np_img.shape[1]]
            CONFIG.SIMPLE_CONFIG['HEATMAP']['SIMPLE_INFO_LABEL_IMAGE_PATH'] = self.heatmap_path
            self.simple_window_fun(CONFIG.SIMPLE_CONFIG['HEATMAP'])

    def about_author_window_fun(self):
        self.AboutAuthorWindow = QtWidgets.QMainWindow()
        self.about_author_window = AboutAuthorWindow()
        self.about_author_window.setup(self.AboutAuthorWindow, CONFIG.ABOUT_AUTHOR_CONFIG)
        self.AboutAuthorWindow.show()

    def about_datasets_window_fun(self, DATASETS_CONFIG):
        self.AboutDatasetsWindow = QtWidgets.QMainWindow()
        self.about_datasets_window = AboutDatasetsWindow()
        self.about_datasets_window.setup(self.AboutDatasetsWindow, DATASETS_CONFIG)
        self.AboutDatasetsWindow.show()

    def about_dataset_nctcrche100k_window_fun(self):
        self.about_datasets_window_fun(CONFIG.ABOUT_DATASETS_CONFIG['NCT_CRC_HE_100K'])

    def about_dataset_breakhis_window_fun(self):
        self.about_datasets_window_fun(CONFIG.ABOUT_DATASETS_CONFIG['BREAK_HIS'])

    def about_models_window_fun(self, MODELS_CONFIG):
        self.AboutModelsWindow = QtWidgets.QMainWindow()
        self.about_models_window = AboutModelsWindow()
        self.about_models_window.setup(self.AboutModelsWindow, MODELS_CONFIG)
        self.AboutModelsWindow.show()

    def about_model_vgg19simple_window_fun(self):
        self.about_models_window_fun(CONFIG.ABOUT_MODELS_CONFIG['VGG19_SIMPLE'])

    def about_model_cnnsimple_window_fun(self):
        self.about_models_window_fun(CONFIG.ABOUT_MODELS_CONFIG['CNN_SIMPLE'])

    def simple_window_fun(self, SIMPLE_CONFIG):
        self.SimpleWindow = QtWidgets.QMainWindow()
        self.simple_window = SimpleWindow()
        self.simple_window.setup(self.SimpleWindow, SIMPLE_CONFIG)
        self.SimpleWindow.show()

    def general_window_fun(self):
        self.simple_window_fun(CONFIG.SIMPLE_CONFIG['GENERAL'])

    def how_to_window_fun(self):
        self.simple_window_fun(CONFIG.SIMPLE_CONFIG['HOWTO'])

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
        self.action_network_filters.triggered.connect(self.filter_patterns_window_fun)
        self.action_intermediate_activations.triggered.connect(self.layer_activations_window_fun)
        self.action_heatmap.triggered.connect(self.heatmap_window_fun)
        self.action_author.triggered.connect(self.about_author_window_fun)
        self.action_nctcrche100k.triggered.connect(self.about_dataset_nctcrche100k_window_fun)
        self.action_breakhis.triggered.connect(self.about_dataset_breakhis_window_fun)
        self.action_vgg19simple.triggered.connect(self.about_model_vgg19simple_window_fun)
        self.action_cnnsimple.triggered.connect(self.about_model_cnnsimple_window_fun)
        self.action_general.triggered.connect(self.general_window_fun)
        self.action_how_to.triggered.connect(self.how_to_window_fun)
        self.action_exit.triggered.connect(self.exit)
        self.action_save.triggered.connect(self.save)

        self.load_image_button.clicked.connect(self.load_image_button_event)
        self.classify_button.clicked.connect(self.classify_button_event)
        self.input_image_label.mousePressEvent = self.input_image_clicked_event
        self.class_probabilities_plot.mousePressEvent = self.class_probabilities_plot_clicked_event

    def load_image_button_event(self):
        image_path = QtWidgets.QFileDialog.getOpenFileName(None, 'Select Image', '',
                                                           "Image File Types(*.jpg *.png *.tif *.tiff)")
        self.image_path = image_path[0]
        self.input_image_label.setPixmap(QtGui.QPixmap(self.image_path))

    def classify_button_event(self):
        if self.image_path != '':
            dataset=''
            if self.breast_tissue_radio_button.isChecked():
                dataset, model_path = 'break_his', CONFIG.MAIN_CONFIG['VGG19_SIMPLE_MODEL_PATH']
            elif self.colorectal_tissue_radio_button.isChecked():
                dataset, model_path = 'nct_crc_he_100k', CONFIG.MAIN_CONFIG['CNN_SIMPLE_MODEL_PATH']
            self.model, self.image, self.image_class, self.plot_path, self.layers = predict_image(self.image_path,
                                                                                                  dataset,
                                                                                                  model_path)
            self.predicted_class_label.setText(self._translate(CONFIG.MAIN_CONFIG['WINDOW_NAME'],
                                               self.image_class.replace('_', ' ').title()))
            self.class_probabilities_plot.setPixmap(QtGui.QPixmap(self.plot_path))
            self.heatmap_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'temporary_plots', 'heatmap.jpg')
            self.layer_activations = True
            self.filter_patterns = True
            CONFIG.INSPECT_CONV_CONFIG['LAYER_ACTIVATIONS']['COMBO_BOX_ITEMS'] = []
            CONFIG.INSPECT_CONV_CONFIG['FILTER_PATTERNS']['COMBO_BOX_ITEMS'] = []
            for layer in self.layers:
                if layer.find('conv') >= 0 or layer.find('pool') >= 0:
                    CONFIG.INSPECT_CONV_CONFIG['LAYER_ACTIVATIONS']['COMBO_BOX_ITEMS'].append(layer)
                if layer.find('conv') >= 0:
                    CONFIG.INSPECT_CONV_CONFIG['FILTER_PATTERNS']['COMBO_BOX_ITEMS'].append(layer)

    def input_image_clicked_event(self, event):
        if self.image_path:
            self.image_clicked_event(self.image_path)

    def class_probabilities_plot_clicked_event(self, event):
        if self.plot_path:
            self.image_clicked_event(self.plot_path)

    def image_clicked_event(self, image_path):
        np_img = load_image(image_path)
        CONFIG.SIMPLE_CONFIG['IMAGE']['WINDOW_X'] = np_img.shape[2]
        CONFIG.SIMPLE_CONFIG['IMAGE']['WINDOW_Y'] = np_img.shape[1]
        CONFIG.SIMPLE_CONFIG['IMAGE']['SIMPLE_INFO_LABEL_POSITION'] = [0, 0, np_img.shape[2], np_img.shape[1]]
        CONFIG.SIMPLE_CONFIG['IMAGE']['SIMPLE_INFO_LABEL_IMAGE_PATH'] = image_path
        self.simple_window_fun(CONFIG.SIMPLE_CONFIG['IMAGE'])

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
