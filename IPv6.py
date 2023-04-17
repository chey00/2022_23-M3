from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QTextBrowser
from PyQt6.QtCore import Qt


class IPv6(QWidget):
    def __init__(self, parent=None):
        super(IPv6, self).__init__(parent)

        self.address = QLineEdit(self)

        # Aufgabe 1

        # Aufgabe 2

        self.subnetmask = QTextBrowser(self)
        self.hex = QTextBrowser(self)

        layout = QGridLayout(self)

        layout.addWidget(QLabel("IPv6-Adresse:"), 1, 1, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(QLabel("Subnetmask:"), 2, 1, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(QLabel("Hexadezimal:"), 3, 1, Qt.AlignmentFlag.AlignRight)

        layout.addWidget(self.address, 1, 2)
        layout.addWidget(self.subnetmask, 2, 2)
        layout.addWidget(self.hex, 3, 2)

        self.setLayout(layout)

    # Aufgabe 2
        # Aufgabe 3
