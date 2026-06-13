from src.shared.constants import MUSIC_FOLDER
from src.features.file_handler.metadata_parser import MetadataParser

from PySide6.QtWidgets import QFileDialog
import shutil
from pathlib import Path

class ImportSongHandler:
    def __init__(self, ui, library):
        self.ui = ui
        self.library = library

        ui.clicked.connect(self.on_import_song_button_clicked)

    def on_import_song_button_clicked(self):
        file_paths, _ = QFileDialog.getOpenFileNames(
            self.ui,
            "Adicionar Música ao Player",
            "",
            "Arquivos de Áudio (*.mp3 *.wav *.flac *.ogg *.m4a);;Todos os Arquivos (*)"
        )

        if file_paths:
            for file_path in file_paths:
                new_file_path = Path(MUSIC_FOLDER) / Path(file_path).name
                shutil.copy2(file_path, new_file_path)
                new_song = MetadataParser.song_from_file(new_file_path)
                self.library.add_song(new_song)
            

