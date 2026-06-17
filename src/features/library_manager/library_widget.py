from src.shared.song import Song
from src.features.library_manager.search.search_bar import SearchBar
from src.features.library_manager.search.search_handler import SearchHandler
from src.features.library_manager.library_table.library_table_view import LibraryTableView
from src.features.library_manager.library_table.library_table_handler import LibraryTableHandler

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout

class LibraryWidget(QWidget):
    library_initialized = Signal(list)
    song_requested = Signal(Song)

    def __init__(self, repository):
        super().__init__()

        layout = QVBoxLayout(self)

        layout.addSpacing(10)

        self.search_bar = SearchBar()
        self.search_handler = SearchHandler(self.search_bar)
        layout.addWidget(self.search_bar)

        layout.addSpacing(10)

        self.library_table_view = LibraryTableView()
        self.library_table_handler = LibraryTableHandler(self.library_table_view, repository)
        self.library_table_handler.library_initialized.connect(self.library_initialized)
        self.library_table_handler.song_requested.connect(self.song_requested)
        self.search_handler.search_requested.connect(self.library_table_handler.on_search_request)
        layout.addWidget(self.library_table_view)