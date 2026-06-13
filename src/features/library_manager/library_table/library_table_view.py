from src.features.library_manager.library_table.library_table_model import LibraryTableModel

from PySide6.QtWidgets import QTableView, QHeaderView

class LibraryTableView(QTableView):
    def __init__(self, data_source=None):
        super().__init__()

        self.table_model = LibraryTableModel(data_source or [])
        self.setModel(self.table_model)

        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setSelectionBehavior(QTableView.SelectRows)
        self.setShowGrid(True)
        self.setAlternatingRowColors(True)
