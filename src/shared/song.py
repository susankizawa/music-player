from src.utils.time import format_time

class Song:
    def __init__(self, file_path, title, artist, album, date, genre, duration):
        self._file_path = file_path
        self.title = title
        self.artist = artist
        self.album = album
        self.date = date
        self.genre = genre
        self.duration = duration

    @property
    def file_path(self):
        return self._file_path

    def __str__(self):
        return (
            f"title: {self.title}\n"
            f"artist: {self.artist}\n"
            f"album: {self.album}\n"
            f"date: {self.date}\n"
            f"genre: {self.genre}\n"
            f"duration: {format_time(self.duration)}\n"
            f"file_path: {self._file_path}\n"
        )

    