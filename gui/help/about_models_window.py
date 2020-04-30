import gui.config as CONFIG
from PyQt5 import QtWidgets
from gui.window import Window
import gui.gui_components as GUI
from gui.help.simple_window import SimpleWindow
from utils.misc import file_get_contents, load_image


class AboutModelsWindow(Window):

    def create_central_widget(self, AboutModelsWindow, ABOUT_MODELS_CONFIG):
        super().create_central_widget(AboutModelsWindow, ABOUT_MODELS_CONFIG)
        self.model_name_label = GUI.get_label(self.centralwidget,
                                              *ABOUT_MODELS_CONFIG['MODEL_NAME_LABEL_POSITION'],
                                              CONFIG.FONT,
                                              False,
                                              ABOUT_MODELS_CONFIG['MODEL_NAME_LABEL_NAME'])
        self.model_summary_label = GUI.get_label(self.centralwidget,
                                                 *ABOUT_MODELS_CONFIG['MODEL_SUMMARY_LABEL_POSITION'],
                                                 CONFIG.FONT,
                                                 False,
                                                 ABOUT_MODELS_CONFIG['MODEL_SUMMARY_LABEL_NAME'])
        self.accuracy_label = GUI.get_image_label(self.centralwidget,
                                                  *ABOUT_MODELS_CONFIG['ACCURACY_LABEL_POSITION'],
                                                  CONFIG.FONT,
                                                  True,
                                                  ABOUT_MODELS_CONFIG['ACCURACY_LABEL_NAME'],
                                                  ABOUT_MODELS_CONFIG['ACCURACY_PATH'])
        self.loss_label = GUI.get_image_label(self.centralwidget,
                                              *ABOUT_MODELS_CONFIG['LOSS_LABEL_POSITION'],
                                              CONFIG.FONT,
                                              True,
                                              ABOUT_MODELS_CONFIG['LOSS_LABEL_NAME'],
                                              ABOUT_MODELS_CONFIG['LOSS_PATH'])
        self.conf_matrix_label = GUI.get_image_label(self.centralwidget,
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
        self.model_name_label.setText(self._translate(ABOUT_MODELS_CONFIG['WINDOW_NAME'],
                                                      ABOUT_MODELS_CONFIG['MODEL_NAME']))
        self.model_summary_label.setText(self._translate(ABOUT_MODELS_CONFIG['WINDOW_NAME'],
                                                         file_get_contents(ABOUT_MODELS_CONFIG['MODEL_SUMMARY_PATH'])))

    def simple_window_fun(self, SIMPLE_CONFIG):
        self.SimpleWindow = QtWidgets.QMainWindow()
        self.simple_window = SimpleWindow()
        self.simple_window.setup(self.SimpleWindow, SIMPLE_CONFIG)
        self.SimpleWindow.show()

    def accuracy_image_clicked_event(self, event):
        self.image_clicked_event(self.accuracy_path)

    def loss_image_clicked_event(self, event):
        self.image_clicked_event(self.loss_path)

    def conf_matrix_image_clicked_event(self, event):
        self.image_clicked_event(self.conf_matrix_path)

    def image_clicked_event(self, image_path):
        np_img = load_image(image_path)
        CONFIG.SIMPLE_CONFIG['IMAGE']['WINDOW_X'] = np_img.shape[2]
        CONFIG.SIMPLE_CONFIG['IMAGE']['WINDOW_Y'] = np_img.shape[1]
        CONFIG.SIMPLE_CONFIG['IMAGE']['SIMPLE_INFO_LABEL_POSITION'] = [0, 0, np_img.shape[2], np_img.shape[1]]
        CONFIG.SIMPLE_CONFIG['IMAGE']['SIMPLE_INFO_LABEL_IMAGE_PATH'] = image_path
        self.simple_window_fun(CONFIG.SIMPLE_CONFIG['IMAGE'])

    def setup(self, AboutModelsWindow, ABOUT_MODELS_CONFIG):
        super().setup(AboutModelsWindow, ABOUT_MODELS_CONFIG)
        self.accuracy_label.mousePressEvent = self.accuracy_image_clicked_event
        self.loss_label.mousePressEvent = self.loss_image_clicked_event
        self.conf_matrix_label.mousePressEvent = self.conf_matrix_image_clicked_event
