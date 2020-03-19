import gui.config as CONFIG
import gui.gui_components as GUI
from gui.window import Window


class HeatmapWindow(Window):

    def set_heatmap_window(self, HeatmapWindow, HEATMAP_CONFIG):
        super().set_window(HeatmapWindow, HEATMAP_CONFIG)

    def create_central_widget(self, HeatmapWindow, HEATMAP_CONFIG):
        super().create_central_widget(HeatmapWindow, HEATMAP_CONFIG)
        self.imageTextLabel = GUI.get_label(self.centralwidget,
                                            *HEATMAP_CONFIG['IMAGE_TEXT_LABEL_POSITION'],
                                            CONFIG.FONT,
                                            False,
                                            HEATMAP_CONFIG['IMAGE_TEXT_LABEL_NAME'])
        self.heatmapTextLabel = GUI.get_label(self.centralwidget,
                                              *HEATMAP_CONFIG['HEATMAP_TEXT_LABEL_POSITION'],
                                              CONFIG.FONT,
                                              False,
                                              HEATMAP_CONFIG['HEATMAP_TEXT_LABEL_NAME'])
        self.inputImageLabel = GUI.get_image_label(self.centralwidget,
                                                   *HEATMAP_CONFIG['INPUT_IMAGE_LABEL_POSITION'],
                                                   CONFIG.FONT,
                                                   True,
                                                   HEATMAP_CONFIG['INPUT_IMAGE_LABEL_NAME'],
                                                   HEATMAP_CONFIG['INPUT_IMAGE_PATH'])
        self.heatmapImageLabel = GUI.get_image_label(self.centralwidget,
                                                     *HEATMAP_CONFIG['HEATMAP_IMAGE_LABEL_POSITION'],
                                                     CONFIG.FONT,
                                                     True,
                                                     HEATMAP_CONFIG['HEATMAP_IMAGE_LABEL_NAME'],
                                                     HEATMAP_CONFIG['HEATMAP_IMAGE_PATH'])
        HeatmapWindow.setCentralWidget(self.centralwidget)

    def retranslate(self, HeatmapWindow, HEATMAP_CONFIG):
        super().retranslate(HeatmapWindow, HEATMAP_CONFIG)
        self.imageTextLabel.setText(self._translate(HEATMAP_CONFIG['WINDOW_NAME'],
                                                    HEATMAP_CONFIG['IMAGE_TEXT_LABEL_TEXT']))
        self.heatmapTextLabel.setText(self._translate(HEATMAP_CONFIG['WINDOW_NAME'],
                                                      HEATMAP_CONFIG['HEATMAP_TEXT_LABEL_TEXT']))

    def setupUi(self, HeatmapWindow, HEATMAP_CONFIG):
        super().setup(HeatmapWindow, HEATMAP_CONFIG)
