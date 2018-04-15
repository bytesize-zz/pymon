from PyQt5.QtWidgets import QTabWidget, QWidget, QGridLayout, QScrollArea, QVBoxLayout
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

        self.initiateLayout()

        try:
            userList = self.dbHandler.getAllUser()
            # Overview Tab
            self.createOverviewTab(userList)
            self.createCharacterTabs(userList)
        except Exception as e:
            print("Exception in MainTabWidget init: " + str(e))



    def initiateLayout(self):
        '''
            box is a Layout needed to Stretch the scrollArea
            scrollArea is needed to add the Scrollbar
            scrollContent is needed to display the scrollable Items inside the scrollArea
            scrollLayout is needed to stretch the Items inside scrollContent

        '''

        box = QVBoxLayout(self)
        box.setContentsMargins(0,0,0,0)
        box.setSpacing(0)

        self.setLayout(box)
        self.scrollArea = QScrollArea(self)
        box.addWidget(self.scrollArea)
        self.scrollArea.setWidgetResizable(True)
        self.scrollContent = QWidget(self.scrollArea)
        self.scrollLayout = QGridLayout(self.scrollContent)
        self.scrollLayout.setContentsMargins(2,2,2,2)
        self.scrollLayout.setSpacing(4)
        #self.scrollLayout.setAlignment(QtCore.Qt.AlignTop)
        self.scrollContent.setLayout(self.scrollLayout)

    def createOverviewTab(self, userList):

        self.overviewTab = QWidget()

        x = 0
        y = 0
        self.widgetList = []
        for user in userList:
            newWidget = CharacterOverviewWidget(user)
            self.widgetList.append(newWidget)
            self.scrollLayout.addWidget(newWidget, x, y)

            # ToDo: Find a proper Way to print these widgets relative to mainwindow size
            # after adding a widget we need to prepare the next coordinates
            if (y == 0): y = y+1
            elif ( y == 1 ):
                x = x+1
                y = y-1
            elif(y > 1): y = 0

        self.addTab(self.scrollArea, "Overview")

        self.scrollArea.setWidget(self.scrollContent)  # Never forget this!
        #self.overviewTab.setLayout(grid)

    def repaintOverviewTab(self):
        self.createOverviewTab()


    def createCharacterTabs(self, userList):

        for user in userList:
            characterTab = CharacterTabWidget(user)
            self.addTab(characterTab, user.CharacterName)


