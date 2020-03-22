from PyQt5 import QtCore
import gui.config as CONFIG
import gui.gui_components as GUI
from gui.window import Window


class SimpleWindow(Window):

    def set_window(self, SimpleWindow, SIMPLE_CONFIG):
        super().set_window(SimpleWindow, SIMPLE_CONFIG)
        SimpleWindow.setMinimumSize(QtCore.QSize(0, 0))
        SimpleWindow.setMaximumSize(QtCore.QSize(2000, 1000))

    def create_central_widget(self, SimpleWindow, SIMPLE_CONFIG):
        super().create_central_widget(SimpleWindow, SIMPLE_CONFIG)
        self.simpleInfoLabel = GUI.get_image_label(self.centralwidget,
                                                   *SIMPLE_CONFIG['SIMPLE_INFO_LABEL_POSITION'],
                                                   CONFIG.FONT,
                                                   True,
                                                   SIMPLE_CONFIG['SIMPLE_INFO_LABEL_NAME'],
                                                   SIMPLE_CONFIG['SIMPLE_INFO_LABEL_IMAGE_PATH'])
        SimpleWindow.setCentralWidget(self.centralwidget)

    def retranslate(self, SimpleWindow, SIMPLE_CONFIG):
        super().retranslate(SimpleWindow, SIMPLE_CONFIG)
        self.simpleInfoLabel.setText(self._translate(SIMPLE_CONFIG['WINDOW_NAME'],
                                                     SIMPLE_CONFIG['TEXT']))
