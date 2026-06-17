from PySide6.QtCore import QObject, Signal

class SearchHandler(QObject):
    search_requested = Signal(str)
    
    def __init__(self, ui):
        super().__init__()
        self.ui = ui

        ui.search_input.returnPressed.connect(self.on_search_button_pressed)
        ui.search_button.clicked.connect(self.on_search_button_pressed)

    def on_search_button_pressed(self):
        search_filter = self.ui.search_input.text()
        self.search_requested.emit(search_filter)