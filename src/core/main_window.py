from src.features.file_handler.import_song.import_song_button import ImportSongButton
from src.features.file_handler.import_song.import_song_handler import ImportSongHandler
from src.features.file_handler.open_music_folder.open_music_folder_button import OpenMusicFolderButton
from src.features.file_handler.open_music_folder.open_music_folder_handler import OpenMusicFolderHandler

from src.features.library_manager.library_table.library_table_handler import LibraryTableHandler
from src.features.library_manager.library_table.library_table_view import LibraryTableView
from src.features.music_player.player_bar import PlayerBar

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTableWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self, library_repository, audio_handler):
        super().__init__()

        self.setWindowTitle("Tocador de Música")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        self.open_music_folder_button = OpenMusicFolderButton()
        self.open_music_folder_handler = OpenMusicFolderHandler(self.open_music_folder_button)
        layout.addWidget(self.open_music_folder_button, alignment=Qt.AlignLeft)

        self.import_song_button = ImportSongButton()
        self.import_song_handler = ImportSongHandler(self.import_song_button, library_repository)
        layout.addWidget(self.import_song_button, alignment=Qt.AlignLeft)
        
        self.library_table_view = LibraryTableView(library_repository.get_all_songs())
        self.library_table_handler = LibraryTableHandler(self.library_table_view, audio_handler, library_repository)
        layout.addWidget(self.library_table_view)

        self.player_bar = PlayerBar(audio_handler)
        layout.addWidget(self.player_bar,
                         stretch=0)

        self.setCentralWidget(central_widget)