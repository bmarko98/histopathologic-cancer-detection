import gui.config as CONFIG
from gui.window import Window
import gui.gui_components as GUI


class SimpleWindow(Window):

    def set_window(self, SimpleWindow, SIMPLE_CONFIG):
        if not GUI.check_screen_size(SIMPLE_CONFIG['WINDOW_X'], SIMPLE_CONFIG['WINDOW_Y']):
            SIMPLE_CONFIG['WINDOW_X'], SIMPLE_CONFIG['WINDOW_Y'] = GUI.resize(SIMPLE_CONFIG['WINDOW_X'],
                                                                              SIMPLE_CONFIG['WINDOW_Y'])
        super().set_window(SimpleWindow, SIMPLE_CONFIG)

    def create_central_widget(self, SimpleWindow, SIMPLE_CONFIG):
        super().create_central_widget(SimpleWindow, SIMPLE_CONFIG)
        self.simple_info_label = GUI.get_image_label(self.centralwidget,
                                                     *SIMPLE_CONFIG['SIMPLE_INFO_LABEL_POSITION'],
                                                     CONFIG.FONT,
                                                     True,
                                                     SIMPLE_CONFIG['SIMPLE_INFO_LABEL_NAME'],
                                                     SIMPLE_CONFIG['SIMPLE_INFO_LABEL_IMAGE_PATH'])
        SimpleWindow.setCentralWidget(self.centralwidget)

    def retranslate(self, SimpleWindow, SIMPLE_CONFIG):
        super().retranslate(SimpleWindow, SIMPLE_CONFIG)
        self.simple_info_label.setText(self._translate(SIMPLE_CONFIG['WINDOW_NAME'],
                                                       SIMPLE_CONFIG['TEXT']))
