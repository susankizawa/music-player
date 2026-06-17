from src.shared.song import Song
from src.features.playlist_manager.add_song.add_song_button import AddSongButton
from src.features.playlist_manager.next_song.next_button import NextButton
from src.features.playlist_manager.previous_song.previous_button import PreviousButton
from src.features.playlist_manager.playlist import Playlist
from src.features.playlist_manager.playlist_table.playlist_table_handler import PlaylistTableHandler
from src.features.playlist_manager.playlist_table.playlist_table_view import PlaylistTableView

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout

class PlaylistWidget(QWidget):
    song_requested = Signal(Song)

    def __init__(self, audio_handler):
        super().__init__()
        self.playlist = Playlist()

        self.playlist.song_requested.connect(self.song_requested)

        layout = QVBoxLayout(self)

        self.inner_container = QWidget()
        self.inner_container.setContentsMargins(0,0,0,0)
        inner_layout = QHBoxLayout(self.inner_container)
        layout.addWidget(self.inner_container)

        self.add_song_button = AddSongButton()
        self.add_song_button.clicked.connect(lambda: self.playlist.add_song(audio_handler.current_song))
        inner_layout.addWidget(self.add_song_button)

        self.previous_button = PreviousButton()
        self.previous_button.clicked.connect(self.playlist.prev_song)
        inner_layout.addWidget(self.previous_button)

        self.next_button = NextButton()
        self.next_button.clicked.connect(self.playlist.next_song)
        inner_layout.addWidget(self.next_button)

        inner_layout.addStretch()

        self.playlist_table_view = PlaylistTableView()
        self.playlist_table_handler = PlaylistTableHandler(self.playlist_table_view, self.playlist)
        layout.addWidget(self.playlist_table_view)


