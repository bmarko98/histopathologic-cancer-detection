import os
import gui.gui_components as GUI

FONT = GUI.get_font('Sans Serif', 12)
BACKGROUND_COLOR = 'rgb(42, 49, 56)'
FONT_COLOR = 'white'
CENTRAL_WIDGET = 'central_widget'
TEMPORARY_PLOTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'temporary_plots')

ABOUT_AUTHOR_CONFIG = {
    'WINDOW_NAME': 'AboutAuthorWindow',
    'WINDOW_TITLE': 'About Author',
    'WINDOW_X': 640,
    'WINDOW_Y': 400,
    'IMAGE_LABEL_POSITION': [50, 75, 100, 150],
    'IMAGE_LABEL_NAME': 'authorImageLabel',
    'AUTHOR_IMAGE_PATH': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'author.jpg'),
    'RESUME_LABEL_POSITION': [250, 75, 250, 250],
    'RESUME_LABEL_NAME': 'resumeLabel',
    'RESUME': 'Write decent CV...'
}

ABOUT_DATASETS_CONFIG = {
    'BREAK_HIS': {
        'WINDOW_NAME': 'AboutDatasetsWindow',
        'WINDOW_TITLE': 'About BreakHis Dataset',
        'WINDOW_X': 1600,
        'WINDOW_Y': 900,
        'OVERVIEW_LABEL_POSITION': [75, 5, 400, 900],
        'OVERVIEW_LABEL_NAME': 'datasetOverviewLabel',
        'IMAGES_LABEL_POSITIONS': [550, 200, 950, 600],
        'IMAGES_LABEL_NAME': 'datasetImagesLabel',
        'IMAGES_URL': '/home/lenovo/Documents/bachelors_thesis/histopathologic-cancer-detection/' +
                      'data/break_his/break_his_sample_images.jpg',
        'DATASET_OVERVIEW_PATH': '/home/lenovo/Documents/bachelors_thesis/histopathologic-cancer-detection/' +
                                 'data/break_his/break_his_dataset_overview.txt'
        },
    'NCT_CRC_HE_100K': {
        'WINDOW_NAME': 'AboutDatasetsWindow',
        'WINDOW_TITLE': 'About NCT_CRC_HE_100K Dataset',
        'WINDOW_X': 1600,
        'WINDOW_Y': 900,
        'OVERVIEW_LABEL_POSITION': [75, 5, 400, 900],
        'OVERVIEW_LABEL_NAME': 'datasetOverviewLabel',
        'IMAGES_LABEL_POSITIONS': [550, 200, 950, 600],
        'IMAGES_LABEL_NAME': 'datasetImagesLabel',
        'IMAGES_URL': '/home/lenovo/Documents/bachelors_thesis/histopathologic-cancer-detection/data/' +
                      'nct_crc_he_100k/nct_crc_he_100k_sample_images.jpg',
        'DATASET_OVERVIEW_PATH': '/home/lenovo/Documents/bachelors_thesis/histopathologic-cancer-detection/' +
                                 'data/nct_crc_he_100k/nct_crc_he_100k_dataset_overview.txt'
        }
}

ABOUT_MODELS_CONFIG = {
    'VGG19_SIMPLE': {
        'WINDOW_NAME': 'AboutModelsWindow',
        'WINDOW_TITLE': 'About VGG19Simple Model',
        'WINDOW_X': 1800,
        'WINDOW_Y': 900,
        'MODEL_NAME': 'VGG19Simple',
        'MODEL_NAME_LABEL_POSITION': [110, 10, 300, 25],
        'MODEL_NAME_LABEL_NAME': 'modelNameLabel',
        'MODEL_SUMMARY_LABEL_POSITION': [25, 35, 500, 850],
        'MODEL_SUMMARY_LABEL_NAME': 'modelSummaryLabel',
        'ACCURACY_LABEL_POSITION': [550, 50, 400, 400],
        'ACCURACY_LABEL_NAME': 'accuracyLabel',
        'ACCURACY_PATH': '/home/lenovo//Documents/bachelors_thesis/histopathologic-cancer-detection/' +
                         'experiments/break_his_models/VGG19Test_16-03-2020_16:36:34/plots/accuracy_plot.png',
        'LOSS_LABEL_POSITION': [550, 450, 400, 400],
        'LOSS_LABEL_NAME': 'lossLabel',
        'LOSS_PATH': '/home/lenovo//Documents/bachelors_thesis/histopathologic-cancer-detection/' +
                     'experiments/break_his_models/VGG19Test_16-03-2020_16:36:34/plots/loss_plot.png',
        'CONF_MATRIX_LABEL_POSITION': [950, 50, 800, 800],
        'CONF_MATRIX_LABEL_NAME': 'confMatrixLabel',
        'CONF_MATRIX_PATH': '/home/lenovo//Documents/bachelors_thesis/histopathologic-cancer-detection/' +
                            'experiments/break_his_models/VGG19Test_16-03-2020_16:36:34/plots/confusion_matrix.png',
        'MODEL_SUMMARY_PATH': '/home/lenovo/Downloads/vgg19_summary.txt',
    },
    'CNN_SIMPLE': {
        'WINDOW_NAME': 'AboutModelsWindow',
        'WINDOW_TITLE': 'About CNNSimple Model',
        'WINDOW_X': 1800,
        'WINDOW_Y': 900,
        'MODEL_NAME': 'CNNSimple',
        'MODEL_NAME_LABEL_POSITION': [25, 35, 500, 850],
        'MODEL_NAME_LABEL_NAME': 'modelSummaryLabel',
        'MODEL_SUMMARY_LABEL_POSITION': [25, 35, 500, 850],
        'MODEL_SUMMARY_LABEL_NAME': 'modelSummaryLabel',
        'ACCURACY_LABEL_POSITION': [550, 50, 400, 400],
        'ACCURACY_LABEL_NAME': 'accuracyLabel',
        'ACCURACY_PATH': '/home/lenovo/Documents/bachelors_thesis/histopathologic-cancer-detection/experiments/' +
                         'nct_crc_he_100k_models/CNNSimpleTest_12-03-2020_15:49:03/plots/accuracy_plot.png',
        'LOSS_LABEL_POSITION': [550, 450, 400, 400],
        'LOSS_LABEL_NAME': 'lossLabel',
        'LOSS_PATH': '/home/lenovo/Documents/bachelors_thesis/histopathologic-cancer-detection/experiments/' +
                     'nct_crc_he_100k_models/CNNSimpleTest_12-03-2020_15:49:03/plots/loss_plot.png',
        'CONF_MATRIX_LABEL_POSITION': [950, 50, 800, 800],
        'CONF_MATRIX_LABEL_NAME': 'confMatrixLabel',
        'CONF_MATRIX_PATH': '/home/lenovo/Documents/bachelors_thesis/histopathologic-cancer-detection/experiments/' +
                            'nct_crc_he_100k_models/CNNSimpleTest_12-03-2020_15:49:03/plots/confusion_matrix.png',
        'MODEL_SUMMARY_PATH': '/home/lenovo/Downloads/cnn_summary.txt',
    }
}

SIMPLE_CONFIG = {
    'GENERAL': {
        'WINDOW_NAME': 'SimpleWindow',
        'WINDOW_TITLE': 'General',
        'WINDOW_X': 640,
        'WINDOW_Y': 400,
        'TEXT': 'Basic usability of the App...',
        'SIMPLE_INFO_LABEL_POSITION': [50, 50, 540, 300],
        'SIMPLE_INFO_LABEL_NAME': 'simpleInfoLabel',
        'SIMPLE_INFO_LABEL_IMAGE_PATH': None
    },
    'HOWTO': {
        'WINDOW_NAME': 'AboutModelsWindow',
        'WINDOW_TITLE': 'How To',
        'WINDOW_X': 1080,
        'WINDOW_Y': 720,
        'TEXT': 'Advanced usability of the App...',
        'SIMPLE_INFO_LABEL_POSITION': [50, 50, 940, 600],
        'SIMPLE_INFO_LABEL_NAME': 'simpleInfoLabel',
        'SIMPLE_INFO_LABEL_IMAGE_PATH': None
    },
    'IMAGE': {
        'WINDOW_NAME': 'ImageWindow',
        'WINDOW_TITLE': 'Image',
        'WINDOW_X': None,
        'WINDOW_Y': None,
        'TEXT': '',
        'SIMPLE_INFO_LABEL_POSITION': None,
        'SIMPLE_INFO_LABEL_NAME': 'simpleInfoLabel',
        'SIMPLE_INFO_LABEL_IMAGE_PATH': None
    }
}

HEATMAP_CONFIG = {
    'WINDOW_NAME': 'HeatmapWindow',
    'WINDOW_TITLE': 'Heatmap',
    'WINDOW_X': 900,
    'WINDOW_Y': 300,
    'IMAGE_TEXT_LABEL_POSITION': [165, 45, 150, 25],
    'IMAGE_TEXT_LABEL_NAME': 'imageTextLabel',
    'IMAGE_TEXT_LABEL_TEXT': 'Original Image',
    'HEATMAP_TEXT_LABEL_POSITION': [525, 45, 300, 17],
    'HEATMAP_TEXT_LABEL_NAME': 'heatmapTextLabel',
    'HEATMAP_TEXT_LABEL_TEXT': 'Heatmap of Class Activation',
    'INPUT_IMAGE_LABEL_POSITION': [50, 75, 380, 200],
    'INPUT_IMAGE_LABEL_NAME': 'inputImageLabel',
    'INPUT_IMAGE_PATH': None,
    'HEATMAP_IMAGE_LABEL_POSITION': [480, 75, 380, 200],
    'HEATMAP_IMAGE_LABEL_NAME': 'heatmapImageLabel',
    'HEATMAP_IMAGE_PATH': None,
}

INSPECT_CONV_CONFIG = {
    'FILTER_PATTERNS': {
        'WINDOW_NAME': 'InspectConvWindow',
        'WINDOW_TITLE': 'Filter Patterns',
        'WINDOW_X': 1080,
        'WINDOW_Y': 720,
        'CONV_LAYER_LABEL_POSITION': [32, 50, 200, 25],
        'CONV_LAYER_LABEL_NAME': 'convLayerLabel',
        'CONV_LAYER_LABEL_TEXT': 'Convolutional Layer',
        'NUMBER_LABEL_POSITION': [50, 80, 150, 25],
        'NUMBER_LABEL_NAME': 'filterNumberLabel',
        'NUMBER_LABEL_TEXT': 'Filter Number',
        'IMAGE_LABEL_POSITION': [450, 80, 600, 600],
        'IMAGE_LABEL_NAME': 'filterPatternLabel',
        'IMAGE_PATH': '/home/lenovo/Pictures/filter.jpg',
        'BUTTON_POSITION': [50, 115, 200, 25],
        'BUTTON_NAME': 'showFilterButton',
        'BUTTON_TEXT': 'Show Filter Patterns',
        'COMBO_BOX_POSITION': [225, 50, 140, 25],
        'COMBO_BOX_NAME': 'layerComboBox',
        'COMBO_BOX_ITEMS': ['item1', 'item2', 'item3'],
        'LINE_EDIT_POSITION': [175, 80, 50, 25],
        'LINE_EDIT_NAME': 'filterNumberEdit'
    },
    'LAYER_ACTIVATIONS': {
        'WINDOW_NAME': 'InspectConvWindow',
        'WINDOW_TITLE': 'Layer Activations',
        'WINDOW_X': 1080,
        'WINDOW_Y': 720,
        'CONV_LAYER_LABEL_POSITION': [32, 50, 200, 25],
        'CONV_LAYER_LABEL_NAME': 'convLayerLabel',
        'CONV_LAYER_LABEL_TEXT': 'Layer',
        'NUMBER_LABEL_POSITION': [50, 80, 150, 25],
        'NUMBER_LABEL_NAME': 'channelNumberLabel',
        'NUMBER_LABEL_TEXT': 'Channel Number',
        'IMAGE_LABEL_POSITION': [450, 75, 600, 600],
        'IMAGE_LABEL_NAME': 'activationLabel',
        'BUTTON_POSITION': [50, 115, 200, 25],
        'BUTTON_NAME': 'showActivationButton',
        'BUTTON_TEXT': 'Show Layer Activations',
        'COMBO_BOX_POSITION': [225, 50, 140, 25],
        'COMBO_BOX_NAME': 'layerComboBox',
        'COMBO_BOX_ITEMS': [],
        'LINE_EDIT_POSITION': [175, 80, 50, 25],
        'LINE_EDIT_NAME': 'channelNumberEdit'
    }
}

MAIN_CONFIG = {
    'WINDOW_NAME': 'MainWindow',
    'WINDOW_TITLE': 'Histopathologic Cancer Detection',
    'WINDOW_X': 1280,
    'WINDOW_Y': 800,
    'LOAD_IMAGE_BUTTON_POSITION': [150, 100, 150, 50],
    'LOAD_IMAGE_BUTTON_NAME': 'loadImageButton',
    'LOAD_IMAGE_BUTTON_TEXT': 'Load Image',
    'INPUT_IMAGE_POSITION': [50, 200, 350, 350],
    'INPUT_IMAGE_NAME': 'inputImageLabel',
    'BREAST_TISSUE_RADIO_BUTTON_POSITION': [570, 420, 150, 25],
    'BREAST_TISSUE_RADIO_BUTTON_NAME': 'breastTissueRadioButton',
    'BREAST_TISSUE_RADIO_BUTTON_TEXT': 'Breast Tissue',
    'COLORECTAL_TISSUE_RADIO_BUTTON_POSITION': [570, 450, 175, 25],
    'COLORECTAL_TISSUE_RADIO_BUTTON_NAME': 'colorectalTissueRadioButton',
    'COLORECTAL_TISSUE_RADIO_BUTTON_TEXT': 'Colorectal Tissue',
    'CLASSIFY_BUTTON_POSITION': [565, 510, 150, 50],
    'CLASSIFY_BUTTON_NAME': 'classifyButton',
    'CLASSIFY_BUTTON_TEXT': 'Classify',
    'VGG19_SIMPLE_MODEL_PATH': '/home/lenovo/Documents/bachelors_thesis/histopathologic-cancer-detection/experiments/' +
                               'break_his_models/VGG19Test_03-03-2020_08:51:10/VGG19Test.h5',
    'CNN_SIMPLE_MODEL_PATH': '/home/lenovo/Documents/bachelors_thesis/histopathologic-cancer-detection/experiments/' +
                             'nct_crc_he_100k_models/CNNSimpleTest_12-03-2020_15:49:03/CNNSimpleTest.h5',
    'PREDICTED_CLASS_LABEL_POSITION': [955, 135, 200, 50],
    'PREDICTED_CLASS_LABEL_NAME': 'predictedClassLabel',
    'PREDICTED_CLASS_LABEL_TEXT': 'Class',
    'PROGRESS_BAR_POSITION': [540, 610, 200, 25],
    'PROGRESS_BAR_NAME': 'classificationProgressBar',
    'CLASS_PROBABILITIES_PLOT_POSITION': [850, 200, 400, 400],
    'CLASS_PROBABILITIES_PLOT_NAME': 'classProbabilitiesPlot',
    'MENU_BAR_POSITION': [0, 0, 1280, 25],
    'MENU_BAR_NAME': 'menuBar',
    'MENU': {
        'FILE_NAME': 'menuFile', 'FILE_TEXT': 'File',
        'FURTHER_ANALYSIS_NAME': 'menuFurtherAnalysis', 'FURTHER_ANALYSIS_TEXT': 'Further Analysis',
        'ABOUT_NAME': 'menuAbout', 'ABOUT_TEXT': 'About',
        'APPLICATION_NAME': 'menuApplication', 'APPLICATION_TEXT': 'Application',
        'DATASETS_NAME': 'menuDatasets', 'DATASETS_TEXT': 'Datasets',
        'MODELS_NAME': 'menuModels', 'MODELS_TEXT': 'Models'
     },
    'ACTION': {
        'MODELS_NAME': 'actionModels', 'MODELS_TEXT': 'Models',
        'AUTHOR_NAME': 'actionAuthor', 'AUTHOR_TEXT': 'Author',
        'HOW_TO_NAME': 'actionHowTo', 'HOW_TO_TEXT': 'How To',
        'BREAK_HIS_NAME': 'actionBreakHis', 'BREAK_HIS_TEXT': 'BreakHis',
        'NCT_CRC_HE_100K_NAME': 'actionNCT_CRC_HE_100K', 'NCT_CRC_HE_100K_TEXT': 'NCT_CRC_HE_100K',
        'CNN_SIMPLE_NAME': 'actionCNNSimple', 'CNN_SIMPLE_TEXT': 'CNNSimple',
        'VGG19_SIMPLE_NAME': 'actionVGG19Simple', 'VGG19_SIMPLE_TEXT': 'VGG19Simple',
        'NETWORK_FILTERS_NAME': 'actionNetworkFilters', 'NETWORK_FILTERS_TEXT': 'Network Filters',
        'INTERMEDIATE_ACTIVATIONS_NAME': 'actionIntermediateActivations', 'INTERMEDIATE_ACTIVATIONS_TEXT': 'Layer Activations',
        'HEATMAPS_NAME': 'actionHeatmaps', 'HEATMAPS_TEXT': 'Heatmaps',
        'GENERAL_NAME': 'actionGeneral', 'GENERAL_TEXT': 'General',
        'EXIT_NAME': 'actionExit', 'EXIT_TEXT': 'Exit'
     }
}
