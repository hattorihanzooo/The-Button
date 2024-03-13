import sys
import time
import socket
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QIcon, QFontDatabase, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QInputDialog
from threading import Thread
from my_client import play_sound

WEIGHT = 800
HEIGHT = 600


class ServerWindow(QWidget):
    room_changed = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("CAM 01")
        self.setFixedSize(WEIGHT, HEIGHT)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.logo_pixmap = QPixmap("img/buttons/button.png")
        self.setWindowIcon(QIcon(self.logo_pixmap))
        self.background_pixmap = QPixmap('img/rooms/room1.jpg')
        self.background_label = QLabel(self)
        self.background_label.setPixmap(self.background_pixmap)
        self.background_label.resize(self.size())
        self.background_label.lower()

        QFontDatabase.addApplicationFont('fonts/Visitor Rus.ttf')
        self.label = QLabel('Ожидание подключения...', self)
        self.label.setFont(QFont('Visitor_Rus', 16))
        self.label.setStyleSheet("color: white;")
        self.label.move(10, HEIGHT - 50)

        self.lights = True
        self.room_window = False
        self.screamer_counter = 0

        self.listen_thread = None
        self.server_socket = None
        self.client_socket = None

        self.ip_address = QInputDialog.getText(self, 'Ввод IP', 'Enter IP:')

        self.start_server()

    def start_server(self):
        # Создание сокета для подключения Клиента
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.ip_address[0], 8888))
        self.server_socket.listen(1)

        # Создание потока для прослушивания значений кнопок

        self.listen_thread = Thread(target=self.listen_for_room)
        self.listen_thread.daemon = True
        self.listen_thread.start()

    def listen_for_room(self):
        self.client_socket, _ = self.server_socket.accept()
        self.label.setText("Подключено успешно.")
        time.sleep(3)
        self.label.deleteLater()

        while True:
            room_number = self.client_socket.recv(1024).decode()
            if room_number:
                if room_number == "1" and self.screamer_counter < 10:
                    self.lights = not self.lights
                    self.room_changed.emit(room_number)
                    play_sound("sfx/metal window.wav")
                elif room_number == "2" and self.screamer_counter < 10:
                    self.room_window = not self.room_window
                    self.room_changed.emit(room_number)
                    play_sound("sfx/light.wav")
                elif room_number == "3":
                    self.screamer_counter += 1
                    self.room_changed.emit(room_number)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    server_window = ServerWindow()


    def on_room_changed():
        if server_window.screamer_counter == 10:
            play_sound("sfx/scare.mp3")
        if server_window.screamer_counter >= 10:
            room_image_path = 'img/rooms/room5.jpg'
        elif server_window.lights and server_window.room_window:
            room_image_path = 'img/rooms/room3.jpg'
        elif server_window.room_window:
            room_image_path = 'img/rooms/room4.jpg'
        elif server_window.lights:
            room_image_path = 'img/rooms/room1.jpg'
        else:
            room_image_path = 'img/rooms/room2.jpg'

        room_pixmap = QPixmap(room_image_path)
        server_window.background_label.setPixmap(room_pixmap)


    server_window.show()
    server_window.room_changed.connect(on_room_changed)
    sys.exit(app.exec_())
