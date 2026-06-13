from PySide6.QtWidgets import QPushButton, QSizePolicy
from PySide6.QtGui import QIcon

class MuteToggleButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setObjectName(u"muteToggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AudioVolumeHigh))
        self.setIcon(icon)
        self.setCheckable(True)
        self.setText("")
