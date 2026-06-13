from src.shared.song import Song

from PySide6.QtCore import QObject, Signal
from PySide6.QtSql import QSqlQuery

class LibraryRepository(QObject):
    songsChanged = Signal()

    def _map_to_song(self, query):
        return Song(
            query.value("file_path"),
            query.value("title"),
            query.value("artist"),
            query.value("album"),
            query.value("date"),
            query.value("genre"),
            query.value("duration")
        )

    def get_song(self, file_path):
        query = QSqlQuery()
        query.prepare("""
            SELECT * FROM library WHERE file_path = :file_path AND deleted = 0
        """)
        query.bindValue(":file_path", file_path)
        if query.next():
            return self._map_to_song(query)
        return None
    
    def get_all_songs(self):
        query = QSqlQuery()
        query.exec("SELECT * FROM library WHERE deleted = 0")
        songs = []
        while query.next():
            songs.append(self._map_to_song(query))
        return songs
    
    def add_song(self, song):
        query = QSqlQuery()
        query.prepare("""
            INSERT OR REPLACE INTO library (file_path, title, artist, album, date, genre, duration, deleted)
            VALUES (:file_path, :title, :artist, :album, :date, :genre, :duration, 0)
        """)
        query.bindValue(":file_path", song.file_path)
        query.bindValue(":title", song.title)
        query.bindValue(":artist", song.artist)
        query.bindValue(":album", song.album)
        query.bindValue(":date", song.date)
        query.bindValue(":genre", song.genre)
        query.bindValue(":duration", song.duration)
        if not query.exec():
            print(f"Query error: {query.lastError().text()}")
        
        self.songsChanged.emit()

    def remove_song(self, song):
        query = QSqlQuery()
        query.prepare("""
            UPDATE library SET deleted = 1 WHERE file_path = :file_path
        """)
        query.bindValue(":file_path", song.file_path)
        query.exec()
        self.songsChanged.emit()