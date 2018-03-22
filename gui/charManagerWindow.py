from PyQt5.QtWidgets import QWidget, QSizePolicy, QLabel, QVBoxLayout, QHBoxLayout, QTableWidget, QMainWindow,\
    QTableWidgetItem, QCheckBox, QAbstractItemView, QHeaderView, QTableView
from PyQt5.QtCore import QSize, QAbstractTableModel, Qt
from PyQt5.QtGui import QPalette, QPixmap, QFont, QIcon
import config


# to complicated for now, because you can't simpli throw a checkbox in a table
# instad you have to create a QAbstractTableView and/or QAbstractItemView

class MyTable(QTableView):
    def __init__(self, r, c):
        super().__init__(r, c)

        #Table Configuration
        self.characterTable.setShowGrid(False)  # Hide Grid ToDo: Hide Field Selection
        self.characterTable.setEditTriggers(QAbstractItemView.NoEditTriggers)  # Disable editing

        self.setSelectionMode(QAbstractItemView.SingleSelection)  # Select only one row at once
        self.setSelectionBehavior(QAbstractItemView.SelectRows)   # Mark the whole Row
        #self.setFocusPolicy(Qt.NoFocus)
        self.show()


class CharManagerWindow(QMainWindow):
    def __init__(self, parent=None):
        super(CharManagerWindow, self).__init__(parent)
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

        self.characterTable = MyTable(2, 4)
        self.layout.addWidget(self.characterTable)

        self.setTableHeader()
        #self.setTableContent()


    def setTableHeader(self):

        header = ("ID", "Name", "Account", "Authentication Status")
        self.characterTable.setHorizontalHeaderLabels(header)
        self.characterTable.verticalHeader().setVisible(False)

        # set each column width, for now ResizeToContents
        for x in range(0, 3):
            self.characterTable.horizontalHeader().setSectionResizeMode(x, QHeaderView.ResizeToContents)
        self.characterTable.horizontalHeader().setStretchLastSection(True)
        self.characterTable.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)

    #def setTableContent(self):

        #self.characterTable.setItem(0,0, QTableWidgetItem("21564611212"))


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



