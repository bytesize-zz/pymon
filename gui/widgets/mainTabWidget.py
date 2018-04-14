from PyQt5.QtWidgets import QTabWidget, QWidget, QGridLayout, QScrollArea
from gui.widgets.characterOverviewWidget import CharacterOverviewWidget
from gui.widgets.characterTabWidget import CharacterTabWidget
from PyQt5 import QtCore

# Database Imports
from db.databaseTables import User
from db.databaseHandler import DatabaseHandler
import threading

class MainTabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(MainTabWidget, self).__init__(parent)
        self.parent = parent
        self.dbHandler = DatabaseHandler()  # ToDo: Dangerous to start an own instance of dbHandler?

        try:
            userList = self.dbHandler.getAllUser()
        except Exception as e:
            print(e)

        # Overview Tab
        self.createOverviewTab(userList)
        self.createCharacterTabs(userList)

    def createOverviewTab(self, userList):

        self.overviewTab = QWidget()
        #self.addTab(self.overviewTab, "Overview")
        grid = QGridLayout(self.overviewTab)

        scrollArea = QScrollArea()
        scrollArea.setWidget(self.overviewTab)

        x = 0
        y = 0
        self.widgetList = []
        for user in userList:
            newWidget = CharacterOverviewWidget(user)
            self.widgetList.append(newWidget)
            grid.addWidget(newWidget, x, y)

            # ToDo: Find a proper Way to print these widgets relative to mainwindow size
            # after adding a widget we need to prepare the next coordinates
            if (y == 0): y = y+1
            elif ( y == 1 ):
                x = x+1
                y = y-1
            elif(y > 1): y = 0

        scrollArea.setLayout(grid)
        self.addTab(scrollArea, "Overview")


        #self.overviewTab.setLayout(grid)

    def repaintOverviewTab(self):
        self.createOverviewTab()


    def createCharacterTabs(self, userList):

        for user in userList:
            characterTab = CharacterTabWidget(user)
            self.addTab(characterTab, user.CharacterName)


