from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QSlider, QLabel

class SeekWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QHBoxLayout(self)

        self.seekBar = QSlider()
        self.seekBar.setObjectName(u"seekBar")
        self.seekBar.setOrientation(Qt.Orientation.Horizontal)
        layout.addWidget(self.seekBar)

        self.durationLabel = QLabel()
        self.durationLabel.setObjectName(u"durationLabel")
        self.durationLabel.setText(u"0:00/00")
        layout.addWidget(self.durationLabel)