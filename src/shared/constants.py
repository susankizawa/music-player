from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MUSIC_FOLDER = ROOT / "music"
DATA_FOLDER = ROOT / "data"

PATHS = {
    "music_folder": ROOT / "music",
    "data_folder": ROOT / "data",
    "config": ROOT / "data" / "config.json",
    "session": ROOT / "data" / "session.json",
}

DEFAULT_CONFIG = {
    "mute": False,
    "volume": 1.0,
}

DEFAULT_SESSION = {
    "current_song": None,
}