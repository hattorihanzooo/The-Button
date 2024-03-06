import sys
import time
import socket
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QIcon, QFontDatabase, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from threading import Thread

WEIGHT = 800
HEIGHT = 600


class ServerWindow(QWidget):
    room_changed = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button The Game")
        self.setFixedSize(WEIGHT, HEIGHT)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.logo_pixmap = QPixmap("button.png")
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
        self.label.move(10, HEIGHT-50)

        self.lights = True
        self.room_window = False

        self.start_server()

    def start_server(self):
        # Create a socket to receive room number
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('', 8888))  # Use the same port as the sender
        self.server_socket.listen(1)

        print("Waiting for connection...")

        # Start the thread to listen for room number
        self.listen_thread = Thread(target=self.listen_for_room)
        self.listen_thread.daemon = True
        self.listen_thread.start()

    def listen_for_room(self):
        try:
            self.client_socket, _ = self.server_socket.accept()
            print("Connection established.")
            self.label.setText("ПОДКЛЮЧЕНО УСПЕШНО.")
            time.sleep(3)
            self.label.deleteLater()

            while True:
                room_number = self.client_socket.recv(1024).decode().strip()
                if room_number:
                    if room_number == "1":
                        self.lights = not self.lights
                        self.room_changed.emit(room_number)
                        print(room_number, ' ', self.lights)
                    elif room_number == "2":
                        self.room_window = not self.room_window
                        print(room_number, ' ', self.room_window)
                    self.room_changed.emit(room_number)
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    server_window = ServerWindow()

    def on_room_changed(room_number):
        print('gvg')
        room_image_path = ''
        if server_window.lights and server_window.room_window:
            room_image_path = 'img/rooms/room3.jpg'
        elif server_window.room_window:
            room_image_path = 'img/rooms/room4.jpg'
        elif server_window.lights:
            room_image_path = 'img/rooms/room1.jpg'
        else:
            room_image_path = 'img/rooms/room2.jpg'

        try:
            room_pixmap = QPixmap(room_image_path)
            server_window.background_label.setPixmap(room_pixmap)
        except FileNotFoundError:
            print(f"Room {room_number} image not found.")

    server_window.show()
    server_window.room_changed.connect(on_room_changed)
    sys.exit(app.exec_())
