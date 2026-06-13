from src.shared.constants import MUSIC_FOLDER

import subprocess
import platform
from pathlib import Path

class OpenMusicFolderHandler():
    def __init__(self, ui):
        ui.clicked.connect(self.on_music_folder_button_clicked)

    def on_music_folder_button_clicked(self):
        folder = Path(MUSIC_FOLDER)
        if platform.system() == "Windows":
            subprocess.run(["explorer", folder])
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["open", folder])
        else:  # Linux
            subprocess.run(["xdg-open", folder])
