from PyQt5.QtWidgets import QTabWidget, QWidget, QGridLayout
from gui.widgets.characterOverviewWidget import CharacterOverviewWidget
from PyQt5 import QtCore

# Database Imports
from db.databaseTables import User
from db.databaseHandler import DatabaseHandler

class TabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(TabWidget, self).__init__(parent)

        self.dbHandler = DatabaseHandler()

        # Overview Tab
        self.createOverviewTab()

    def createOverviewTab(self):
        self.overviewTab = QWidget()
        self.addTab(self.overviewTab, "Overview")

        grid = QGridLayout(self.overviewTab)

        userList = self.dbHandler.getAllUser()

        x = 0
        y = 0
        self.widgetList = []
        for user in userList:
            newWidget = CharacterOverviewWidget(user)
            self.widgetList.append(newWidget)
            grid.addWidget(newWidget, x, y)

            # after adding a widget we need to prepare the next coordinates
            if (x == y): y = y+1
            elif ( y > x ): x = x+1


        # ToDo: Hier Schleife einfügen: for each user createOverViewWidget(User)
        #self.characterOverview1 = CharacterOverviewWidget(self)
        #characterOverview2 = CharacterOverviewWidget(self)
        #characterOverview3 = CharacterOverviewWidget(self)
        #grid.addWidget(self.characterOverview1, 0, 0)
        #grid.addWidget(characterOverview2, 0, 1)
        #grid.addWidget(characterOverview3, 1, 0)

        self.overviewTab.setLayout(grid)

    def repaintOverviewTab(self):
        print("x")
        #print(self.widgetList)

    def createCharacterTab(self):
        self.characterTab = QWidget()
        self.addTab(self.characterTab, "Character Name")

