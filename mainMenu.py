import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from buttons import create_button, set_button_icon
from subprocesses import start_client, start_server

WIDTH = 800
HEIGHT = 600

LONG_BUTTON_WIDTH = 256
LONG_BUTTON_HEIGHT = 128


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Button")
        self.setFixedSize(WIDTH, HEIGHT)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.logo_pixmap = QPixmap("img/buttons/button.png")
        self.setWindowIcon(QIcon(self.logo_pixmap))
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap('img/backgrounds/bg.png'))
        self.background_label.resize(self.size())
        self.background_label.lower()

        self.to_look_button = create_button(self, 'img/buttons/toLookButtonUnpressed.png',
                                            (WIDTH - WIDTH + 100, int((HEIGHT / 3) * 2)),
                                            (LONG_BUTTON_WIDTH, LONG_BUTTON_HEIGHT),
                                            self.to_look_button_clicked)

        self.to_do_button = create_button(self, 'img/buttons/todoButtonUnpressed.png',
                                          (WIDTH - LONG_BUTTON_WIDTH - 100, int((HEIGHT / 3) * 2)),
                                          (LONG_BUTTON_WIDTH, LONG_BUTTON_HEIGHT),
                                          self.to_do_button_clicked)

    def to_look_button_clicked(self):
        set_button_icon(self.to_look_button, 'img/buttons/toLookButtonPressed.png')
        start_server()

    def to_do_button_clicked(self):
        set_button_icon(self.to_do_button, 'img/buttons/toDoButtonPressed.jpg.png')
        start_client()

    def close_main_window(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
