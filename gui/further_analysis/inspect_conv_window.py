import gui.config as CONFIG
import gui.gui_components as GUI
from gui.window import Window


class InspectConvWindow(Window):

    def set_inspect_conv_window(self, InspectConvWindow, INSPECT_CONV_CONFIG):
        super().set_window(InspectConvWindow, INSPECT_CONV_CONFIG)

    def create_central_widget(self, InspectConvWindow, INSPECT_CONV_CONFIG):
        self.centralwidget = GUI.get_widget(InspectConvWindow, 'centralwidget')
        self.convLayerLabel = GUI.get_label(self.centralwidget,
                                            *INSPECT_CONV_CONFIG['CONV_LAYER_LABEL_POSITION'],
                                            CONFIG.FONT,
                                            False,
                                            INSPECT_CONV_CONFIG['CONV_LAYER_LABEL_NAME'])
        self.numberLabel = GUI.get_label(self.centralwidget,
                                         *INSPECT_CONV_CONFIG['NUMBER_LABEL_POSITION'],
                                         CONFIG.FONT,
                                         False,
                                         INSPECT_CONV_CONFIG['NUMBER_LABEL_NAME'])
        self.imageLabel = GUI.get_image_label(self.centralwidget,
                                              *INSPECT_CONV_CONFIG['IMAGE_LABEL_POSITION'],
                                              CONFIG.FONT,
                                              True,
                                              INSPECT_CONV_CONFIG['IMAGE_LABEL_NAME'],
                                              INSPECT_CONV_CONFIG['IMAGE_PATH'])
        self.showButton = GUI.get_button(self.centralwidget,
                                         *INSPECT_CONV_CONFIG['BUTTON_POSITION'],
                                         CONFIG.FONT,
                                         INSPECT_CONV_CONFIG['BUTTON_NAME'])
        self.layerComboBox = GUI.get_combo_box(self.centralwidget,
                                               *INSPECT_CONV_CONFIG['COMBO_BOX_POSITION'],
                                               CONFIG.FONT,
                                               INSPECT_CONV_CONFIG['COMBO_BOX_ITEMS'],
                                               INSPECT_CONV_CONFIG['COMBO_BOX_NAME'])
        self.numberEdit = GUI.get_line_edit(self.centralwidget,
                                            *INSPECT_CONV_CONFIG['LINE_EDIT_POSITION'],
                                            CONFIG.FONT,
                                            INSPECT_CONV_CONFIG['LINE_EDIT_NAME'])
        InspectConvWindow.setCentralWidget(self.centralwidget)

    def retranslate(self, InspectConvWindow, INSPECT_CONV_CONFIG):
        super().retranslate(InspectConvWindow, INSPECT_CONV_CONFIG)
        self.convLayerLabel.setText(self._translate(INSPECT_CONV_CONFIG['WINDOW_NAME'],
                                                    INSPECT_CONV_CONFIG['CONV_LAYER_LABEL_TEXT']))
        self.numberLabel.setText(self._translate(INSPECT_CONV_CONFIG['WINDOW_NAME'],
                                                 INSPECT_CONV_CONFIG['NUMBER_LABEL_TEXT']))
        self.showButton.setText(self._translate(INSPECT_CONV_CONFIG['WINDOW_NAME'],
                                                INSPECT_CONV_CONFIG['BUTTON_TEXT']))
        for index, item in enumerate(INSPECT_CONV_CONFIG['COMBO_BOX_ITEMS']):
            self.layerComboBox.setItemText(index, self._translate(INSPECT_CONV_CONFIG['WINDOW_NAME'], item))

    def setup(self, InspectConvWindow, INSPECT_CONV_CONFIG):
        super().setup(InspectConvWindow, INSPECT_CONV_CONFIG)
