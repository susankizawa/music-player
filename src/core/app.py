from src.core.main_window import MainWindow
from src.shared.library import Library
from src.shared.song import Song
from src.features.music_player.audio_handler import AudioHandler
from src.features.file_handler.metadata_parser import MetadataParser
from src.core.startup import load_songs
from src.database.sql_db import create_connection, cleanup_connections
from src.repositories.library_repository import LibraryRepository

import sys
from PySide6.QtWidgets import QApplication, QPushButton, QSlider, QLabel, QFileDialog
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

class App(QApplication):
    def __init__(self):
        super().__init__()
        create_connection()
        self.audio_handler = AudioHandler()
        self.library_repository = LibraryRepository()

        load_songs(self.library_repository)

        self.view = MainWindow(self.library_repository, self.audio_handler)

        #first_song = self.library_repository.get_all_songs()[0]

        #self.audio_handler.load_song(first_song)

    def run(self):
        self.view.show()
        sys.exit(self.exec())
    
    
    
    
        