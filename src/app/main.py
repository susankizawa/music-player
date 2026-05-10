import os
import signal

from PySide6.QtMultimedia import QMediaMetaData, QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, QCoreApplication, QTimer
import sys

import mutagen
from mutagen.easyid3 import EasyID3

from src.models.song import Song

app = QCoreApplication(sys.argv)

# player = QMediaPlayer()
# audio_output = QAudioOutput()
# player.setAudioOutput(audio_output)

# audio_output.setVolume(50)
# file_path = ".\\music\\1-04 Limbus.mp3"
# player.setSource(QUrl.fromLocalFile(file_path))

# player.play()

# song_file = EasyID3(file_path)

# print("")

# if song_file.items():
#     for key, value in song_file.items():
#         print(f"{key}: {value}")
# else:
#     print(os.path.basename(file_path))

# print("")

song = Song(".\\music\\1-04 Limbus.mp3", "Limbus")

print(song.__file_path)

# handles interrupt signal (Ctrl+C) to allow graceful exit
signal.signal(signal.SIGINT, signal.SIG_DFL)

sys.exit(app.exec())