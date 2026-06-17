from re import search

from src.shared.song import Song
from src.features.library_manager.library_table.library_table_model import LibraryTableModel
from src.workers.background_task_builder import BackgroundTaskBuilder
from src.workers.library_worker import LibraryWorker
from src.workers.task_queue import TaskQueue

from PySide6.QtCore import QObject, Signal

class LibraryTableHandler(QObject):
    library_initialized = Signal(list)
    song_requested = Signal(Song)

    def __init__(self, ui, repository):
        super().__init__()
        self.ui = ui
        self.repository = repository

        self._initialized = False
        
        self.initialize_model()

        self.ui.doubleClicked.connect(self.on_item_double_clicked)
        self.repository.songsChanged.connect(self.update_model)
    
    def on_item_double_clicked(self, index):
        row = index.row()
        song = self.table_model.get_song(row)
        
        self.song_requested.emit(song)
    
    def initialize_model(self):
        self.table_model = LibraryTableModel()
        self.ui.setModel(self.table_model)
        self.update_model()
    
    def update_model(self):
        task_queue = TaskQueue()
        task_queue.enqueue(LibraryWorker("get_all_songs"),
                           self.on_songs_fetched)
    
    def on_songs_fetched(self, songs):
        self.table_model.update_data(songs)

        if self._initialized:
            return
        
        self._initialized = True
        self.library_initialized.emit(songs)
    
    def on_search_request(self, search_filter):
        if not search_filter.strip():
            songs = self.repository.get_all_songs()
        else:
            songs = self.repository.filter_songs_by_title(search_filter)

        self.table_model.update_data(songs)
    

    
    