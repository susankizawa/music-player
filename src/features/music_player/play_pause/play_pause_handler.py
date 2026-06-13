class PlayPauseHandler():
    def __init__(self, ui, audio_handler):
        self.audio_handler = audio_handler
        ui.toggled.connect(lambda toggled: self.on_play_pause_button_toggled(toggled))
    
    def on_play_pause_button_toggled(self, toggled):
        if toggled:
            self.audio_handler.play()
        else:
            self.audio_handler.pause()