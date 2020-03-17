import sys
import gui.config as CONFIG
import gui.gui_components as GUI
from PyQt5 import QtCore, QtWidgets
from gui.help.simple_window import Ui_SimpleWindow
from gui.help.about_models_window import Ui_AboutModelsWindow
from gui.help.about_author_window import Ui_AboutAuthorWindow
from gui.help.about_datasets_window import Ui_AboutDatasetsWindow
from gui.further_analysis.heatmap_window import Ui_HeatmapWindow
from gui.further_analysis.activations_window import Ui_ActivationsWindow
from gui.further_analysis.filter_patterns_window import Ui_FilterPatternsWindow


class Ui_MainWindow():

    def set_main_window(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 800))
        MainWindow.setFont(CONFIG.FONT)
        MainWindow.setStyleSheet("background-color: {b};\n color: {f};".format(b=CONFIG.BACKGROUND_COLOR,
                                                                               f=CONFIG.FONT_COLOR))


    def create_central_widget(self, MainWindow):
        self.centralwidget = GUI.get_widget(MainWindow, 'centralwidget')
        self.loadImageButton = GUI.get_button(self.centralwidget,
                                              150, 100, 150, 50,
                                              CONFIG.FONT,
                                              'loadImageButton')
        self.inputImageLabel = GUI.get_image_label(self.centralwidget,
                                                   50, 200, 350, 350,
                                                   CONFIG.FONT,
                                                   True,
                                                   'inputImageLabel',
                                                   CONFIG.INPUT_IMAGE_URL)
        self.breastTissueRadioButton = GUI.get_radio_button(self.centralwidget,
                                                            570, 420, 150, 25,
                                                            CONFIG.FONT,
                                                            'breastTissueRadioButton')
        self.colorectalTissueRadioButton = GUI.get_radio_button(self.centralwidget,
                                                                570, 450, 175, 25,
                                                                CONFIG.FONT,
                                                                'colorectalTissueRadioButton')
        self.classifyButton = GUI.get_button(self.centralwidget,
                                             565, 510, 150, 50,
                                             CONFIG.FONT,
                                             'classifyButton')
        self.predictedClassLabel = GUI.get_label(self.centralwidget,
                                                 955, 135, 200, 50,
                                                 CONFIG.FONT,
                                                 False,
                                                 'predictedClassLabel')
        self.classificationProgressBar = GUI.get_progress_bar(self.centralwidget,
                                                              540, 610, 200, 25,
                                                              'classificationProgressBar')
        self.classProbabilitiesPlot = GUI.get_image_label(self.centralwidget,
                                                          850, 200, 400, 400,
                                                          CONFIG.FONT,
                                                          True,
                                                          'classProbabilitiesPlot',
                                                          CONFIG.PROB_URL)
        MainWindow.setCentralWidget(self.centralwidget)


    def create_menu(self, MainWindow):
        self.menubar = GUI.get_menu_bar(MainWindow,
                                        0, 0, 1280, 24,
                                        CONFIG.FONT,
                                        'menubar')
        self.menuFile = GUI.get_menu(self.menubar, 'menuFile')
        self.menuFurther_Analysis = GUI.get_menu(self.menubar, 'menuFurther_Analysis')
        self.menuAbout = GUI.get_menu(self.menubar, 'menuAbout')
        self.menuApplication = GUI.get_menu(self.menubar, 'menuApplication')
        self.menuDatasets = GUI.get_menu(self.menubar, 'menuDatasets')
        self.menuModels = GUI.get_menu(self.menubar, 'menuModels')

        MainWindow.setMenuBar(self.menubar)

        self.actionModels = GUI.get_action(MainWindow, 'actionModels')
        self.actionAuthor = GUI.get_action(MainWindow, 'actionAuthor')
        self.actionHow_To = GUI.get_action(MainWindow, 'actionHow_To')
        self.actionBreakHis = GUI.get_action(MainWindow, 'actionBreakHis')
        self.actionNCT_CRC_HE_100K = GUI.get_action(MainWindow, 'actionNCT_CRC_HE_100K')
        self.actionCNNSimple = GUI.get_action(MainWindow, 'actionCNNSimple')
        self.actionVGG19Simple = GUI.get_action(MainWindow, 'actionVGG19Simple')
        self.actionNetwork_Filters = GUI.get_action(MainWindow, 'actionNetwork_Filters')
        self.actionIntermediate_Activations = GUI.get_action(MainWindow, 'actionIntermediate_Activations')
        self.actionHeatmaps = GUI.get_action(MainWindow, 'actionHeatmaps')
        self.actionExit = GUI.get_action(MainWindow, 'actionExit')
        self.actionGeneral = GUI.get_action(MainWindow, 'actionGeneral')


    def add_actions(self):
        self.menuFile.addAction(self.actionExit)
        self.menuFurther_Analysis.addAction(self.actionIntermediate_Activations)
        self.menuFurther_Analysis.addAction(self.actionHeatmaps)
        self.menuFurther_Analysis.addSeparator()
        self.menuFurther_Analysis.addAction(self.actionNetwork_Filters)
        self.menuApplication.addAction(self.actionGeneral)
        self.menuApplication.addAction(self.actionHow_To)
        self.menuApplication.addSeparator()
        self.menuApplication.addAction(self.actionAuthor)
        self.menuDatasets.addAction(self.actionBreakHis)
        self.menuDatasets.addAction(self.actionNCT_CRC_HE_100K)
        self.menuModels.addAction(self.actionCNNSimple)
        self.menuModels.addAction(self.actionVGG19Simple)
        self.menuAbout.addAction(self.menuApplication.menuAction())
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.menuDatasets.menuAction())
        self.menuAbout.addAction(self.menuModels.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuFurther_Analysis.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Histopathologic Cancer Detection"))
        self.loadImageButton.setText(_translate("MainWindow", "Load Image"))
        self.breastTissueRadioButton.setText(_translate("MainWindow", "Breast Tissue"))
        self.colorectalTissueRadioButton.setText(_translate("MainWindow", "Colorectal Tissue"))
        self.classifyButton.setText(_translate("MainWindow", "Classify"))
        self.predictedClassLabel.setText(_translate("MainWindow", "Class"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuFurther_Analysis.setTitle(_translate("MainWindow", "Further Analysis"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuApplication.setTitle(_translate("MainWindow", "Application"))
        self.menuDatasets.setTitle(_translate("MainWindow", "Datasets"))
        self.menuModels.setTitle(_translate("MainWindow", "Models"))
        self.actionModels.setText(_translate("MainWindow", "Models"))
        self.actionHow_To.setText(_translate("MainWindow", "How To"))
        self.actionAuthor.setText(_translate("MainWindow", "Author"))
        self.actionBreakHis.setText(_translate("MainWindow", "BreakHis"))
        self.actionNCT_CRC_HE_100K.setText(_translate("MainWindow", "NCT_CRC_HE_100K"))
        self.actionCNNSimple.setText(_translate("MainWindow", "CNNSimple"))
        self.actionVGG19Simple.setText(_translate("MainWindow", "VGG19Simple"))
        self.actionNetwork_Filters.setText(_translate("MainWindow", "Network Filters"))
        self.actionIntermediate_Activations.setText(_translate("MainWindow", "Intermediate Activations"))
        self.actionHeatmaps.setText(_translate("MainWindow", "Heatmaps"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionGeneral.setText(_translate("MainWindow", "General"))


    def filtersPatternsWindow(self):
        self.FilterPatternsWindow = QtWidgets.QMainWindow()
        ui = Ui_FilterPatternsWindow()
        ui.setupUi(self.FilterPatternsWindow)
        self.FilterPatternsWindow.show()


    def activationsWindow(self):
        self.ActivationsWindow = QtWidgets.QMainWindow()
        ui = Ui_ActivationsWindow()
        ui.setupUi(self.ActivationsWindow)
        self.ActivationsWindow.show()


    def heatmapWindow(self):
        self.HeatmapWindow = QtWidgets.QMainWindow()
        ui = Ui_HeatmapWindow()
        ui.setupUi(self.HeatmapWindow)
        self.HeatmapWindow.show()


    def aboutAuthorWindow(self):
        self.AboutAuthorWindow = QtWidgets.QMainWindow()
        ui = Ui_AboutAuthorWindow()
        ui.setupUi(self.AboutAuthorWindow)
        self.AboutAuthorWindow.show()


    def aboutDatasetsWindow(self, dataset):
        self.AboutDatasetsWindow = QtWidgets.QMainWindow()
        ui = Ui_AboutDatasetsWindow()
        ui.setupUi(self.AboutDatasetsWindow, dataset)
        self.AboutDatasetsWindow.show()
    def aboutDatasetNCT_CRC_HE_100K(self):
        self.aboutDatasetsWindow('nct_crc_he_100k')
    def aboutDatasetBreakHis(self):
        self.aboutDatasetsWindow('break_his')


    def aboutModelsWindow(self, model):
        self.AboutModelsWindow = QtWidgets.QMainWindow()
        ui = Ui_AboutModelsWindow()
        ui.setupUi(self.AboutModelsWindow, model)
        self.AboutModelsWindow.show()
    def aboutModelVGG19Simple(self):
        self.aboutModelsWindow('vgg19_simple')
    def aboutModelCNNSimple(self):
        self.aboutModelsWindow('cnn_simple')


    def simpleWindow(self, type):
        self.SimpleWindow = QtWidgets.QMainWindow()
        ui = Ui_SimpleWindow()
        ui.setupUi(self.SimpleWindow, type)
        self.SimpleWindow.show()
    def generalWindow(self):
        self.simpleWindow('GeneralWindow')
    def howToWindow(self):
        self.simpleWindow('HowToWindow')


    def triggers(self):
        self.actionNetwork_Filters.triggered.connect(self.filtersPatternsWindow)
        self.actionIntermediate_Activations.triggered.connect(self.activationsWindow)
        self.actionHeatmaps.triggered.connect(self.heatmapWindow)
        self.actionAuthor.triggered.connect(self.aboutAuthorWindow)
        self.actionNCT_CRC_HE_100K.triggered.connect(self.aboutDatasetNCT_CRC_HE_100K)
        self.actionBreakHis.triggered.connect(self.aboutDatasetBreakHis)
        self.actionVGG19Simple.triggered.connect(self.aboutModelVGG19Simple)
        self.actionCNNSimple.triggered.connect(self.aboutModelCNNSimple)
        self.actionGeneral.triggered.connect(self.generalWindow)
        self.actionHow_To.triggered.connect(self.howToWindow)
        self.actionExit.triggered.connect(sys.exit)


    def setupUi(self, MainWindow):
        self.set_main_window(MainWindow)
        self.create_central_widget(MainWindow)
        self.create_menu(MainWindow)
        self.add_actions()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.triggers()


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
