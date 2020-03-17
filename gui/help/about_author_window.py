import gui.config as CONFIG
import gui.gui_components as GUI
from PyQt5 import QtCore, QtWidgets


class Ui_AboutAuthorWindow():

    def set_about_author_window(self, AboutAuthorWindow):
        AboutAuthorWindow.setObjectName("AboutAuthorWindow")
        AboutAuthorWindow.resize(640, 400)
        AboutAuthorWindow.setMinimumSize(QtCore.QSize(640, 400))
        AboutAuthorWindow.setMaximumSize(QtCore.QSize(640, 400))
        AboutAuthorWindow.setFont(CONFIG.FONT)
        AboutAuthorWindow.setStyleSheet("background-color: {b};\n color: {f};".format(b=CONFIG.BACKGROUND_COLOR,
                                                                                      f=CONFIG.FONT_COLOR))


    def create_central_widget(self, AboutAuthorWindow):
        self.centralwidget = GUI.get_widget(AboutAuthorWindow, 'centralwidget')
        self.authorImageLabel = GUI.get_image_label(self.centralwidget,
                                                    50, 75, 100, 150,
                                                    CONFIG.FONT,
                                                    True,
                                                    'authorImageLabel',
                                                    CONFIG.AUTHOR_IMAGE_URL)
        self.resumeLabel = GUI.get_label(self.centralwidget,
                                         250, 75, 250, 250,
                                         CONFIG.FONT,
                                         False,
                                         'resumeLabel')
        AboutAuthorWindow.setCentralWidget(self.centralwidget)


    def setupUi(self, AboutAuthorWindow):
        self.set_about_author_window(AboutAuthorWindow)
        self.create_central_widget(AboutAuthorWindow)
        self.retranslateUi(AboutAuthorWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutAuthorWindow)


    def retranslateUi(self, AboutAuthorWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutAuthorWindow.setWindowTitle(_translate("AboutAuthorWindow", "About - Author"))
        self.resumeLabel.setText(_translate("AboutAuthorWindow", "Short Resume"))
