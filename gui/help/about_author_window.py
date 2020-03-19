import gui.config as CONFIG
import gui.gui_components as GUI
from gui.window import Window


class AboutAuthorWindow(Window):

    def set_about_author_window(self, AboutAuthorWindow, ABOUT_AUTHOR_CONFIG):
        super().set_window(AboutAuthorWindow, ABOUT_AUTHOR_CONFIG)

    def create_central_widget(self, AboutAuthorWindow, ABOUT_AUTHOR_CONFIG):
        super().create_central_widget(AboutAuthorWindow, ABOUT_AUTHOR_CONFIG)
        self.authorImageLabel = GUI.get_image_label(self.centralwidget,
                                                    *ABOUT_AUTHOR_CONFIG['IMAGE_LABEL_POSITION'],
                                                    CONFIG.FONT,
                                                    True,
                                                    ABOUT_AUTHOR_CONFIG['IMAGE_LABEL_NAME'],
                                                    ABOUT_AUTHOR_CONFIG['AUTHOR_IMAGE_PATH'])
        self.resumeLabel = GUI.get_label(self.centralwidget,
                                         *ABOUT_AUTHOR_CONFIG['RESUME_LABEL_POSITION'],
                                         CONFIG.FONT,
                                         False,
                                         ABOUT_AUTHOR_CONFIG['RESUME_LABEL_NAME'])
        AboutAuthorWindow.setCentralWidget(self.centralwidget)

    def retranslate(self, AboutAuthorWindow, ABOUT_AUTHOR_CONFIG):
        super().retranslate(AboutAuthorWindow, ABOUT_AUTHOR_CONFIG)
        self.resumeLabel.setText(self._translate(ABOUT_AUTHOR_CONFIG['WINDOW_NAME'],
                                                 ABOUT_AUTHOR_CONFIG['RESUME']))

    def setup(self, AboutAuthorWindow, ABOUT_AUTHOR_CONFIG):
        super().setup(AboutAuthorWindow, ABOUT_AUTHOR_CONFIG)
