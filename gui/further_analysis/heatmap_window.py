import gui.config as CONFIG
import gui.gui_components as GUI
from PyQt5 import QtCore, QtWidgets


class Ui_HeatmapWindow():

    def set_heatmap_window(self, HeatmapWindow):
        HeatmapWindow.setObjectName("HeatmapWindow")
        HeatmapWindow.resize(900, 300)
        HeatmapWindow.setMinimumSize(QtCore.QSize(900, 300))
        HeatmapWindow.setMaximumSize(QtCore.QSize(900, 300))
        HeatmapWindow.setFont(CONFIG.FONT)
        HeatmapWindow.setStyleSheet("background-color: {b};\n color: {f};".format(b=CONFIG.BACKGROUND_COLOR,
                                                                                  f=CONFIG.FONT_COLOR))


    def create_central_widget(self, HeatmapWindow):
        self.centralwidget = GUI.get_widget(HeatmapWindow, 'centralwidget')
        self.imageTextLabel = GUI.get_label(self.centralwidget,
                                            165, 45, 150, 25,
                                            CONFIG.FONT,
                                            False,
                                            'imageTextLabel')
        self.heatmapTextLabel = GUI.get_label(self.centralwidget,
                                              525, 45, 300, 17,
                                              CONFIG.FONT,
                                              False,
                                              'heatmapTextLabel')
        self.inputImageLabel = GUI.get_image_label(self.centralwidget,
                                                   50, 75, 380, 200,
                                                   CONFIG.FONT,
                                                   True,
                                                   'inputImageLabel',
                                                   CONFIG.INPUT_IMAGE_URL)
        self.heatmapImageLabel = GUI.get_image_label(self.centralwidget,
                                                     480, 75, 380, 200,
                                                     CONFIG.FONT,
                                                     True,
                                                     'heatmapImageLabel',
                                                     CONFIG.HEATMAP_URL)
        HeatmapWindow.setCentralWidget(self.centralwidget)


    def setupUi(self, HeatmapWindow):
        self.set_heatmap_window(HeatmapWindow)
        self.create_central_widget(HeatmapWindow)
        self.retranslateUi(HeatmapWindow)
        QtCore.QMetaObject.connectSlotsByName(HeatmapWindow)


    def retranslateUi(self, HeatmapWindow):
        _translate = QtCore.QCoreApplication.translate
        HeatmapWindow.setWindowTitle(_translate("HeatmapWindow", "Heatmap"))
        self.imageTextLabel.setText(_translate("HeatmapWindow", "Original Image"))
        self.heatmapTextLabel.setText(_translate("HeatmapWindow", "Heatmap of Class Activation"))
