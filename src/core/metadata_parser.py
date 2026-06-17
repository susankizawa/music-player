from pathlib import Path

from mutagen import MutagenError, File
from mutagen.easyid3 import EasyID3

from src.core.exceptions import CorruptedFileError, UnsupportedFileTypeError
from src.shared.constants import ROOT
from src.shared.song import Song

class MetadataParser:
    @staticmethod
    def song_from_file(file_path):
        file = Path(file_path)

        try:
            MetadataParser.validate_audio_file(file)
            audio_file = File(str(file))

            if audio_file is None:
                raise ValueError(f"Unsupported Format: Mutagen could not identify {file.name}")
        
        except MutagenError as e:
            raise CorruptedFileError(f"Corrupted or invalid media data in {file.name}") from e
        except (OSError, PermissionError) as e:
            raise e
        
        metadata_tags = EasyID3(file)

        song = Song(
            str(file),
            metadata_tags.get("title", [file.stem])[0],
            metadata_tags.get("artist", [""])[0],
            metadata_tags.get("album", [""])[0],
            metadata_tags.get("date", [""])[0],
            metadata_tags.get("genre", [""])[0],
            audio_file.info.length * 1000,
        )

        return song

    @staticmethod
    def validate_audio_file(file):
        if not file.exists():
            raise FileNotFoundError(f"{file.name} doesn't exist")

        if not file.is_file():
            raise IsADirectoryError(f"'{file.name}' isn't a file")

        if file.stat().st_size == 0:
            raise ValueError(f"The file '{file.name}' is empty")

        if file.suffix.lower() not in [".mp3", ".wav", ".ogg"]:
            raise UnsupportedFileTypeError(f"{file.suffix} files are not supported")

        
        
