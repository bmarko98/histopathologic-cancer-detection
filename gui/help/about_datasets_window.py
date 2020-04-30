import gui.config as CONFIG
from gui.window import Window
import gui.gui_components as GUI
from PyQt5 import QtCore, QtWidgets
from gui.help.simple_window import SimpleWindow
from utils.misc import file_get_contents, load_image


class AboutDatasetsWindow(Window):

    def set_about_datasets_window(self, AboutDatasetsWindow, ABOUT_DATASETS_CONFIG):
        super().set_about_window(AboutDatasetsWindow, ABOUT_DATASETS_CONFIG)

    def create_central_widget(self, AboutDatasetsWindow, ABOUT_DATASETS_CONFIG):
        super().create_central_widget(AboutDatasetsWindow, ABOUT_DATASETS_CONFIG)
        self.dataset_overview_label = GUI.get_label(self.centralwidget,
                                                    *ABOUT_DATASETS_CONFIG['OVERVIEW_LABEL_POSITION'],
                                                    CONFIG.FONT,
                                                    False,
                                                    ABOUT_DATASETS_CONFIG['OVERVIEW_LABEL_NAME'],
                                                    QtCore.Qt.AlignLeft)
        self.dataset_images_label = GUI.get_image_label(self.centralwidget,
                                                        *ABOUT_DATASETS_CONFIG['IMAGES_LABEL_POSITIONS'],
                                                        CONFIG.FONT,
                                                        True,
                                                        ABOUT_DATASETS_CONFIG['IMAGES_LABEL_NAME'],
                                                        ABOUT_DATASETS_CONFIG['IMAGES_URL'])
        self.image_path = ABOUT_DATASETS_CONFIG['IMAGES_PATH']
        AboutDatasetsWindow.setCentralWidget(self.centralwidget)

    def retranslate(self, AboutDatasetsWindow, ABOUT_DATASETS_CONFIG):
        super().retranslate(AboutDatasetsWindow, ABOUT_DATASETS_CONFIG)
        self.dataset_overview_label.setText(self._translate(ABOUT_DATASETS_CONFIG['WINDOW_NAME'],
                                                            file_get_contents(ABOUT_DATASETS_CONFIG['DATASET_OVERVIEW_PATH'])))

    def simple_window_fun(self, SIMPLE_CONFIG):
        self.SimpleWindow = QtWidgets.QMainWindow()
        self.simple_window = SimpleWindow()
        self.simple_window.setup(self.SimpleWindow, SIMPLE_CONFIG)
        self.SimpleWindow.show()

    def dataset_image_clicked_event(self, event):
        np_img = load_image(self.image_path)
        CONFIG.SIMPLE_CONFIG['IMAGE']['WINDOW_X'] = np_img.shape[2]
        CONFIG.SIMPLE_CONFIG['IMAGE']['WINDOW_Y'] = np_img.shape[1]
        CONFIG.SIMPLE_CONFIG['IMAGE']['SIMPLE_INFO_LABEL_POSITION'] = [0, 0, np_img.shape[2], np_img.shape[1]]
        CONFIG.SIMPLE_CONFIG['IMAGE']['SIMPLE_INFO_LABEL_IMAGE_PATH'] = self.image_path
        self.simple_window_fun(CONFIG.SIMPLE_CONFIG['IMAGE'])

    def setup(self, AboutDatasetsWindow, ABOUT_DATASETS_CONFIG):
        super().setup(AboutDatasetsWindow, ABOUT_DATASETS_CONFIG)
        self.dataset_images_label.mousePressEvent = self.dataset_image_clicked_event
