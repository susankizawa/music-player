from src.shared.singleton import SingletonMeta

from PySide6.QtCore import QObject, Signal

class Library(QObject):
    # Notes:
    # Technically a singleton, but doesn't inherit from SingletonMeta cuz it would conflict with QObject which i need to use signals

    _instance = None
    songsChanged = Signal(object)

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, songs=None):
        if hasattr(self, '_initialized'):
            return
        self._initialized = True

        super().__init__()

        self._songs = songs if songs is not None else []

    @property
    def songs(self):
        return tuple(self._songs)

    @property
    def length(self):
        return len(self._songs)
    
    def add_song(self, song):
        self._songs.append(song)
        self.songsChanged.emit(self.songs)
    
    def remove_song(self, song):
        song_idx = self._songs.index(song)
        self.songsChanged.emit(self.songs)
        return self._songs.pop(song_idx)

    # maybe replace for database id later
    def get_song(self, file_path):
        return next((song for song in self._songs if song.file_path == file_path), None)
    
    def __str__(self):
        return '\n'.join(str(song) for song in self._songs)