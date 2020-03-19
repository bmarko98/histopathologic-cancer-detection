import gui.config as CONFIG
import gui.gui_components as GUI
from gui.window import Window
from utils.misc import file_get_contents


class AboutModelsWindow(Window):

    def set_about_models_window(self, AboutModelsWindow, ABOUT_MODELS_CONFIG):
        super().set_window(AboutModelsWindow, ABOUT_MODELS_CONFIG)


    def create_central_widget(self, AboutModelsWindow, ABOUT_MODELS_CONFIG):
        super().create_central_widget(AboutModelsWindow, ABOUT_MODELS_CONFIG)
        self.modelNameLabel = GUI.get_label(self.centralwidget,
                                            *ABOUT_MODELS_CONFIG['MODEL_NAME_LABEL_POSITION'],
                                            CONFIG.FONT,
                                            False,
                                            ABOUT_MODELS_CONFIG['MODEL_NAME_LABEL_NAME'])
        self.modelSummaryLabel = GUI.get_label(self.centralwidget,
                                               *ABOUT_MODELS_CONFIG['MODEL_SUMMARY_LABEL_POSITION'],
                                               CONFIG.FONT,
                                               False,
                                               ABOUT_MODELS_CONFIG['MODEL_SUMMARY_LABEL_NAME'])
        self.accuracyLabel = GUI.get_image_label(self.centralwidget,
                                                 *ABOUT_MODELS_CONFIG['ACCURACY_LABEL_POSITION'],
                                                 CONFIG.FONT,
                                                 True,
                                                 ABOUT_MODELS_CONFIG['ACCURACY_LABEL_NAME'],
                                                 ABOUT_MODELS_CONFIG['ACCURACY_PATH'])
        self.lossLabel = GUI.get_image_label(self.centralwidget,
                                             *ABOUT_MODELS_CONFIG['LOSS_LABEL_POSITION'],
                                             CONFIG.FONT,
                                             True,
                                             ABOUT_MODELS_CONFIG['LOSS_LABEL_NAME'],
                                             ABOUT_MODELS_CONFIG['LOSS_PATH'])
        self.confMatrixLabel = GUI.get_image_label(self.centralwidget,
                                                   *ABOUT_MODELS_CONFIG['CONF_MATRIX_LABEL_POSITION'],
                                                   CONFIG.FONT,
                                                   True,
                                                   ABOUT_MODELS_CONFIG['CONF_MATRIX_LABEL_NAME'],
                                                   ABOUT_MODELS_CONFIG['CONF_MATRIX_PATH'])
        AboutModelsWindow.setCentralWidget(self.centralwidget)


    def retranslate(self, AboutModelsWindow, ABOUT_MODELS_CONFIG):
        super().retranslate(AboutModelsWindow, ABOUT_MODELS_CONFIG)
        self.modelNameLabel.setText(self._translate(ABOUT_MODELS_CONFIG['WINDOW_NAME'],
                                                    ABOUT_MODELS_CONFIG['MODEL_NAME']))
        self.modelSummaryLabel.setText(self._translate(ABOUT_MODELS_CONFIG['WINDOW_NAME'],
                                                      file_get_contents(ABOUT_MODELS_CONFIG['MODEL_SUMMARY_PATH'])))


    def setup(self, AboutModelsWindow, ABOUT_MODELS_CONFIG):
        super().setup(AboutModelsWindow, ABOUT_MODELS_CONFIG)
