from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSlider

class VolumeSlider(QSlider):
    def __init__(self):
        super().__init__()

        self.setObjectName(u"volumeSlider")
        self.setMaximum(1000)
        self.setSingleStep(1)
        self.setOrientation(Qt.Orientation.Horizontal)