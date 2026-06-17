from src.core.config_manager import ConfigManager

class MuteToggleHandler():
    def __init__(self, ui, audio_handler):
        self.audio_handler = audio_handler
        ui.toggled.connect(lambda toggled: self.on_mute_toggle_button_toggled(toggled))
    
    def on_mute_toggle_button_toggled(self, toggled):
        config_manager = ConfigManager()

        if toggled:
            self.audio_handler.mute()
        else:
            self.audio_handler.unmute()
        
        config_manager.update({ "mute": toggled })
        config_manager.save()