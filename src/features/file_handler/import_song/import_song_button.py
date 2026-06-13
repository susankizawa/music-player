from PySide6.QtWidgets import QPushButton, QSizePolicy

class ImportSongButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setObjectName(u"importSongButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setText("Import song")