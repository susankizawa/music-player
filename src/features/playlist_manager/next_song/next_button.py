from PySide6.QtWidgets import QPushButton, QSizePolicy
from PySide6.QtGui import QIcon

class NextButton(QPushButton):
    def __init__(self):
        super().__init__()

        self.setObjectName("nextButton")

        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

        icon = QIcon.fromTheme(QIcon.ThemeIcon.MediaSkipForward)
        self.setIcon(icon)

        self.setText("")