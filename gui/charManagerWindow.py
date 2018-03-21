from PyQt5.QtWidgets import QWidget, QSizePolicy, QLabel, QVBoxLayout, QHBoxLayout, QTableWidget, QMainWindow,\
    QTableWidgetItem, QCheckBox, QAbstractItemView, QHeaderView
from PyQt5.QtCore import QSize, QAbstractTableModel, Qt
from PyQt5.QtGui import QPalette, QPixmap, QFont, QIcon
import config


# to complicated for now, because you can't simpli throw a checkbox in a table
# instad you have to create a QAbstractTableView and/or QAbstractItemView

class MyTable(QTableWidget):
    def __init__(self, r, c):
        super().__init__(r, c)

        self.setSelectionMode(QAbstractItemView.SingleSelection)  #
        self.setSelectionBehavior(QAbstractItemView.SelectRows)   # Mark the whole Row
        #self.setFocusPolicy(Qt.NoFocus)
        self.show()


class CharManagerWindow(QMainWindow):
    def __init__(self, parent=None):
        super(CharManagerWindow, self).__init__(parent)
        self.set_main_window()

        self.centralwidget = QWidget(self)
        self.layout = QVBoxLayout(self.centralwidget)
        self.layout.setContentsMargins(0, 0, 2, 0)
        self.layout.setSpacing(0)
        self.setCentralWidget(self.centralwidget)

        self.createTable()
        self.setTableHeader()

        self.show()

    def createTable(self):

        self.characterTable = MyTable(2, 5)
        self.layout.addWidget(self.characterTable)
        self.characterTable.setShowGrid(False)  # Hide Grid ToDo: Field Hide Selection

        checkBox = QCheckBox("x")
        #self.characterTable.setItem(1, 1, QTableWidgetItem())

    def setTableHeader(self):

        header = ("ID", "Name", "Account", "Authentication Status")
        self.characterTable.setHorizontalHeaderLabels(header)
        self.characterTable.verticalHeader().setVisible(False)

        # set each column width, for now ResizeToContents
        for x in range(0, 5):
            self.characterTable.horizontalHeader().setSectionResizeMode(x, QHeaderView.ResizeToContents)


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



