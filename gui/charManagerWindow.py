from PyQt5.QtWidgets import QWidget, QSizePolicy, QLabel, QVBoxLayout, QHBoxLayout, QTableWidget, QMainWindow,\
    QTableWidgetItem, QCheckBox, QAbstractItemView, QHeaderView, QTableView
from PyQt5.QtCore import QSize, QAbstractTableModel, Qt, QVariant
from PyQt5.QtGui import QPalette, QPixmap, QFont, QIcon
import config
import sys

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


class MyTableModel(QAbstractTableModel):
    def __init__(self, datain, headerdata, parent=None):
        """
        Args:
            datain: a list of lists\n
            headerdata: a list of strings
        """
        QAbstractTableModel.__init__(self, parent)
        self.arraydata = datain
        self.headerdata = headerdata

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        if len(self.arraydata) > 0:
            return len(self.arraydata[0])
        return 0

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.row()][index.column()])

    def setData(self, index, value, role):
        pass         # not sure what to put here

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headerdata[col])
        return QVariant()

class CharManagerWindow(QMainWindow):
    def __init__(self, parent=None):
        super(CharManagerWindow, self).__init__(parent)

        self.dbHandler = DatabaseHandler()

        self.set_main_window()

        self.centralwidget = QWidget(self)
        self.layout = QVBoxLayout(self.centralwidget)
        self.layout.setContentsMargins(0, 0, 5, 0)
        self.layout.setSpacing(0)
        self.setCentralWidget(self.centralwidget)

        #Heading Label
        self.headingLabel = QLabel("Characters")
        self.headingLabel.setFont(QFont("Arial", 20, QFont.Bold))
        self.layout.addWidget(self.headingLabel)
        self.layout.addSpacing(10)

        self.createTable()
        self.show()

    def createTable(self):

        self.characterTable = MyTable(0, 4)
        self.layout.addWidget(self.characterTable)

        self.setTableHeader()
        self.setTableContent()




    def setTableHeader(self):

        header = ("ID", "Name", "Account", "Authentication Status")
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
        for instance in userList:
            data=[]
            data.append(str(instance.CharacterID))
            data.append(instance.CharacterName)
            data.append("Account Name ?")
            data.append("OK")       # Add Auth check here
            self.characterTable.add_row(data)

    def set_main_window(self):
        # Standard Values for this Window
        standard_width = 544
        standard_height = 480
        minimum_width = 544
        minimum_height = 480

        """Sets the size policies of the main window"""
        self.resize(standard_width, standard_height)
        size_policy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)
        self.setMinimumSize(QSize(minimum_width, minimum_height))

        # main window icon
        self.setWindowIcon(QIcon(""))
        self.setWindowTitle(config.APP_NAME + " Character Manager")



