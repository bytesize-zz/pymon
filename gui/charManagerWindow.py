from PyQt5.QtWidgets import QWidget, QSizePolicy, QLabel, QVBoxLayout, QHBoxLayout, QTableWidget, QMainWindow,\
    QTableWidgetItem, QCheckBox, QAbstractItemView, QHeaderView, QTableView, QPushButton
from PyQt5.QtCore import QSize, QAbstractTableModel, Qt, QVariant
from PyQt5.QtGui import QPalette, QPixmap, QFont, QIcon
import config
import sys
import datetime

from db.databaseHandler import DatabaseHandler


# to complicated for now, because you can't simply throw a checkbox in a table
# instad you have to create a QAbstractTableView and/or QAbstractItemView

class MyTable(QTableWidget):
    def __init__(self, r, c):
        super().__init__(r, c)

        #Table Configuration
        self.setShowGrid(False)  # Hide Grid ToDo: Hide Field Selection
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)  # Disable editing

        self.setSelectionMode(QAbstractItemView.SingleSelection)  # Select only one row at once
        self.setSelectionBehavior(QAbstractItemView.SelectRows)   # Mark the whole Row
        #self.setFocusPolicy(Qt.NoFocus)

    def add_row(self,  data):
        # expect a array of strings, wich contain data of one user
        # ToDo check if data is valid
        self.insertRow(self.rowCount())

        for pos in range(0, len(data)):
            self.setItem(self.rowCount()-1, pos, QTableWidgetItem(data[pos]))


class CharManagerWindow(QMainWindow):
    def __init__(self, gui_queue, parent=None):
        super(CharManagerWindow, self).__init__(parent)

        self.dbHandler = DatabaseHandler()
        self.gui_queue = gui_queue

        self.set_main_window()

        self.centralwidget = QWidget(self)
        self.layout = QVBoxLayout(self.centralwidget)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(0)
        self.setCentralWidget(self.centralwidget)

        #Heading Label
        self.headingLabel = QLabel("Characters")
        self.headingLabel.setFont(QFont("Arial", 18, QFont.Bold))
        self.layout.addWidget(self.headingLabel)
        self.layout.addSpacing(10)

        #Buttons
        hBox = QHBoxLayout()
        deleteButton = QPushButton("Delete")
        importButton = QPushButton("Import")
        exportButton = QPushButton("Export")
        deleteButton.clicked.connect(self.deleteTriggered)
        importButton.clicked.connect(self.importTriggered)
        exportButton.clicked.connect(self.exportTriggered)

        hBox.addWidget(deleteButton)
        hBox.addWidget(importButton)
        hBox.addWidget(exportButton)

        self.layout.addLayout(hBox)

        self.createTable()
        self.show()

    def createTable(self):

        self.characterTable = MyTable(0, 4)
        self.layout.addWidget(self.characterTable)

        self.setTableHeader()
        self.setTableContent()

    def setTableHeader(self):
        header = ("", "ID", "Name", "Authentication Status")
        self.characterTable.setHorizontalHeaderLabels(header)
        self.characterTable.verticalHeader().setVisible(False)

        # set each column width, for now ResizeToContents
        for x in range(0, len(header)-1):
            self.characterTable.horizontalHeader().setSectionResizeMode(x, QHeaderView.ResizeToContents)
        self.characterTable.horizontalHeader().setStretchLastSection(True)
        self.characterTable.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)

    def setTableContent(self):
        # self.characterTable.add_row(["test", "test2"])

        # Ask the Database for a List of all saved Characters
        userList = self.dbHandler.getAllUser()

        # If there are any users saved get the needed elements for our table
        for user in userList:
            data=[]
            data.append(str(user.id))
            data.append(str(user.CharacterID))
            data.append(user.CharacterName)
            data.append(self.getUserAuthStatus(user))
            self.characterTable.add_row(data)

    def set_main_window(self):
        # Standard Values for this Window
        standard_width = 544
        standard_height = 480
        minimum_width = 544
        minimum_height = 300

        """Sets the size policies of the main window"""
        self.resize(standard_width, standard_height)
        size_policy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)
        self.setMinimumSize(QSize(minimum_width, minimum_height))

        # main window icon
        self.setWindowIcon(QIcon(config.APP_ICON))
        self.setWindowTitle(config.APP_NAME + " Character Manager")

    def getSelectedUser(self):

        #print(self.characterTable.selectedItems())
        selection = self.characterTable.selectedItems()
        if selection is None or len(selection) == 0:
            return None
        else:
            return int(self.characterTable.selectedItems()[1].text())

    def getUserAuthStatus(self, user):
        status = ""
        now = datetime.datetime.utcnow()

        if user.RefreshToken is None or user.AccessToken is None:
            status = "No Authentication"
        elif now < user.AccessTokenExpire:
            status = "Valid Access Token"
        elif now > user.AccessTokenExpire:
            status = "Valid Refresh Token"

        return status

    def deleteTriggered(self):
        character_id = self.getSelectedUser()
        #print(str(character_id))
        self.deleteWindow = DeleteWindow(character_id, self.gui_queue, self)
        self.deleteWindow.show()


    def importTriggered(self):
        print("import")

    def exportTriggered(self):
        print("export")

class DeleteWindow(QMainWindow):
    def __init__(self, character_id, gui_queue, parent=None):
        super(DeleteWindow, self).__init__(parent)
        self.dbHandler = DatabaseHandler()
        self.user = self.dbHandler.getUser(character_id)
        self.gui_queue = gui_queue

        self.set_main_window()

        self.centralwidget = QWidget(self)
        self.layout = QVBoxLayout(self.centralwidget)

        if self.user.id is None:
            self.layout.addWidget(QLabel("No User selected"))
            self.layout.addStretch(1)
            hBox = QHBoxLayout()
            hBox.addStretch(1)
            button = QPushButton("OK")
            button.clicked.connect(self.close)
            hBox.addWidget(button)

            self.layout.addLayout(hBox)
        else:
            self.layout.addWidget(QLabel("You are about to delete the Character: " + self.user.CharacterName))
            self.layout.addWidget(QLabel("All Data will be lost! Are you sure?"))
            self.layout.addStretch(1)

            hBox = QHBoxLayout()
            deleteButton = QPushButton("Delete")
            deleteButton.clicked.connect(self.deleteUser)
            cancelButton = QPushButton("Cancel")
            cancelButton.clicked.connect(self.close)
            hBox.addStretch(1)
            hBox.addWidget(deleteButton)
            hBox.addWidget(cancelButton)

            self.layout.addLayout(hBox)

        self.setCentralWidget(self.centralwidget)
        self.show()

    def deleteUser(self):
        self.dbHandler.deleteUser(self.user.id)
        self.gui_queue.put("Reprint MainWindow")
        self.close()

    def set_main_window(self):
        # Standard Values for this Window
        standard_width = 400
        standard_height = 180

        """Sets the size policies of the main window"""
        self.resize(standard_width, standard_height)
        size_policy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)
        self.setMinimumSize(QSize(standard_width, standard_height))
        self.setMaximumSize(QSize(standard_width, standard_height))

        # main window icon
        self.setWindowIcon(QIcon(config.APP_ICON))
        self.setWindowTitle("Delete Character")