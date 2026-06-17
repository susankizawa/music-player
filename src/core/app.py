from src.shared.constants import PATHS
from src.core.config_manager import ConfigManager
from src.core.session_manager import SessionManager
from src.features.library_manager.sync_library import SyncLibrary
from src.core.main_window import MainWindow
from src.shared.library import Library
from src.shared.song import Song
from src.features.music_player.audio_handler import AudioHandler
from src.core.metadata_parser import MetadataParser
from src.database.sql_db import create_connection
from src.repositories.library_repository import LibraryRepository
from src.core.library_watcher import LibraryWatcher
from src.workers.background_task_builder import BackgroundTaskBuilder
from src.workers.library_worker import LibraryWorker
from src.workers.task_queue import TaskQueue

import sys
from PySide6.QtWidgets import QApplication, QPushButton, QSlider, QLabel, QFileDialog
from PySide6.QtCore import QFile, QThread
from PySide6.QtUiTools import QUiLoader

class App(QApplication):
    def __init__(self):
        super().__init__()
        self.db = create_connection("main")
        self.audio_handler = AudioHandler()
        self.library_repository = LibraryRepository(self.db)
        self.sync_library = SyncLibrary(self.library_repository)
        self.library_watcher = LibraryWatcher(self.sync_library)
        self.task_queue = TaskQueue()

        self.config_manager = ConfigManager()
        self.session_manager = SessionManager()

        if not PATHS["config"].exists():
            self.config_manager.save()

        self.view = MainWindow(self.library_repository, self.audio_handler)

        print(f"main thread: {hex(id(QThread.currentThread()))}")

        self.sync_library.sync_fully()

    def run(self):
        self.view.show()
        sys.exit(self.exec())

    
    
    
    
        