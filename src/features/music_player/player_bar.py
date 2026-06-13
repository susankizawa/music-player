from src.features.music_player.play_pause.play_pause_button import PlayPauseButton
from src.features.music_player.play_pause.play_pause_handler import PlayPauseHandler
from src.features.music_player.seek.seek_widget import SeekWidget
from src.features.music_player.seek.seek_handler import SeekHandler
from src.features.music_player.mute_toggle.mute_toggle_button import MuteToggleButton
from src.features.music_player.mute_toggle.mute_toggle_handler import MuteToggleHandler
from src.features.music_player.volume_control.volume_slider import VolumeSlider
from src.features.music_player.volume_control.volume_control_handler import VolumeControlHandler
from src.features.music_player.song_info.song_info_widget import SongInfoWidget
from src.features.music_player.song_info.song_info_handler import SongInfoHandler

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout

class PlayerBar(QWidget):
    def __init__(self, audio_handler):
        super().__init__()

        layout = QHBoxLayout(self)

        self.song_info_widget = SongInfoWidget()
        self.song_info_handler = SongInfoHandler(self.song_info_widget, audio_handler)
        self.song_info_widget.setMinimumWidth(200)
        self.song_info_widget.setMaximumWidth(325)
        layout.addWidget(self.song_info_widget,
                         stretch=1)

        self.playback_container = QWidget()
        playback_layout = QVBoxLayout(self.playback_container)
        self.playback_container.setMinimumWidth(400)
        layout.addWidget(self.playback_container,
                         stretch=2)

        self.play_pause_button = PlayPauseButton()
        self.play_pause_handler = PlayPauseHandler(self.play_pause_button, audio_handler)
        playback_layout.addWidget(self.play_pause_button, 
                                  alignment=Qt.AlignCenter)

        self.seek_widget = SeekWidget()
        self.seek_handler = SeekHandler(self.seek_widget, audio_handler)
        playback_layout.addWidget(self.seek_widget)

        self.volume_container = QWidget()
        volume_layout = QHBoxLayout(self.volume_container)
        self.volume_container.setMinimumWidth(100)
        self.volume_container.setMaximumWidth(175)
        layout.addWidget(self.volume_container,
                         stretch=1)

        self.mute_button = MuteToggleButton()
        self.mute_handler = MuteToggleHandler(self.mute_button, audio_handler)
        volume_layout.addWidget(self.mute_button, 
                                alignment=Qt.AlignCenter)

        self.volume_slider = VolumeSlider()
        self.volume_control_handler = VolumeControlHandler(self.volume_slider, audio_handler)
        self.volume_slider.setMinimumWidth(50)
        volume_layout.addWidget(self.volume_slider)




