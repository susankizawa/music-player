from PySide6.QtWidgets import QTableView, QHeaderView

class LibraryTableView(QTableView):
    def __init__(self):
        super().__init__()
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setSelectionBehavior(QTableView.SelectRows)
        self.setShowGrid(True)
        self.setAlternatingRowColors(True)
