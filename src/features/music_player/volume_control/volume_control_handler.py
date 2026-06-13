from src.shared.config import Config

class VolumeControlHandler():
    def __init__(self, ui, audio_handler):
        self.audio_handler = audio_handler

        self.config = Config()

        scaled_volume = self.config.volume * 1000

        ui.setMinimum(0)
        ui.setMaximum(1000)
        ui.setValue(scaled_volume)
        
        ui.sliderMoved.connect(self.on_volume_slider_moved)

    def on_volume_slider_moved(self, value):
        normalized_value = value / 1000
        self.config.volume = normalized_value
        self.audio_handler.change_volume(normalized_value)