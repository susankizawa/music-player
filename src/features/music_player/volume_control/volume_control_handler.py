from src.core.config_manager import ConfigManager

class VolumeControlHandler():
    def __init__(self, ui, audio_handler):
        self.audio_handler = audio_handler
        self.ui = ui

        self.config_manager = ConfigManager()
        config = self.config_manager.load()
        volume = config.get("volume")

        scaled_volume = volume * 1000

        self.ui.setMinimum(0)
        self.ui.setMaximum(1000)
        self.ui.setValue(scaled_volume)
        
        self.ui.sliderMoved.connect(self.on_volume_slider_moved)
        self.ui.sliderReleased.connect(self.on_volume_slider_released)

    def on_volume_slider_moved(self, value):
        normalized_value = value / 1000
        self.audio_handler.change_volume(normalized_value)

    def on_volume_slider_released(self):
        value = self.ui.value()
        normalized_value = value / 1000
        self.config_manager.update({
            "volume": normalized_value
        })