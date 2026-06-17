from PySide6.QtWidgets import (
    QWidget,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QSizePolicy
)

class SearchBar(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("searchBar")

        # --- input ---
        self.search_input = QLineEdit()
        self.search_input.setObjectName("searchInput")
        self.search_input.setPlaceholderText("Search songs...")

        size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.search_input.setSizePolicy(size_policy)

        # --- button ---
        self.search_button = QPushButton("Search")
        self.search_button.setObjectName("searchButton")

        button_policy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.search_button.setSizePolicy(button_policy)

        # --- layout ---
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)

        layout.addWidget(self.search_input)
        layout.addWidget(self.search_button)

        self.setLayout(layout)