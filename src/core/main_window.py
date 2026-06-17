
from src.features.library_manager.search.search_handler import SearchHandler
from src.features.library_manager.search.search_bar import SearchBar
from src.features.file_handler.import_song.import_song_button import ImportSongButton
from src.features.file_handler.import_song.import_song_handler import ImportSongHandler
from src.features.file_handler.open_music_folder.open_music_folder_button import OpenMusicFolderButton
from src.features.file_handler.open_music_folder.open_music_folder_handler import OpenMusicFolderHandler
from src.features.music_player.player_bar import PlayerBar
from src.features.library_manager.library_widget import LibraryWidget
from src.features.playlist_manager.playlist_widget import PlaylistWidget

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

        self.inner_container2 = QWidget()
        inner_layout2 = QHBoxLayout(self.inner_container2)
        inner_layout2.setContentsMargins(0,0,0,0)
        layout.addWidget(self.inner_container2)

        self.library_widget = LibraryWidget(library_repository)
        self.library_widget.library_initialized.connect(self.load_first_song)
        self.library_widget.song_requested.connect(lambda song: self.audio_handler.play_song(song))
        inner_layout2.addWidget(self.library_widget, stretch=2)

        self.playlist_widget = PlaylistWidget(audio_handler)
        self.playlist_widget.song_requested.connect(lambda song: self.audio_handler.play_song(song))
        inner_layout2.addWidget(self.playlist_widget, stretch=1)

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
