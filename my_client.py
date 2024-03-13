import sys
import socket
import time
from pygame import mixer
from buttons import create_button, set_button_icon
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout, QInputDialog

WIDTH = 800
HEIGHT = 600

BUTTON_WIDTH = 130
BUTTON_HEIGHT = 130

btn_counter = [0, 0, 0]


class ClientWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CCTV room")
        self.setFixedSize(WIDTH, HEIGHT)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.logo_pixmap = QPixmap("img/buttons/button.png")
        self.setWindowIcon(QIcon(self.logo_pixmap))
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap('img/backgrounds/bg.png'))
        self.background_label.resize(self.size())
        self.background_label.lower()

        self.btn_pixmap = QPixmap("img/buttons/button.png")
        self.btn_pixmap = self.btn_pixmap.scaled(BUTTON_WIDTH, BUTTON_HEIGHT, Qt.KeepAspectRatio)
        self.btnprsd_pixmap = QPixmap("img/buttons/buttonpressed.png")
        self.btnprsd_pixmap = self.btnprsd_pixmap.scaled(BUTTON_WIDTH, BUTTON_HEIGHT, Qt.KeepAspectRatio)

        self.window_button = create_button(self, self.btn_pixmap, [BUTTON_WIDTH, BUTTON_HEIGHT], self.window_func)
        self.light_button = create_button(self, self.btn_pixmap,  [BUTTON_WIDTH, BUTTON_HEIGHT], self.light_func)
        self.scare_button = create_button(self, self.btn_pixmap, [BUTTON_WIDTH, BUTTON_HEIGHT], self.scare_func)

        # Сетка для удобства расположения кнопок
        self.grid = QGridLayout(self)
        self.grid.setContentsMargins(0, 350, 0, 0)
        self.grid.addWidget(self.window_button, 0, 0)
        self.grid.addWidget(self.light_button, 0, 1)
        self.grid.addWidget(self.scare_button, 0, 2)

        self.ip_address = QInputDialog.getText(self, 'Ввод IP', 'Enter IP:')

        self.connect_to_server()

    def window_func(self):
        if btn_counter[0] == 0:
            btn_counter[0] += 1
            self.window_button.setIcon(QIcon(self.btnprsd_pixmap))
            self.client_socket.send('1'.encode('utf-8'))
        elif btn_counter[0] == 1:
            btn_counter[0] -= 1
            self.window_button.setIcon(QIcon(self.btn_pixmap))
            self.client_socket.send('1'.encode('utf-8'))
        play_sound("sfx/button.mp3")

    def light_func(self):
        if btn_counter[1] == 0:
            btn_counter[1] += 1
            self.light_button.setIcon(QIcon(self.btnprsd_pixmap))
            self.client_socket.send('2'.encode('utf-8'))
        elif btn_counter[1] == 1:
            btn_counter[1] -= 1
            self.light_button.setIcon(QIcon(self.btn_pixmap))
            self.client_socket.send('2'.encode('utf-8'))
        play_sound("sfx/button.mp3")

    def scare_func(self):
        if btn_counter[2] == 0:
            btn_counter[2] += 1
            self.scare_button.setIcon(QIcon(self.btnprsd_pixmap))
            self.client_socket.send('3'.encode('utf-8'))
        elif btn_counter[2] == 1:
            btn_counter[2] -= 1
            self.scare_button.setIcon(QIcon(self.btn_pixmap))
            self.client_socket.send('3'.encode('utf-8'))
        play_sound("sfx/button.mp3")

    def connect_to_server(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.ip_address[0], 8888))


def play_sound(sound_file):
    mixer.init()
    mixer.music.load(sound_file)
    mixer.music.play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = ClientWindow()
    main_window.show()
    sys.exit(app.exec_())
