import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl

class VideoBackgroundWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Background")
        self.setGeometry(100, 100, 800, 600)

        self.video_widget = QVideoWidget(self)
        self.setCentralWidget(self.video_widget)

        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.media_player.setVideoOutput(self.video_widget)

        # Укажите путь к вашему видеоролику
        video_url = QUrl.fromLocalFile("путь_к_вашему_видео.mp4")
        media_content = QMediaContent(video_url)
        self.media_player.setMedia(media_content)

        self.media_player.play()

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoBackgroundWindow()
    sys.exit(app.exec_())
