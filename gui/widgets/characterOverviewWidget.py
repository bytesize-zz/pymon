from PyQt5.QtWidgets import QWidget, QSizePolicy, QLabel
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPalette


class CharacterOverviewWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setAutoFillBackground(True)

        pal = QPalette()
        pal.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(pal)

        self.set_size_policy()


    def set_size_policy(self):
        self.setMaximumSize(320,120)
        self.setMinimumSize(320, 120)
