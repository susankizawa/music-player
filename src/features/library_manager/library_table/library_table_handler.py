class LibraryTableHandler():
    def __init__(self, ui, audio_handler, library_repository):
        self.audio_handler = audio_handler
        self.ui = ui
        self.library_repository = library_repository

        self.ui.doubleClicked.connect(self.on_item_double_clicked)
        self.library_repository.songsChanged.connect(self.on_songs_changed)
    
    def on_item_double_clicked(self, index):
        row = index.row()
        song = self.ui.table_model.get_song(row)
        
        self.audio_handler.load_song(song)
        self.audio_handler.play()
    
    def on_songs_changed(self):
        data = self.library_repository.get_all_songs()
        self.ui.table_model.update_data(data)
    