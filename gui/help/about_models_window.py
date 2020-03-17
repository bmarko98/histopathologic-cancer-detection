import gui.config as CONFIG
import gui.gui_components as GUI
from PyQt5 import QtCore, QtWidgets, QtGui


class Ui_AboutModelsWindow():

    def set_about_models_window(self, AboutModelsWindow):
        AboutModelsWindow.setObjectName("AboutModelsWindow")
        AboutModelsWindow.resize(1800, 900)
        AboutModelsWindow.setMinimumSize(QtCore.QSize(1800, 900))
        AboutModelsWindow.setMaximumSize(QtCore.QSize(1800, 900))
        AboutModelsWindow.setFont(CONFIG.FONT)
        AboutModelsWindow.setStyleSheet("background-color: {b};\n color: {f};".format(b=CONFIG.BACKGROUND_COLOR,
                                                                                      f=CONFIG.FONT_COLOR))


    def create_central_widget(self, AboutModelsWindow, model):
        self.centralwidget = GUI.get_widget(AboutModelsWindow, 'centralwidget')

        if model == 'vgg19_simple':
            accuracy_plot = CONFIG.VGG19_ACCURACY_PLOT_URL
            loss_plot = CONFIG.VGG19_LOSS_PLOT_URL
            confusion_matrix = CONFIG.VGG19_CONFUSION_MATRIX_URL
        elif model == 'cnn_simple':
            accuracy_plot = CONFIG.CNN_ACCURACY_PLOT_URL
            loss_plot = CONFIG.CNN_LOSS_PLOT_URL
            confusion_matrix = CONFIG.CNN_CONFUSION_MATRIX_URL

        self.modelNameLabel = GUI.get_label(self.centralwidget,
                                            110, 10, 300, 25,
                                            CONFIG.FONT,
                                            False,
                                            'modelNameLabel')
        self.modelSummaryLabel = GUI.get_label(self.centralwidget,
                                               25, 35, 500, 850,
                                               CONFIG.FONT,
                                               False,
                                               'modelSummaryLabel')
        self.accuracyLabel = GUI.get_image_label(self.centralwidget,
                                                 550, 50, 400, 400,
                                                 CONFIG.FONT,
                                                 True,
                                                 'accuracyLabel',
                                                 accuracy_plot)
        self.lossLabel = GUI.get_image_label(self.centralwidget,
                                             550, 450, 400, 400,
                                             CONFIG.FONT,
                                             True,
                                             'lossLabel',
                                             loss_plot)
        self.confMatrixLabel = GUI.get_image_label(self.centralwidget,
                                                   950, 50, 800, 800,
                                                   CONFIG.FONT,
                                                   True,
                                                   'confMatrixLabel',
                                                   confusion_matrix)
        AboutModelsWindow.setCentralWidget(self.centralwidget)


    def retranslateUi(self, AboutModelsWindow, model):
        _translate = QtCore.QCoreApplication.translate
        AboutModelsWindow.setWindowTitle(_translate("AboutModelsWindow", "About Model"))
        if model == 'vgg19_simple':
            self.modelNameLabel.setText(_translate("AboutModelsWindow", "VGG19Simple"))
            self.modelSummaryLabel.setText(_translate("AboutModelsWindow",
                                                      file_get_contents(CONFIG.VGG19_FILE_URL)))
        elif model == 'cnn_simple':
            self.modelNameLabel.setText(_translate("AboutModelsWindow", "CNNSimple"))
            self.modelSummaryLabel.setText(_translate("AboutModelsWindow",
                                                      file_get_contents(CONFIG.CNN_FILE_URL)))


    def setupUi(self, AboutModelsWindow, model):
        self.set_about_models_window(AboutModelsWindow)
        self.create_central_widget(AboutModelsWindow, model)
        self.retranslateUi(AboutModelsWindow, model)
        QtCore.QMetaObject.connectSlotsByName(AboutModelsWindow)


def file_get_contents(filename):
    with open(filename) as f:
        s = f.read()
    return s
