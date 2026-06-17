from src.features.library_manager.library_table.library_table_view import LibraryTableView
from src.features.library_manager.library_table.library_table_handler import LibraryTableHandler

class LibraryTable:
    def __init__(self,audio_handler, repository):
        self.view = LibraryTableView()
        self.handler = LibraryTableHandler(self.view, audio_handler, repository)