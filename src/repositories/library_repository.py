from src.shared.song import Song

from pathlib import Path
from PySide6.QtCore import QObject, Signal
from PySide6.QtSql import QSqlQuery, QSqlDatabase

class LibraryRepository(QObject):
    songsChanged = Signal()

    def __init__(self, db=QSqlDatabase.database()):
        self.db = db
        super().__init__()

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
        query = QSqlQuery(self.db)
        query.prepare("""
            SELECT * FROM library WHERE file_path = :file_path AND deleted = 0
        """)
        query.bindValue(":file_path", file_path)
        if query.next():
            return self._map_to_song(query)
        return None
    
    def get_all_songs(self):
        query = QSqlQuery(self.db)
        query.exec("SELECT * FROM library WHERE deleted = 0")
        songs = []
        while query.next():
            songs.append(self._map_to_song(query))
        return songs
    
    def add_song(self, song):
        query = QSqlQuery(self.db)
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

    def soft_delete_song(self, object):
        if isinstance(object, Song):
            file_path = object.file_path
        elif isinstance(object, Path) or isinstance(object, str):
            file_path = str(object)
        
        query = QSqlQuery(self.db)
        query.prepare("""
            UPDATE library SET deleted = 1 WHERE file_path = :file_path
        """)
        query.bindValue(":file_path", file_path)
        query.exec()
        self.songsChanged.emit()
    
    def filter_songs_by_title(self, filter):
        query = QSqlQuery(self.db)
        query.prepare("""
            SELECT * FROM library WHERE LOWER(title) LIKE LOWER(:filter) AND deleted = 0
        """)
        query.bindValue(":filter", f"%{filter}%")

        result = []

        if not query.exec():
            return []
        
        while query.next():
            result.append(self._map_to_song(query))

        return result