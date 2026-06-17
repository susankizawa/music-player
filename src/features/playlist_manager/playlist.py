from src.shared.song import Song

from PySide6.QtCore import QObject, Signal

class Playlist(QObject):
    song_requested = Signal(Song)
    playlist_changed = Signal(list)

    def __init__(self):
        super().__init__()
        self.playlist = []
        self.current_index = 0
    
    def add_song(self, song):
        self.playlist.append(song)
        self.playlist_changed.emit(self.playlist)

    def remove_song(self, song):
        if song in self.playlist:
            idx = self.playlist.index(song)
            self.playlist.remove(song)

            if idx <= self.current_index:
                self.current_index = max(0, self.current_index - 1)
            
            self.playlist_changed.emit(self.playlist)
    
    def play_current(self):
        if not self.playlist:
            return

        song = self.playlist[self.current_index]
        self.song_requested.emit(song)
    
    def next_song(self):
        if self.current_index + 1 < len(self.playlist):
            self.current_index += 1
            self.play_current()
    
    def prev_song(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.play_current()