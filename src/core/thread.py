from src.core.startup import load_songs

from PySide6.QtCore import QThread, Signal, QObject

class LoadSongsWorker(QObject):
    finished = Signal()
    
    def __init__(self, repository):
        super().__init__()
        self.repository = repository
    
    def run(self):
        load_songs(self.repository) 
        self.finished.emit()