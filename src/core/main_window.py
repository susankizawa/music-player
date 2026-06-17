from src.features.library_manager.search.search_handler import SearchHandler
from src.features.library_manager.search.search_bar import SearchBar
from src.features.file_handler.import_song.import_song_button import ImportSongButton
from src.features.file_handler.import_song.import_song_handler import ImportSongHandler
from src.features.file_handler.open_music_folder.open_music_folder_button import OpenMusicFolderButton
from src.features.file_handler.open_music_folder.open_music_folder_handler import OpenMusicFolderHandler

from src.features.library_manager.library_table.library_table_handler import LibraryTableHandler
from src.features.library_manager.library_table.library_table_view import LibraryTableView
from src.features.music_player.player_bar import PlayerBar

from src.core.session_manager import SessionManager
from src.core.config_manager import ConfigManager

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self, library_repository, audio_handler):
        super().__init__()
        self.audio_handler = audio_handler

        self.setWindowTitle("Tocador de Música")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        self.inner_container1 = QWidget()
        inner_layout1 = QHBoxLayout(self.inner_container1)
        inner_layout1.setContentsMargins(0,0,0,0)
        layout.addWidget(self.inner_container1)

        inner_layout1.addStretch()

        self.open_music_folder_button = OpenMusicFolderButton()
        self.open_music_folder_handler = OpenMusicFolderHandler(self.open_music_folder_button)
        inner_layout1.addWidget(self.open_music_folder_button, alignment=Qt.AlignLeft)

        self.import_song_button = ImportSongButton()
        self.import_song_handler = ImportSongHandler(self.import_song_button, library_repository)
        inner_layout1.addWidget(self.import_song_button, alignment=Qt.AlignLeft)
        
        layout.addSpacing(10)

        self.search_bar = SearchBar()
        self.search_handler = SearchHandler(self.search_bar)
        layout.addWidget(self.search_bar)

        layout.addSpacing(10)

        self.library_table_view = LibraryTableView()
        self.library_table_handler = LibraryTableHandler(self.library_table_view, library_repository)
        self.library_table_handler.library_initialized.connect(self.load_first_song)
        self.library_table_handler.song_requested.connect(audio_handler.play_song)
        self.search_handler.search_requested.connect(self.library_table_handler.on_search_request)
        layout.addWidget(self.library_table_view)

        self.player_bar = PlayerBar(audio_handler)
        self.player_bar.setContentsMargins(0,0,0,0)
        layout.addWidget(self.player_bar,
                         stretch=0)

        self.setCentralWidget(central_widget)
    
    def load_first_song(self, songs):
        if songs:
            session_manager = SessionManager()
            session = session_manager.load()
            first_song_file_path = session.get("current_song")
            position = session.get("position", 0)
            print(position)
            if first_song_file_path:
                first_song = next((s for s in songs if s.file_path == first_song_file_path), None)
            else:
                first_song = songs[0]
            self.audio_handler.load_song(first_song)
            self.audio_handler.play()
    
    def closeEvent(self, event):
        session_manager = SessionManager()

        session_manager.update({
            "current_song": self.audio_handler.current_song.file_path
        })
        session_manager.save()

        event.accept()
