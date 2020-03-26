import sys
from PyQt5 import QtCore, QtGui, QtWidgets


def get_font(family, size):
    font = QtGui.QFont()
    font.setFamily(family)
    font.setPointSize(size)
    return font


def get_widget(window, widget_name):
    widget = QtWidgets.QWidget(window)
    widget.setObjectName(widget_name)
    return widget


def get_button(widget, x, y, width, height, button_font, button_name):
    button = QtWidgets.QPushButton(widget)
    button.setGeometry(QtCore.QRect(x, y, width, height))
    button.setFont(button_font)
    button.setObjectName(button_name)
    return button


def get_label(widget, x, y, width, height, label_font, scale, label_name, allign=QtCore.Qt.AlignCenter):
    label = QtWidgets.QLabel(widget)
    label.setGeometry(QtCore.QRect(x, y, width, height))
    label.setFont(label_font)
    label.setScaledContents(scale)
    label.setAlignment(allign)
    label.setObjectName(label_name)
    return label


def get_image_label(widget, x, y, width, height, image_label_font, scale, image_label_name, image_URL):
    if not check_screen_size(width, height):
        width, height = resize(width, height)
    image_label = get_label(widget, x, y, width, height, image_label_font, scale, image_label_name)
    if image_URL is not None:
        image_label.setPixmap(QtGui.QPixmap(image_URL))
    return image_label


def get_radio_button(widget, x, y, width, height, radio_button_font, radio_button_name):
    radio_button = QtWidgets.QRadioButton(widget)
    radio_button.setGeometry(QtCore.QRect(x, y, width, height))
    radio_button.setFont(radio_button_font)
    radio_button.setObjectName(radio_button_name)
    return radio_button


def get_progress_bar(widget, x, y, width, height, progress_bar_name):
    progress_bar = QtWidgets.QProgressBar(widget)
    progress_bar.setGeometry(QtCore.QRect(x, y, width, height))
    progress_bar.setProperty("value", 0)
    progress_bar.setObjectName(progress_bar_name)
    return progress_bar


def get_menu_bar(window, x, y, width, height, menu_bar_font, menu_bar_name):
    menu_bar = QtWidgets.QMenuBar(window)
    menu_bar.setGeometry(QtCore.QRect(x, y, width, height))
    menu_bar.setFont(menu_bar_font)
    menu_bar.setObjectName(menu_bar_name)
    return menu_bar


def get_menu(menu_bar, menu_name):
    menu = QtWidgets.QMenu(menu_bar)
    menu.setObjectName(menu_name)
    return menu


def get_action(window, action_name):
    action = QtWidgets.QAction(window)
    action.setObjectName(action_name)
    return action


def get_combo_box(widget, x, y, width, height, combo_box_font, items, combo_box_name):
    combo_box = QtWidgets.QComboBox(widget)
    combo_box.setGeometry(QtCore.QRect(x, y, width, height))
    combo_box.setFont(combo_box_font)
    for item in items:
        combo_box.addItem(item)
    combo_box.setObjectName(combo_box_name)
    return combo_box


def get_line_edit(widget, x, y, width, height, line_edit_font, line_edit_name):
    line_edit = QtWidgets.QLineEdit(widget)
    line_edit.setGeometry(QtCore.QRect(x, y, width, height))
    line_edit.setFont(line_edit_font)
    line_edit.setObjectName(line_edit_name)
    return line_edit


def check_screen_size(width, height):
    MIN_WIDTH, MIN_HEIGHT = 0, 0
    MAX_WIDTH, MAX_HEIGHT = 1920, 1080
    return (MIN_WIDTH <= width <= MAX_WIDTH) and (MIN_HEIGHT <= height <= MAX_HEIGHT)


def resize(width, height):
    while not check_screen_size(width, height):
        width = int(width/1.2)
        height = int(height/1.2)
    return width, height
