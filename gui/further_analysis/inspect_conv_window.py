import os
import gui.config as CONFIG
from PyQt5 import QtWidgets
from gui.window import Window
import gui.gui_components as GUI
from utils.misc import load_image
from gui.help.simple_window import SimpleWindow
from utils.visualize_filters import create_pattern
from utils.visualize_intermediate_activations_and_heatmaps import visualize_intermediate_activations


class InspectConvWindow(Window):

    def create_central_widget(self, InspectConvWindow, INSPECT_CONV_CONFIG):
        self.centralwidget = GUI.get_widget(InspectConvWindow, 'centralwidget')
        self.conv_layer_label = GUI.get_label(self.centralwidget,
                                              *INSPECT_CONV_CONFIG['CONV_LAYER_LABEL_POSITION'],
                                              CONFIG.FONT,
                                              False,
                                              INSPECT_CONV_CONFIG['CONV_LAYER_LABEL_NAME'])
        self.number_label = GUI.get_label(self.centralwidget,
                                          *INSPECT_CONV_CONFIG['NUMBER_LABEL_POSITION'],
                                          CONFIG.FONT,
                                          False,
                                          INSPECT_CONV_CONFIG['NUMBER_LABEL_NAME'])
        self.show_button = GUI.get_button(self.centralwidget,
                                          *INSPECT_CONV_CONFIG['BUTTON_POSITION'],
                                          CONFIG.FONT,
                                          INSPECT_CONV_CONFIG['BUTTON_NAME'])
        self.layer_combo_box = GUI.get_combo_box(self.centralwidget,
                                                 *INSPECT_CONV_CONFIG['COMBO_BOX_POSITION'],
                                                 CONFIG.FONT,
                                                 INSPECT_CONV_CONFIG['COMBO_BOX_ITEMS'],
                                                 INSPECT_CONV_CONFIG['COMBO_BOX_NAME'])
        self.number_edit = GUI.get_line_edit(self.centralwidget,
                                             *INSPECT_CONV_CONFIG['LINE_EDIT_POSITION'],
                                             CONFIG.FONT,
                                             INSPECT_CONV_CONFIG['LINE_EDIT_NAME'])
        InspectConvWindow.setCentralWidget(self.centralwidget)

    def retranslate(self, InspectConvWindow, INSPECT_CONV_CONFIG):
        super().retranslate(InspectConvWindow, INSPECT_CONV_CONFIG)
        self.conv_layer_label.setText(self._translate(INSPECT_CONV_CONFIG['WINDOW_NAME'],
                                                      INSPECT_CONV_CONFIG['CONV_LAYER_LABEL_TEXT']))
        self.number_label.setText(self._translate(INSPECT_CONV_CONFIG['WINDOW_NAME'],
                                                  INSPECT_CONV_CONFIG['NUMBER_LABEL_TEXT']))
        self.show_button.setText(self._translate(INSPECT_CONV_CONFIG['WINDOW_NAME'],
                                                 INSPECT_CONV_CONFIG['BUTTON_TEXT']))
        for index, item in enumerate(INSPECT_CONV_CONFIG['COMBO_BOX_ITEMS']):
            self.layer_combo_box.setItemText(index, self._translate(INSPECT_CONV_CONFIG['WINDOW_NAME'], item))

    def show_button_event(self):
        line_edit_text = self.number_edit.text()
        combo_box_text = self.layer_combo_box.currentText()
        if line_edit_text and combo_box_text:
            if self.show_button.objectName() == 'showActivationButton':
                if line_edit_text == 'all':
                    self.image_path = visualize_intermediate_activations(self.input_image, self.model, combo_box_text, None,
                                                                         CONFIG.TEMPORARY_PLOTS_DIR)
                    if self.image_path:
                        self.label_clicked_event()
                elif line_edit_text.isdigit():
                    channel_number = int(line_edit_text)
                    self.image_path = visualize_intermediate_activations(self.input_image, self.model, combo_box_text,
                                                                         channel_number, CONFIG.TEMPORARY_PLOTS_DIR)
                    if self.image_path:
                        self.label_clicked_event()
            elif self.show_button.objectName() == 'showFilterButton':
                if line_edit_text == 'all':
                    self.image_path = os.path.join(CONFIG.TEMPORARY_PLOTS_DIR, 'filters',
                                                   combo_box_text + '_filter_patterns.png')
                    if self.image_path:
                        self.label_clicked_event()
                elif line_edit_text.isdigit():
                    filter_number = int(line_edit_text)
                    self.image_path = create_pattern(self.model, combo_box_text, filter_number, save=True)
                    if self.image_path:
                        self.label_clicked_event()

    def simple_window_fun(self, SIMPLE_CONFIG):
        self.SimpleWindow = QtWidgets.QMainWindow()
        self.simple_window = SimpleWindow()
        self.simple_window.setup(self.SimpleWindow, SIMPLE_CONFIG)
        self.SimpleWindow.show()

    def label_clicked_event(self):
        np_img = load_image(self.image_path)
        CONFIG.SIMPLE_CONFIG['IMAGE']['WINDOW_X'] = np_img.shape[2]
        CONFIG.SIMPLE_CONFIG['IMAGE']['WINDOW_Y'] = np_img.shape[1]
        CONFIG.SIMPLE_CONFIG['IMAGE']['SIMPLE_INFO_LABEL_POSITION'] = [0, 0, np_img.shape[2], np_img.shape[1]]
        CONFIG.SIMPLE_CONFIG['IMAGE']['SIMPLE_INFO_LABEL_IMAGE_PATH'] = self.image_path
        self.simple_window_fun(CONFIG.SIMPLE_CONFIG['IMAGE'])

    def setup(self, InspectConvWindow, INSPECT_CONV_CONFIG):
        super().setup(InspectConvWindow, INSPECT_CONV_CONFIG)
        self.show_button.clicked.connect(self.show_button_event)
