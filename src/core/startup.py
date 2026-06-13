from src.shared.constants import MUSIC_FOLDER
from src.features.file_handler.metadata_parser import MetadataParser

def load_songs(library):
    for song_file in MUSIC_FOLDER.glob("*.mp3"):
        song = MetadataParser.song_from_file(song_file)
        library.add_song(song)