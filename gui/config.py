import os
import gui.gui_components as GUI

FONT = GUI.get_font('Sans Serif', 12)
BACKGROUND_COLOR = 'rgb(42, 49, 56)'
FONT_COLOR = 'white'
CENTRAL_WIDGET = 'central_widget'
REPO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
TEMPORARY_PLOTS_DIR = os.path.join(REPO_DIR, 'gui', 'temporary_plots')
VGG19_SIMPLE_MODEL_PATH = os.path.join(REPO_DIR, 'experiments', 'break_his_models',
                                       'VGG19Simple', 'VGG19Simple.h5')
CNN_SIMPLE_MODEL_PATH = os.path.join(REPO_DIR, 'experiments', 'nct_crc_he_100k_models', 'CNNSimple', 'CNNSimple.h5')

ABOUT_AUTHOR_CONFIG = {
    'WINDOW_NAME': 'AboutAuthorWindow',
    'WINDOW_TITLE': 'About Author',
    'WINDOW_X': 640,
    'WINDOW_Y': 250,
    'IMAGE_LABEL_POSITION': [50, 35, 100, 150],
    'IMAGE_LABEL_NAME': 'authorImageLabel',
    'AUTHOR_IMAGE_PATH': os.path.join(REPO_DIR, 'gui', 'resources', 'author.jpg'),
    'RESUME_LABEL_POSITION': [140, 20, 450, 200],
    'RESUME_LABEL_NAME': 'resumeLabel',
    'RESUME': '''
              Student from Serbia, currently undertaking BSc
              in Computer Science at Eötvös Loránd
              University in Budapest. Strong mathematical
              background, skilled in machine learning,
              statistics and programming. Wrote
              Histopathologic Cancer Detection as part of
              final thesis paper.

              github.com/bmarko98
              '''
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
        'IMAGES_PATH': os.path.join(REPO_DIR, 'data', 'break_his', 'break_his_sample_images.jpg'),
        'DATASET_OVERVIEW_PATH': os.path.join(REPO_DIR, 'data', 'break_his', 'break_his_dataset_overview.txt')
        },
    'NCT_CRC_HE_100K': {
        'WINDOW_NAME': 'AboutDatasetsWindow',
        'WINDOW_TITLE': 'About NCT_CRC_HE_100K Dataset',
        'WINDOW_X': 1600,
        'WINDOW_Y': 1000,
        'OVERVIEW_LABEL_POSITION': [75, 5, 400, 1000],
        'OVERVIEW_LABEL_NAME': 'datasetOverviewLabel',
        'IMAGES_LABEL_POSITIONS': [550, 200, 950, 600],
        'IMAGES_LABEL_NAME': 'datasetImagesLabel',
        'IMAGES_PATH': os.path.join(REPO_DIR, 'data', 'nct_crc_he_100k', 'nct_crc_he_100k_sample_images.jpg'),
        'DATASET_OVERVIEW_PATH': os.path.join(REPO_DIR, 'data', 'nct_crc_he_100k', 'nct_crc_he_100k_dataset_overview.txt')
        }
}

ABOUT_MODELS_CONFIG = {
    'VGG19_SIMPLE': {
        'WINDOW_NAME': 'AboutModelsWindow',
        'WINDOW_TITLE': 'About VGG19Simple Model',
        'WINDOW_X': 1800,
        'WINDOW_Y': 700,
        'MODEL_NAME': 'VGG19Simple',
        'MODEL_NAME_LABEL_POSITION': [110, 100, 300, 25],
        'MODEL_NAME_LABEL_NAME': 'modelNameLabel',
        'MODEL_SUMMARY_LABEL_POSITION': [25, 135, 500, 450],
        'MODEL_SUMMARY_LABEL_NAME': 'modelSummaryLabel',
        'ACCURACY_LABEL_POSITION': [550, 34, 400, 316],
        'ACCURACY_LABEL_NAME': 'accuracyLabel',
        'ACCURACY_PATH': os.path.join(os.path.dirname(VGG19_SIMPLE_MODEL_PATH), 'plots', 'accuracy_plot.png'),
        'LOSS_LABEL_POSITION': [550, 350, 400, 316],
        'LOSS_LABEL_NAME': 'lossLabel',
        'LOSS_PATH': os.path.join(os.path.dirname(VGG19_SIMPLE_MODEL_PATH), 'plots', 'loss_plot.png'),
        'CONF_MATRIX_LABEL_POSITION': [950, 70, 800, 560],
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
        'MODEL_NAME_LABEL_NAME': 'modelNameLabel',
        'MODEL_SUMMARY_LABEL_POSITION': [25, 70, 500, 950],
        'MODEL_SUMMARY_LABEL_NAME': 'modelSummaryLabel',
        'ACCURACY_LABEL_POSITION': [550, 188, 400, 312],
        'ACCURACY_LABEL_NAME': 'accuracyLabel',
        'ACCURACY_PATH': os.path.join(os.path.dirname(CNN_SIMPLE_MODEL_PATH), 'plots', 'accuracy_plot.png'),
        'LOSS_LABEL_POSITION': [550, 500, 400, 312],
        'LOSS_LABEL_NAME': 'lossLabel',
        'LOSS_PATH': os.path.join(os.path.dirname(CNN_SIMPLE_MODEL_PATH), 'plots', 'loss_plot.png'),
        'CONF_MATRIX_LABEL_POSITION': [950, 220, 800, 560],
        'CONF_MATRIX_LABEL_NAME': 'confMatrixLabel',
        'CONF_MATRIX_PATH': os.path.join(os.path.dirname(CNN_SIMPLE_MODEL_PATH), 'plots', 'confusion_matrix.png'),
        'MODEL_SUMMARY_PATH': os.path.join(os.path.dirname(CNN_SIMPLE_MODEL_PATH), 'CNNSimple_architecture.txt'),
    }
}

SIMPLE_CONFIG = {
    'GENERAL': {
        'WINDOW_NAME': 'BasicUseWindow',
        'WINDOW_TITLE': 'Basic Use',
        'WINDOW_X': 640,
        'WINDOW_Y': 400,
        'TEXT': '''
                Basic use of Histopathologic Canced Detection:

                1. Predicting tissue and cancer subtype of breast and colorectal
                tissue, i.e. predicting whether patient has breast or colorectal
                cancer or not
                    - load image by clicking 'Load Image' button
                    - set tissue type by choosing appropriate radio button
                    - classify slide by clicking 'Classify' button

                2. Visualizing what Convolutional Neural Network learns, i.e.
                visualizing how network transforms input image, and which parts
                of input image lead to predicting tissue and cancer subtype
                    - visualize heatmap of class activations by selecting:
                        Further Analysis -> Heatmap
                    - visualize filters of convolutional layers by selecting:
                        Further Analysis -> Network Filters
                    - visualize intermediate activations by selecting:
                        Further Analysis -> Class Activations
                ''',
        'SIMPLE_INFO_LABEL_POSITION': [-30, 0, 620, 380],
        'SIMPLE_INFO_LABEL_NAME': 'simpleInfoLabel',
        'SIMPLE_INFO_LABEL_IMAGE_PATH': None
    },
    'HOWTO': {
        'WINDOW_NAME': 'AdvancedUseWindow',
        'WINDOW_TITLE': 'Advanced Use',
        'WINDOW_X': 760,
        'WINDOW_Y': 460,
        'TEXT': '''
                Advanced use of Histopathologic Cancer Detection:

                Adding additional tissue type (ex. lung tissue), along with tissue/cancer subtype
                classification can be accomplished in four steps:

                1. Creating dataset
                - Obtaining dataset of new tissue type, and preparing dataset to be fed to Keras-
                built CNN, which includes creating appropriate directory structure

                2. Building CNN
                - Crating new convolutional neural network class inherited from BaseCNN by
                defining data generator transformations, network architecture, etc.

                3. Fine-tuning CNN
                - Defining hyperparameter dictionary and training neural networks in order to
                increase classification accuracy and prevent overfitting

                4. Extending GUI
                - Adding additional radio button to MainWindow class, and extending action
                associated with classify button, as well as further analysis actions, to use newly
                created network
                ''',
        'SIMPLE_INFO_LABEL_POSITION': [-40, 0, 740, 440],
        'SIMPLE_INFO_LABEL_NAME': 'simpleInfoLabel',
        'SIMPLE_INFO_LABEL_IMAGE_PATH': None
    },
    'IMAGE': {
        'WINDOW_NAME': 'ImageWindow',
        'WINDOW_TITLE': ' ',
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
    'PREDICTED_CLASS_LABEL_POSITION': [830, 85, 200, 50],
    'PREDICTED_CLASS_LABEL_NAME': 'predictedClassLabel',
    'PREDICTED_CLASS_LABEL_TEXT': 'Class',
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
        'HOW_TO_NAME': 'actionHowTo', 'HOW_TO_TEXT': 'Advanced Use',
        'BREAK_HIS_NAME': 'actionBreakHis', 'BREAK_HIS_TEXT': 'BreakHis',
        'NCT_CRC_HE_100K_NAME': 'actionNCT_CRC_HE_100K', 'NCT_CRC_HE_100K_TEXT': 'NCT_CRC_HE_100K',
        'CNN_SIMPLE_NAME': 'actionCNNSimple', 'CNN_SIMPLE_TEXT': 'CNNSimple',
        'VGG19_SIMPLE_NAME': 'actionVGG19Simple', 'VGG19_SIMPLE_TEXT': 'VGG19Simple',
        'NETWORK_FILTERS_NAME': 'actionNetworkFilters', 'NETWORK_FILTERS_TEXT': 'Network Filters',
        'INTERMEDIATE_ACTIVATIONS_NAME': 'actionIntermediateActivations', 'INTERMEDIATE_ACTIVATIONS_TEXT': 'Layer Activations',
        'HEATMAP_NAME': 'actionHeatmap', 'HEATMAP_TEXT': 'Heatmap',
        'GENERAL_NAME': 'actionGeneral', 'GENERAL_TEXT': 'Basic Use',
        'EXIT_NAME': 'actionExit', 'EXIT_TEXT': 'Exit',
        'SAVE_NAME': 'actionSave', 'SAVE_TEXT': 'Save'
     }
}
