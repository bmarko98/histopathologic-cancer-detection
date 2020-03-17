import gui.config as CONFIG
import gui.gui_components as GUI
from PyQt5 import QtCore, QtWidgets


class Ui_AboutDatasetsWindow():

    def set_about_datasets_window(self, AboutDatasetsWindow):
        AboutDatasetsWindow.setObjectName("AboutDatasetsWindow")
        AboutDatasetsWindow.resize(1600, 900)
        AboutDatasetsWindow.setMinimumSize(QtCore.QSize(1600, 900))
        AboutDatasetsWindow.setMaximumSize(QtCore.QSize(1600, 900))
        AboutDatasetsWindow.setFont(CONFIG.FONT)
        AboutDatasetsWindow.setStyleSheet("background-color: {b};\n color: {f};".format(b=CONFIG.BACKGROUND_COLOR,
                                                                                        f=CONFIG.FONT_COLOR))


    def create_central_widget(self, AboutDatasetsWindow, dataset):
        self.centralwidget = GUI.get_widget(AboutDatasetsWindow, 'centralwidget')
        self.datasetOverviewLabel = GUI.get_label(self.centralwidget,
                                                  75, 5, 400, 900,
                                                  CONFIG.FONT,
                                                  False,
                                                  'datasetOverviewLabel',
                                                  QtCore.Qt.AlignLeft)
        if dataset == 'break_his':
            dataset_images_url = CONFIG.BREAK_HIS_IMAGES_URL
        elif dataset == 'nct_crc_he_100k':
            dataset_images_url = CONFIG.NCT_CRC_HE_100K_IMAGES_URL
        self.datasetImagesLabel = GUI.get_image_label(self.centralwidget,
                                                      550, 200, 950, 600,
                                                      CONFIG.FONT,
                                                      True,
                                                      'datasetImagesLabel',
                                                      dataset_images_url)
        AboutDatasetsWindow.setCentralWidget(self.centralwidget)


    def retranslateUi(self, AboutDatasetsWindow, dataset):
        _translate = QtCore.QCoreApplication.translate
        AboutDatasetsWindow.setWindowTitle(_translate("AboutDatasetsWindow", "About Datasets"))
        if dataset == 'break_his':
            self.datasetOverviewLabel.setText(_translate("AboutDatasetsWindow",
                                                         file_get_contents(CONFIG.BREAK_HIS_FILE_URL)))
        elif dataset == 'nct_crc_he_100k':
            self.datasetOverviewLabel.setText(_translate("AboutDatasetsWindow",
                                                         file_get_contents(CONFIG.NCT_CRC_HE_100K_FILE_URL)))


    def setupUi(self, AboutDatasetsWindow, dataset):
        self.set_about_datasets_window(AboutDatasetsWindow)
        self.create_central_widget(AboutDatasetsWindow, dataset)
        self.retranslateUi(AboutDatasetsWindow, dataset)
        QtCore.QMetaObject.connectSlotsByName(AboutDatasetsWindow)


def file_get_contents(filename):
    with open(filename) as f:
        s = f.read()
    return s
