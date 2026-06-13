from PySide6.QtWidgets import QPushButton, QSizePolicy
from PySide6.QtGui import QIcon

class PlayPauseButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setObjectName(u"playbackButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        self.setIcon(icon)
        self.setCheckable(True)
        self.setText("")