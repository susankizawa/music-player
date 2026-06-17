from src.shared.constants import MUSIC_FOLDER

from PySide6.QtCore import QFileSystemWatcher

class LibraryWatcher(QFileSystemWatcher):
    def __init__(self, synchronizer):
        super().__init__()
        self.addPath(str(MUSIC_FOLDER))
        self.directoryChanged.connect(synchronizer.sync_incrementally)