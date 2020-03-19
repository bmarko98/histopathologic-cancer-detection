import gui.config as CONFIG
import gui.gui_components as GUI
from gui.window import Window
from PyQt5 import QtCore
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
        AboutDatasetsWindow.setCentralWidget(self.centralwidget)


    def retranslate(self, AboutDatasetsWindow, ABOUT_DATASETS_CONFIG):
        super().retranslate(AboutDatasetsWindow, ABOUT_DATASETS_CONFIG)
        self.datasetOverviewLabel.setText(self._translate(ABOUT_DATASETS_CONFIG['WINDOW_NAME'],
                                                          file_get_contents(ABOUT_DATASETS_CONFIG['DATASET_OVERVIEW_PATH'])))


    def setup(self, AboutDatasetsWindow, ABOUT_DATASETS_CONFIG):
        super().setup(AboutDatasetsWindow, ABOUT_DATASETS_CONFIG)
