from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QPushButton

LONG_BUTTON_WIDTH = 256
LONG_BUTTON_HEIGHT = 128


def create_button(parent, icon_path, position, clicked_slot):
    x, y = position
    button = QPushButton(parent)
    button.setFixedSize(LONG_BUTTON_WIDTH, LONG_BUTTON_HEIGHT)
    button.setStyleSheet("QPushButton { border: none; background-color: transparent; }")
    button.move(x, y)
    button.clicked.connect(clicked_slot)
    set_button_icon(button, icon_path)
    return button


def set_button_icon(button, image_path):
    pixmap = QPixmap(image_path)
    button.setIcon(QIcon(pixmap))
    button.setIconSize(pixmap.size())
