from PyQt5.QtWidgets import QTabWidget, QWidget, QGridLayout
from gui.widgets.characterOverviewWidget import CharacterOverviewWidget
from PyQt5 import QtCore

class TabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(TabWidget, self).__init__(parent)

        # Overview Tab
        self.createOverviewTab()




    def createOverviewTab(self):
        self.overviewTab = QWidget()
        self.addTab(self.overviewTab, "Overview")

        grid = QGridLayout(self.overviewTab)

        # ToDo: Hier Schleife einfügen: for each user createOverViewWidget(User)
        self.characterOverview1 = CharacterOverviewWidget(self)
        characterOverview2 = CharacterOverviewWidget(self)
        characterOverview3 = CharacterOverviewWidget(self)
        grid.addWidget(self.characterOverview1, 0, 0)
        grid.addWidget(characterOverview2, 0, 1)
        grid.addWidget(characterOverview3, 1, 0)

        self.overviewTab.setLayout(grid)

    def createCharacterTab(self):
        self.characterTab = QWidget()
        self.addTab(self.characterTab, "Character Name")

