from PyQt5.QtWidgets import QTabWidget, QWidget, QGridLayout
from gui.widgets.characterOverviewWidget import CharacterOverviewWidget
from PyQt5 import QtCore

# Database Imports
from db.databaseTables import User
from db.databaseHandler import DatabaseHandler

class TabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(TabWidget, self).__init__(parent)
        self.parent = parent

        # Overview Tab
        self.createOverviewTab()


    def createOverviewTab(self):
        dbHandler = DatabaseHandler()  # ToDo: Dangerous to start an own instance of dbHandler?

        self.overviewTab = QWidget()
        self.addTab(self.overviewTab, "Overview")

        grid = QGridLayout(self.overviewTab)

        try:
            userList = dbHandler.getAllUser()
            dbHandler.close()
        except Exception as e:
            print(e)



        x = 0
        y = 0
        self.widgetList = []
        for user in userList:
            print(user)
            newWidget = CharacterOverviewWidget(user)
            self.widgetList.append(newWidget)
            grid.addWidget(newWidget, x, y)

            # ToDo: Find a proper Way to print these widgets, maybe QHBox+ QVBox Layout
            # after adding a widget we need to prepare the next coordinates
            if (y == 0): y = y+1
            elif ( y == 1 ):
                x = x+1
                y = y-1
            elif(y > 1): y = 0

        self.overviewTab.setLayout(grid)

    def repaintOverviewTab(self):
        #print("x")
        self.createOverviewTab()


    def createCharacterTab(self):
        self.characterTab = QWidget()
        self.addTab(self.characterTab, "Character Name")

