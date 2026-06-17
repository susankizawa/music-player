from PySide6.QtWidgets import QPushButton, QSizePolicy
from PySide6.QtGui import QIcon

class RemoveSong(QPushButton):
    def __init__(self):
        super().__init__()

        self.setObjectName("removeSongButton")

        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.setSizePolicy(sizePolicy)

        icon = QIcon.fromTheme(QIcon.ThemeIcon.ListRemove)
        self.setIcon(icon)

        self.setText("")