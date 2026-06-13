from src.core.main_window import MainWindow
from src.shared.library import Library
from src.shared.song import Song
from src.features.music_player.audio_handler import AudioHandler
from src.features.file_handler.metadata_parser import MetadataParser
from src.core.startup import load_songs

import sys
from PySide6.QtWidgets import QApplication, QPushButton, QSlider, QLabel, QFileDialog
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

class App(QApplication):
    def __init__(self):
        super().__init__()
        self.audio_handler = AudioHandler()
        self.library = Library()

        load_songs(self.library)

        self.view = MainWindow(self.library, self.audio_handler)

        first_song = self.library.songs[0]

        self.audio_handler.load_song(first_song)

    def run(self):
        self.view.show()
        sys.exit(self.exec())
    
    
    
    
        