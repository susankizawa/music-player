from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex

from src.utils.time import format_time

class LibraryTableModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()

        self._data = []
        self._column_config = [
            {"header": "title", "attr": "title"},
            {"header": "artist", "attr": "artist"},
            {"header": "duration", "attr": "duration"},
        ]
    
    def rowCount(self, parent=QModelIndex()):
        return len(self._data)
    
    def columnCount(self, parent=QModelIndex()):
        return len(self._column_config)
    
    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        
        if role == Qt.DisplayRole:
            song = self._data[index.row()]
            attr_name = self._column_config[index.column()]["attr"]
            value = getattr(song, attr_name, None)

            if attr_name == "duration":
                return format_time(value)
            
            return value
        
        return None
    
    def get_song(self, row):
        return self._data[row]
    
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._column_config[section]["header"]
        return None
    
    def update_data(self, data):
        self.beginResetModel()
        self._data = data
        self.endResetModel()
        self.layoutChanged.emit()
