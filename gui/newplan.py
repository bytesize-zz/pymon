from PyQt5.QtWidgets import QWidget, QSizePolicy, QLabel, QVBoxLayout, QHBoxLayout, QTableWidget, QMainWindow,\
    QTableWidgetItem, QCheckBox, QAbstractItemView, QHeaderView, QTableView, QPushButton, QInputDialog, QApplication, \
    QLineEdit, QTextEdit
from PyQt5.QtCore import QSize, QAbstractTableModel, Qt, QVariant
from PyQt5.QtGui import QPalette, QPixmap, QFont, QIcon


import config
from db.databaseHandler import DatabaseHandler
from db.databaseTables import SkillPlan

from gui.skillplanwindow import SkillPlannerWindow

class NewPlanWindow(QMainWindow):
    def __init__(self, gui_queue, user_id, parent=None):
        super(NewPlanWindow, self).__init__(parent)

        self.parent = parent

        self.dbHandler = DatabaseHandler()
        self.gui_queue = gui_queue
        self.user_id = user_id

        if self.user_id is None:
            self.close()

        self.set_main_window()
        self.createLayout()


    def createLayout(self):
        self.centralwidget = QWidget(self)
        self.layout = QVBoxLayout(self.centralwidget)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(5)
        self.setCentralWidget(self.centralwidget)

        self.layout.addWidget(QLabel("Enter a name for this plan:"))
        self.name_dialog = QLineEdit(self)
        self.name_dialog.textChanged.connect(self.nameChanged)
        self.description_dialog = QTextEdit(self)

        self.layout.addWidget(self.name_dialog)
        self.layout.addSpacing(2)
        self.layout.addWidget(QLabel("Enter a description for this plan (optional):"))
        self.layout.addWidget(self.description_dialog)
        #self.layout.addStretch(1)

        self.ok_button = QPushButton("OK")
        self.ok_button.setDisabled(True)
        self.ok_button.clicked.connect(self.addPlan)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.close)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.ok_button)
        hbox.addWidget(self.cancel_button)

        self.layout.addLayout(hbox)

        #self.setLayout(self.layout)

    def nameChanged(self, text):
        if self.name_dialog.text() == "":
            self.ok_button.setDisabled(True)
        else:
            self.ok_button.setDisabled(False)

    def addPlan(self):
        name = self.name_dialog.text()
        description = self.description_dialog.toPlainText()

        newPlan = SkillPlan().create(name, description, self.user_id)

        self.dbHandler.addPlan(newPlan)
        #self.openSkillPlanner(newPlan.id)
        self.close()

    def openSkillPlanner(self, plan_id):
        skillPlanner = SkillPlannerWindow(plan_id)
        skillPlanner.show()

    def set_main_window(self):
        # Standard Values for this Window
        standard_width = 300
        standard_height = 200

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
        self.setWindowTitle(" New Plan")

