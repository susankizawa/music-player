class SongInfoHandler:
    def __init__(self, ui, audio_handler):
        self.ui = ui

        audio_handler.songChanged.connect(self.on_song_changed)
    
    def on_song_changed(self, song):
        self.ui.full_title = song.title
        self.ui.full_artist_name = song.artist
        self.ui.update_labels()