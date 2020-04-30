from PyQt5 import QtCore
import gui.config as CONFIG
import gui.gui_components as GUI


class Window():

    def set_window(self, Window, WINDOW_CONFIG):
        Window.setObjectName(WINDOW_CONFIG['WINDOW_NAME'])
        Window.resize(WINDOW_CONFIG['WINDOW_X'], WINDOW_CONFIG['WINDOW_Y'])
        Window.setMinimumSize(QtCore.QSize(WINDOW_CONFIG['WINDOW_X'], WINDOW_CONFIG['WINDOW_Y']))
        Window.setMaximumSize(QtCore.QSize(WINDOW_CONFIG['WINDOW_X'], WINDOW_CONFIG['WINDOW_Y']))
        Window.setFont(CONFIG.FONT)
        Window.setStyleSheet("background-color: {b};\n color: {f};".format(b=CONFIG.BACKGROUND_COLOR,
                                                                           f=CONFIG.FONT_COLOR))

    def create_central_widget(self, Window, WINDOW_CONFIG):
        self.centralwidget = GUI.get_widget(Window, CONFIG.CENTRAL_WIDGET)

    def retranslate(self, Window, WINDOW_CONFIG):
        self._translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(self._translate(WINDOW_CONFIG['WINDOW_NAME'], WINDOW_CONFIG['WINDOW_TITLE']))

    def setup(self, Window, WINDOW_CONFIG):
        self.set_window(Window, WINDOW_CONFIG)
        self.create_central_widget(Window, WINDOW_CONFIG)
        self.retranslate(Window, WINDOW_CONFIG)
        QtCore.QMetaObject.connectSlotsByName(Window)
