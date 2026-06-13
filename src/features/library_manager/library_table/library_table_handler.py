class LibraryTableHandler():
    def __init__(self, ui, audio_handler):
        self.audio_handler = audio_handler
        self.ui = ui

        self.ui.doubleClicked.connect(self.on_item_double_clicked)
    
    def on_item_double_clicked(self, index):
        row = index.row()
        song = self.ui.table_model.get_song(row)
        
        self.audio_handler.load_song(song)
        self.audio_handler.play()
    
    