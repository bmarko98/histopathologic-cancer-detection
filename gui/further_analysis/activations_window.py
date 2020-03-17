import gui.config as CONFIG
import gui.gui_components as GUI
from PyQt5 import QtCore, QtWidgets


class Ui_ActivationsWindow():

    def set_activations_window(self, ActivationsWindow):
        ActivationsWindow.setObjectName("ActivationsWindow")
        ActivationsWindow.resize(1280, 720)
        ActivationsWindow.setMinimumSize(QtCore.QSize(1280, 720))
        ActivationsWindow.setMaximumSize(QtCore.QSize(1280, 720))
        ActivationsWindow.setFont(CONFIG.FONT)
        ActivationsWindow.setStyleSheet("background-color: {b};\n color: {f};".format(b=CONFIG.BACKGROUND_COLOR,
                                                                                      f=CONFIG.FONT_COLOR))

    def create_central_widget(self, ActivationsWindow):
        self.centralwidget = GUI.get_widget(ActivationsWindow, 'centralwidget')
        self.convLayerLabel = GUI.get_label(self.centralwidget,
                                            37, 50, 200, 25,
                                            CONFIG.FONT,
                                            False,
                                            'convLayerLabel')
        self.channelNumberLabel = GUI.get_label(self.centralwidget,
                                                50, 80, 150, 25,
                                                CONFIG.FONT,
                                                False,
                                                'channelNumberLabel')
        self.activationLabel = GUI.get_image_label(self.centralwidget,
                                                   450, 75, 600, 600,
                                                   CONFIG.FONT,
                                                   True,
                                                   'activationLabel',
                                                   CONFIG.ACTIVATION_URL)
        self.showActivationButton = GUI.get_button(self.centralwidget,
                                                   50, 115, 200, 25,
                                                   CONFIG.FONT,
                                                   'showActivationButton')
        self.layerComboBox = GUI.get_combo_box(self.centralwidget,
                                               225, 50, 140, 25,
                                               CONFIG.FONT,
                                               ['item1', 'item2', 'item3'],
                                               'layerComboBox')
        self.channelNumberEdit = GUI.get_line_edit(self.centralwidget,
                                                   200, 80, 50, 25,
                                                   CONFIG.FONT,
                                                   'channelNumberEdit')
        ActivationsWindow.setCentralWidget(self.centralwidget)


    def retranslateUi(self, ActivationsWindow):
        _translate = QtCore.QCoreApplication.translate
        ActivationsWindow.setWindowTitle(_translate("ActivationsWindow", "Activations"))
        self.convLayerLabel.setText(_translate("ActivationsWindow", "Convolutional Layer"))
        self.channelNumberLabel.setText(_translate("ActivationsWindow", "Channel Number"))
        self.showActivationButton.setText(_translate("ActivationsWindow", "Show Activation"))
        self.layerComboBox.setItemText(0, _translate("ActivationsWindow", "New Item"))
        self.layerComboBox.setItemText(1, _translate("ActivationsWindow", "New Item"))
        self.layerComboBox.setItemText(2, _translate("ActivationsWindow", "New Item"))


    def setupUi(self, ActivationsWindow):
        self.set_activations_window(ActivationsWindow)
        self.create_central_widget(ActivationsWindow)
        self.retranslateUi(ActivationsWindow)
        QtCore.QMetaObject.connectSlotsByName(ActivationsWindow)
