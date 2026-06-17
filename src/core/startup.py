from src.shared.constants import MUSIC_FOLDER
from src.core.metadata_parser import MetadataParser

from pathlib import Path

def startup(library_repository):
    # Logic moved to workers
    folder_files = {Path(f) for f in MUSIC_FOLDER.glob("*.mp3")}
    db_songs = library_repository.get_all_songs()
    db_files = {Path(song.file_path) for song in db_songs}
    added = folder_files - db_files
    removed = db_files - folder_files

    for song_file in added:
        song = MetadataParser.song_from_file(song_file)
        library_repository.add_song(song)
    
    for song_file in removed:
        library_repository.soft_delete_song(song_file)
