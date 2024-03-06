import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget
from my_server import ServerWindow

WEIGHT = 800
HEIGHT = 600


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button The Game")
        self.setFixedSize(WEIGHT, HEIGHT)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.logo_pixmap = QPixmap('img/buttons/button.png')
        self.setWindowIcon(QIcon(self.logo_pixmap))
        self.background_pixmap = QPixmap('img/backgrounds/bg.png')
        self.background_label = QLabel(self)
        self.background_label.setPixmap(self.background_pixmap)
        self.background_label.resize(self.size())
        self.background_label.lower()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())