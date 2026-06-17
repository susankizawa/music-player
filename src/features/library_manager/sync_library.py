from src.core.metadata_parser import MetadataParser
from src.shared.constants import MUSIC_FOLDER

from pathlib import Path

class SyncLibrary:
    def __init__(self, repository):
        self.repository = repository
        self._snapshot = set(MUSIC_FOLDER.glob("*.mp3"))
    
    def sync(self, previous, current):
        added = current - previous
        removed = previous - current

        for song_file in added:
            song = MetadataParser.song_from_file(song_file)
            self.repository.add_song(song)
        
        for song_file in removed:
            self.repository.soft_delete_song(song_file)
    
    def sync_incrementally(self):
        current = set(MUSIC_FOLDER.glob("*.mp3"))

        self.sync(self._snapshot, current)

        self._snapshot = current

    def sync_fully(self):
        current = set(MUSIC_FOLDER.glob("*.mp3"))
        db_songs = self.repository.get_all_songs()
        previous = { Path(song.file_path) for song in db_songs }

        self.sync(previous, current)

        self._snapshot = current