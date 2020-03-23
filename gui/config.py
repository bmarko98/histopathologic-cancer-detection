import os
import gui.gui_components as GUI

FONT = GUI.get_font('Sans Serif', 12)
BACKGROUND_COLOR = 'rgb(42, 49, 56)'
FONT_COLOR = 'white'
CENTRAL_WIDGET = 'central_widget'
REPO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
TEMPORARY_PLOTS_DIR = os.path.join(REPO_DIR, 'gui', 'temporary_plots')
VGG19_SIMPLE_MODEL_PATH = os.path.join(REPO_DIR, 'experiments', 'break_his_models', 'VGG19Simple', 'VGG19Simple.h5')
CNN_SIMPLE_MODEL_PATH = os.path.join(REPO_DIR, 'experiments', 'nct_crc_he_100k_models', 'CNNSimple', 'CNNSimple.h5')

ABOUT_AUTHOR_CONFIG = {
    'WINDOW_NAME': 'AboutAuthorWindow',
    'WINDOW_TITLE': 'About Author',
    'WINDOW_X': 640,
    'WINDOW_Y': 400,
    'IMAGE_LABEL_POSITION': [50, 75, 100, 150],
    'IMAGE_LABEL_NAME': 'authorImageLabel',
    'AUTHOR_IMAGE_PATH': os.path.join(REPO_DIR, 'gui', 'resources', 'author.jpg'),
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
        'IMAGES_URL': os.path.join(REPO_DIR, 'data', 'break_his', 'break_his_sample_images.jpg'),
        'DATASET_OVERVIEW_PATH': os.path.join(REPO_DIR, 'data', 'break_his', 'break_his_dataset_overview.txt')
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
        'IMAGES_URL': os.path.join(REPO_DIR, 'data', 'nct_crc_he_100k', 'nct_crc_he_100k_sample_images.jpg'),
        'DATASET_OVERVIEW_PATH': os.path.join(REPO_DIR, 'data', 'nct_crc_he_100k', 'nct_crc_he_100k_dataset_overview.txt')
        }
}

ABOUT_MODELS_CONFIG = {
    'VGG19_SIMPLE': {
        'WINDOW_NAME': 'AboutModelsWindow',
        'WINDOW_TITLE': 'About VGG19Simple Model',
        'WINDOW_X': 1800,
        'WINDOW_Y': 900,
        'MODEL_NAME': 'VGG19Simple',
        'MODEL_NAME_LABEL_POSITION': [110, 200, 300, 25],
        'MODEL_NAME_LABEL_NAME': 'modelNameLabel',
        'MODEL_SUMMARY_LABEL_POSITION': [25, 235, 500, 450],
        'MODEL_SUMMARY_LABEL_NAME': 'modelSummaryLabel',
        'ACCURACY_LABEL_POSITION': [550, 50, 400, 400],
        'ACCURACY_LABEL_NAME': 'accuracyLabel',
        'ACCURACY_PATH': os.path.join(os.path.dirname(VGG19_SIMPLE_MODEL_PATH), 'plots', 'accuracy_plot.png'),
        'LOSS_LABEL_POSITION': [550, 450, 400, 400],
        'LOSS_LABEL_NAME': 'lossLabel',
        'LOSS_PATH': os.path.join(os.path.dirname(VGG19_SIMPLE_MODEL_PATH), 'plots', 'loss_plot.png'),
        'CONF_MATRIX_LABEL_POSITION': [950, 50, 800, 800],
        'CONF_MATRIX_LABEL_NAME': 'confMatrixLabel',
        'CONF_MATRIX_PATH': os.path.join(os.path.dirname(VGG19_SIMPLE_MODEL_PATH), 'plots', 'confusion_matrix.png'),
        'MODEL_SUMMARY_PATH': os.path.join(os.path.dirname(VGG19_SIMPLE_MODEL_PATH), 'VGG19Simple_architecture.txt'),
    },
    'CNN_SIMPLE': {
        'WINDOW_NAME': 'AboutModelsWindow',
        'WINDOW_TITLE': 'About CNNSimple Model',
        'WINDOW_X': 1800,
        'WINDOW_Y': 1000,
        'MODEL_NAME': 'CNNSimple',
        'MODEL_NAME_LABEL_POSITION': [110, 35, 300, 25],
        'MODEL_NAME_LABEL_NAME': 'modelSummaryLabel',
        'MODEL_SUMMARY_LABEL_POSITION': [25, 70, 500, 950],
        'MODEL_SUMMARY_LABEL_NAME': 'modelSummaryLabel',
        'ACCURACY_LABEL_POSITION': [550, 50, 400, 400],
        'ACCURACY_LABEL_NAME': 'accuracyLabel',
        'ACCURACY_PATH': os.path.join(os.path.dirname(CNN_SIMPLE_MODEL_PATH), 'plots', 'accuracy_plot.png'),
        'LOSS_LABEL_POSITION': [550, 450, 400, 400],
        'LOSS_LABEL_NAME': 'lossLabel',
        'LOSS_PATH': os.path.join(os.path.dirname(CNN_SIMPLE_MODEL_PATH), 'plots', 'loss_plot.png'),
        'CONF_MATRIX_LABEL_POSITION': [950, 50, 800, 800],
        'CONF_MATRIX_LABEL_NAME': 'confMatrixLabel',
        'CONF_MATRIX_PATH': os.path.join(os.path.dirname(CNN_SIMPLE_MODEL_PATH), 'plots', 'confusion_matrix.png'),
        'MODEL_SUMMARY_PATH': os.path.join(os.path.dirname(CNN_SIMPLE_MODEL_PATH), 'CNNSimple_architecture.txt'),
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
    },
    'HEATMAP': {
        'WINDOW_NAME': 'HeatmapWindow',
        'WINDOW_TITLE': 'Heatmap',
        'WINDOW_X': None,
        'WINDOW_Y': None,
        'TEXT': '',
        'SIMPLE_INFO_LABEL_POSITION': None,
        'SIMPLE_INFO_LABEL_NAME': 'simpleInfoLabel',
        'SIMPLE_INFO_LABEL_IMAGE_PATH': None
    }
}

INSPECT_CONV_CONFIG = {
    'FILTER_PATTERNS': {
        'WINDOW_NAME': 'InspectConvWindow',
        'WINDOW_TITLE': 'Filter Patterns',
        'WINDOW_X': 400,
        'WINDOW_Y': 165,
        'CONV_LAYER_LABEL_POSITION': [20, 20, 200, 25],
        'CONV_LAYER_LABEL_NAME': 'convLayerLabel',
        'CONV_LAYER_LABEL_TEXT': 'Convolutional Layer',
        'NUMBER_LABEL_POSITION': [20, 55, 150, 25],
        'NUMBER_LABEL_NAME': 'filterNumberLabel',
        'NUMBER_LABEL_TEXT': 'Filter Number',
        'IMAGE_LABEL_POSITION': [450, 80, 600, 600],
        'IMAGE_LABEL_NAME': 'filterPatternLabel',
        'BUTTON_POSITION': [100, 100, 200, 40],
        'BUTTON_NAME': 'showFilterButton',
        'BUTTON_TEXT': 'Show Filter Patterns',
        'COMBO_BOX_POSITION': [225, 20, 140, 25],
        'COMBO_BOX_NAME': 'layerComboBox',
        'COMBO_BOX_ITEMS': [],
        'LINE_EDIT_POSITION': [160, 55, 50, 25],
        'LINE_EDIT_NAME': 'filterNumberEdit',
    },
    'LAYER_ACTIVATIONS': {
        'WINDOW_NAME': 'InspectConvWindow',
        'WINDOW_TITLE': 'Layer Activations',
        'WINDOW_X': 315,
        'WINDOW_Y': 165,
        'CONV_LAYER_LABEL_POSITION': [-20, 20, 200, 25],
        'CONV_LAYER_LABEL_NAME': 'convLayerLabel',
        'CONV_LAYER_LABEL_TEXT': 'Layer',
        'NUMBER_LABEL_POSITION': [50, 55, 150, 25],
        'NUMBER_LABEL_NAME': 'channelNumberLabel',
        'NUMBER_LABEL_TEXT': 'Channel Number',
        'IMAGE_LABEL_POSITION': [450, 75, 600, 600],
        'IMAGE_LABEL_NAME': 'activationLabel',
        'BUTTON_POSITION': [45, 100, 205, 40],
        'BUTTON_NAME': 'showActivationButton',
        'BUTTON_TEXT': 'Show Layer Activations',
        'COMBO_BOX_POSITION': [125, 20, 140, 25],
        'COMBO_BOX_NAME': 'layerComboBox',
        'COMBO_BOX_ITEMS': [],
        'LINE_EDIT_POSITION': [210, 55, 50, 25],
        'LINE_EDIT_NAME': 'channelNumberEdit'
    }
}

MAIN_CONFIG = {
    'WINDOW_NAME': 'MainWindow',
    'WINDOW_TITLE': 'Histopathologic Cancer Detection',
    'WINDOW_X': 1280,
    'WINDOW_Y': 600,
    'LOAD_IMAGE_BUTTON_POSITION': [150, 50, 150, 50],
    'LOAD_IMAGE_BUTTON_NAME': 'loadImageButton',
    'LOAD_IMAGE_BUTTON_TEXT': 'Load Image',
    'INPUT_IMAGE_POSITION': [50, 150, 350, 350],
    'INPUT_IMAGE_NAME': 'inputImageLabel',
    'BREAST_TISSUE_RADIO_BUTTON_POSITION': [570, 270, 150, 25],
    'BREAST_TISSUE_RADIO_BUTTON_NAME': 'breastTissueRadioButton',
    'BREAST_TISSUE_RADIO_BUTTON_TEXT': 'Breast Tissue',
    'COLORECTAL_TISSUE_RADIO_BUTTON_POSITION': [570, 300, 175, 25],
    'COLORECTAL_TISSUE_RADIO_BUTTON_NAME': 'colorectalTissueRadioButton',
    'COLORECTAL_TISSUE_RADIO_BUTTON_TEXT': 'Colorectal Tissue',
    'CLASSIFY_BUTTON_POSITION': [565, 360, 150, 50],
    'CLASSIFY_BUTTON_NAME': 'classifyButton',
    'CLASSIFY_BUTTON_TEXT': 'Classify',
    'VGG19_SIMPLE_MODEL_PATH': VGG19_SIMPLE_MODEL_PATH,
    'CNN_SIMPLE_MODEL_PATH': CNN_SIMPLE_MODEL_PATH,
    'PREDICTED_CLASS_LABEL_POSITION': [955, 85, 200, 50],
    'PREDICTED_CLASS_LABEL_NAME': 'predictedClassLabel',
    'PREDICTED_CLASS_LABEL_TEXT': 'Class',
    'PROGRESS_BAR_POSITION': [540, 460, 200, 25],
    'PROGRESS_BAR_NAME': 'classificationProgressBar',
    'CLASS_PROBABILITIES_PLOT_POSITION': [850, 150, 350, 350],
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
        'HEATMAP_NAME': 'actionHeatmap', 'HEATMAP_TEXT': 'Heatmap',
        'GENERAL_NAME': 'actionGeneral', 'GENERAL_TEXT': 'General',
        'EXIT_NAME': 'actionExit', 'EXIT_TEXT': 'Exit',
        'SAVE_NAME': 'actionSave', 'SAVE_TEXT': 'Save'
     }
}
