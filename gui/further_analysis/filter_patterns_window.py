import gui.config as CONFIG
import gui.gui_components as GUI
from PyQt5 import QtCore, QtWidgets


class Ui_FilterPatternsWindow():

    def set_filter_patterns_window(self, FilterPatternsWindow):
        FilterPatternsWindow.setObjectName("FilterPatternsWindow")
        FilterPatternsWindow.resize(1080, 720)
        FilterPatternsWindow.setMinimumSize(QtCore.QSize(1080, 720))
        FilterPatternsWindow.setMaximumSize(QtCore.QSize(1080, 720))
        FilterPatternsWindow.setFont(CONFIG.FONT)
        FilterPatternsWindow.setStyleSheet("background-color: {b};\n color: {f};".format(b=CONFIG.BACKGROUND_COLOR,
                                                                                         f=CONFIG.FONT_COLOR))


    def create_central_widget(self, FilterPatternsWindow):
        self.centralwidget = GUI.get_widget(FilterPatternsWindow, 'centralwidget')
        self.convLayerLabel = GUI.get_label(self.centralwidget,
                                            32, 50, 200, 25,
                                            CONFIG.FONT,
                                            False,
                                            'convLayerLabel')
        self.filterNumberLabel = GUI.get_label(self.centralwidget,
                                               32, 80, 150, 25,
                                               CONFIG.FONT,
                                               False,
                                               'filterNumberLabel')
        self.filterPatternLabel = GUI.get_image_label(self.centralwidget,
                                                      450, 80, 600, 600,
                                                      CONFIG.FONT,
                                                      True,
                                                      'filterPatternLabel',
                                                      CONFIG.FILTER_URL)
        self.showFilterButton = GUI.get_button(self.centralwidget,
                                               50, 115, 200, 25,
                                               CONFIG.FONT,
                                               'showFilterButton')
        self.layerComboBox = GUI.get_combo_box(self.centralwidget,
                                               225, 50, 140, 25,
                                               CONFIG.FONT,
                                               ['item1', 'item2', 'item3'],
                                               'layerComboBox')
        self.filterNumberEdit = GUI.get_line_edit(self.centralwidget,
                                                  175, 80, 50, 25,
                                                  CONFIG.FONT,
                                                  'filterNumberEdit')
        FilterPatternsWindow.setCentralWidget(self.centralwidget)


    def retranslateUi(self, FilterPatternsWindow):
        _translate = QtCore.QCoreApplication.translate
        FilterPatternsWindow.setWindowTitle(_translate("FilterPatternsWindow", "Filter Patterns"))
        self.convLayerLabel.setText(_translate("FilterPatternsWindow", "Convolutional Layer"))
        self.filterNumberLabel.setText(_translate("FilterPatternsWindow", "Filter Number"))
        self.showFilterButton.setText(_translate("FilterPatternsWindow", "Show FIlter Patterns"))
        self.layerComboBox.setItemText(0, _translate("FilterPatternsWindow", "New Item"))
        self.layerComboBox.setItemText(1, _translate("FilterPatternsWindow", "New Item"))
        self.layerComboBox.setItemText(2, _translate("FilterPatternsWindow", "New Item"))


    def setupUi(self, FilterPatternsWindow):
        self.set_filter_patterns_window(FilterPatternsWindow)
        self.create_central_widget(FilterPatternsWindow)
        self.retranslateUi(FilterPatternsWindow)
        QtCore.QMetaObject.connectSlotsByName(FilterPatternsWindow)
