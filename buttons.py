from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QPushButton

# Этот модуль содержит в себе функции, используемые для отрисовки кнопок в Главном меню и приложении Клиента


def create_button(parent, icon_path, size, clicked_slot):
    width, height = size
    button = QPushButton(parent)
    button.setFixedSize(width, height)
    button.setStyleSheet("QPushButton { border: none; background-color: transparent; }")
    button.clicked.connect(clicked_slot)
    set_button_icon(button, icon_path)
    return button


def set_button_icon(button, image_path):
    pixmap = QPixmap(image_path)
    button.setIcon(QIcon(pixmap))
    button.setIconSize(pixmap.size())
