from PyQt5.QtWidgets import QTabWidget, QWidget, QFrame, QGridLayout, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize, QRect

from gui.widgets.characterOverviewWidget import CharacterOverviewWidget

class TabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(TabWidget, self).__init__(parent)

        # Overview Tab
        self.createOverviewTab()


    def createOverviewTab(self):
        self.overviewTab = QWidget()
        self.addTab(self.overviewTab, "Overview")

        grid = QGridLayout(self.overviewTab)

        # Hier Schleife einfügen: for each user createOverViewWidget(User)
        characterOverview1 = CharacterOverviewWidget(self)
        button2 = QPushButton("name2")
        grid.addWidget(characterOverview1, 0, 0)
        grid.addWidget(characterOverview1, 0, 1)
        grid.addWidget(button2, 0, 2)

        self.overviewTab.setLayout(grid)

    def createCharacterTab(self):
        self.characterTab = QWidget()
        self.addTab(self.characterTab, "Character Name")