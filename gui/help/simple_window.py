import gui.config as CONFIG
import gui.gui_components as GUI
from PyQt5 import QtCore, QtWidgets, QtGui


class Ui_SimpleWindow():

    def set_simple_window(self, SimpleWindow, type):
        if type == 'GeneralWindow':
            SimpleWindow.setObjectName('GeneralWindow')
            SimpleWindow.resize(640, 400)
            SimpleWindow.setMinimumSize(QtCore.QSize(640, 400))
            SimpleWindow.setMaximumSize(QtCore.QSize(640, 400))
        elif type == 'HowToWindow':
            SimpleWindow.setObjectName('HowToWindow')
            SimpleWindow.resize(1080, 720)
            SimpleWindow.setMinimumSize(QtCore.QSize(1080, 720))
            SimpleWindow.setMaximumSize(QtCore.QSize(1080, 720))

        SimpleWindow.setFont(CONFIG.FONT)
        SimpleWindow.setStyleSheet("background-color: {b};\n color: {f};".format(b=CONFIG.BACKGROUND_COLOR,
                                                                                 f=CONFIG.FONT_COLOR))


    def create_central_widget(self, SimpleWindow, type):
        if type == 'GeneralWindow':
            width, height = 540, 300
        elif type == 'HowToWindow':
            width, height = 940, 600

        self.centralwidget = GUI.get_widget(SimpleWindow, 'centralwidget')
        self.simpleInfoLabel = GUI.get_label(self.centralwidget,
                                              50, 50, width, height,
                                              CONFIG.FONT,
                                              False,
                                              'simpleInfoLabel')
        SimpleWindow.setCentralWidget(self.centralwidget)


    def retranslateUi(self, SimpleWindow, type):
        _translate = QtCore.QCoreApplication.translate
        SimpleWindow.setWindowTitle(_translate("SimpleWindow", type))
        self.simpleInfoLabel.setText(_translate("SimpleWindow", type))


    def setupUi(self, SimpleWindow, type):
        self.set_simple_window(SimpleWindow, type)
        self.create_central_widget(SimpleWindow, type)
        self.retranslateUi(SimpleWindow, type)
        QtCore.QMetaObject.connectSlotsByName(SimpleWindow)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SimpleWindow = QtWidgets.QMainWindow()
    ui = Ui_SimpleWindow()
    ui.setupUi(SimpleWindow, 'HowToWindow')
    SimpleWindow.show()
    sys.exit(app.exec_())
