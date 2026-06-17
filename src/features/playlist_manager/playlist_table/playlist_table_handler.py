from src.shared.song import Song
from src.features.playlist_manager.playlist_table.playlist_table_model import PlaylistTableModel

from PySide6.QtCore import QObject, Signal

class PlaylistTableHandler(QObject):
    song_requested = Signal(Song)

    def __init__(self, ui, playlist):
        super().__init__()
        self.ui = ui
        self.playlist = playlist
        
        self.initialize_model()

        self.ui.doubleClicked.connect(self.on_item_double_clicked)
        self.playlist.playlist_changed.connect(self.update_model)
    
    def on_item_double_clicked(self, index):
        row = index.row()
        song = self.table_model.get_song(row)
        self.playlist.current_index = row
        
        self.song_requested.emit(song)
    
    def initialize_model(self):
        self.table_model = PlaylistTableModel()
        self.ui.setModel(self.table_model)
        self.update_model([])
    
    def update_model(self, songs):
        self.table_model.update_data(songs)
    

    
    