from src.utils.time import format_time

class SeekHandler():
    def __init__(self, ui, audio_handler):
        self.ui = ui
        self.audio_handler = audio_handler

        self.repositioning = False

        self.ui.seekBar.setMinimum(0)
        self.ui.seekBar.setMaximum(1)
        self.ui.seekBar.setValue(0)

        self.audio_handler.songChanged.connect(self.on_song_changed)
        self.audio_handler.positionChanged.connect(self.update_ui)
        self.ui.seekBar.sliderPressed.connect(self.on_seek_bar_pressed)
        self.ui.seekBar.sliderReleased.connect(self.on_seek_bar_released)
        self.ui.seekBar.valueChanged.connect(self.on_seek_bar_value_changed)
    
    def update_ui(self, value):
        if not self.repositioning:
            self.ui.seekBar.setValue(value)
    
    def on_song_changed(self, song):
        self.ui.seekBar.setMinimum(0)
        self.ui.seekBar.setMaximum(song.duration)
        self.ui.seekBar.setValue(0)
        self.ui.durationLabel.setText(f'{format_time(0)}/{format_time(song.duration)}')
    
    def on_seek_bar_pressed(self):
        self.repositioning = True
    
    def on_seek_bar_released(self):
        self.repositioning = False
        self.audio_handler.position = self.ui.seekBar.value()
    
    def on_seek_bar_value_changed(self, value):
        duration = self.audio_handler.duration
        self.ui.durationLabel.setText(f'{format_time(value)}/{format_time(duration)}')
    

    

