from src.shared.song import Song
from src.core.config_manager import ConfigManager

from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, QObject, Signal

class AudioHandler(QObject):
    # Notes:
    # Technically a singleton, but doesn't inherit from SingletonMeta cuz it would conflict with QObject which i need to use signals

    _instance = None
    songChanged = Signal(object)
    positionChanged = Signal(int)

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_initialized'):
            return
        self._initialized = True

        super().__init__()

        config_manager = ConfigManager()
        
        self._media_player = QMediaPlayer()
        self._audio_output = QAudioOutput()
        self.current_song = None

        config = config_manager.load()
        volume = config.get("volume")

        self._media_player.setAudioOutput(self._audio_output)
        self._audio_output.setVolume(volume)

        self._media_player.positionChanged.connect(self.positionChanged.emit)

    def load_song(self, song):
        if not isinstance(song, Song):
            raise TypeError(f"Expected Song, got {type(song).__name__}")
        
        self.current_song = song
        file_path = self.current_song.file_path
        self._media_player.setSource(QUrl.fromLocalFile(file_path))
        self.songChanged.emit(song)

    def play_song(self, song):
        self.load_song(song)
        self.play()

    def play(self):
        if self.current_song:
            self._media_player.play()

    def pause(self):
        if self.current_song:
            self._media_player.pause()

    def stop(self):
        if self.current_song:
            self._media_player.stop()
    
    def change_volume(self, volume):
        self._audio_output.setVolume(volume)

    def mute(self):
        self._audio_output.setMuted(True)

    def unmute(self):
        self._audio_output.setMuted(False)
    
    @property
    def position(self):
        return self._media_player.position()
    
    @position.setter
    def position(self, value):
        value = max(0, min(value, self.duration))
        self._media_player.setPosition(value)

    @property
    def duration(self):
        return self.current_song.duration
