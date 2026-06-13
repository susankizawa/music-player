from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QFont

class SongInfoWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.full_title = "Song Title"
        self.full_artist_name = "Artist Name"

        self.songTitleLabel = QLabel()
        self.songTitleLabel.setObjectName(u"songTitleLabel")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.songTitleLabel.setFont(font)
        self.songTitleLabel.setText(self.full_title)
        layout.addWidget(self.songTitleLabel)

        self.songArtistLabel = QLabel()
        self.songArtistLabel.setObjectName(u"songArtistLabel")
        self.songArtistLabel.setText(self.full_artist_name)
        layout.addWidget(self.songArtistLabel)
    
    def update_labels(self):
        title_metrics = self.songTitleLabel.fontMetrics()
        elided_title = title_metrics.elidedText(self.full_title, Qt.ElideRight, self.songTitleLabel.width())
        self.songTitleLabel.setText(elided_title)

        artist_name_metrics = self.songArtistLabel.fontMetrics()
        elided_artist_name = artist_name_metrics.elidedText(self.full_artist_name, Qt.ElideRight, self.songArtistLabel.width())
        self.songArtistLabel.setText(elided_artist_name)

        self.songArtistLabel.setVisible(bool(self.full_artist_name))
    
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_labels()

    
    