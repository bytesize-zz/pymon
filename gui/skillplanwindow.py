from PyQt5.QtWidgets import QWidget, QSizePolicy, QLabel, QVBoxLayout, QHBoxLayout, QTableWidget, QMainWindow,\
    QTableWidgetItem, QCheckBox, QAbstractItemView, QHeaderView, QTableView, QPushButton, QInputDialog, QApplication, \
    QLineEdit, QTextEdit
from PyQt5.QtCore import QSize, QAbstractTableModel, Qt, QVariant
from PyQt5.QtGui import QPalette, QPixmap, QFont, QIcon


import config
from db.databaseHandler import DatabaseHandler
from db.databaseTables import SkillPlan

class SkillPlannerWindow(QMainWindow):
    def __init__(self, plan_id, parent=None):
        super(SkillPlannerWindow, self).__init__(parent)

        self.dbHandler = DatabaseHandler()

        if plan_id is None:
            self.close()
        else:
            self.plan = self.dbHandler.getPlan(plan_id)
            if self.plan is not None:
                self.character_name = self.dbHandler.getCharacter(self.plan.owner_id).name

        self.set_main_window()
        self.createLayout()


    def set_main_window(self):
        # Standard Values for this Window
        standard_width = 860
        standard_height = 600
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
        # self.setMaximumSize(QSize(standard_width, standard_height))

        # main window icon
        self.setWindowIcon(QIcon(config.APP_ICON))
        #self.setWindowTitle(self.character_name + self.plan.name + config.APP_NAME + " Skill Planner")  # ToDo: Add plan owner and plan name

    def createLayout(self):
        self.centralwidget = QWidget(self)
        self.layout = QVBoxLayout(self.centralwidget)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(5)
        self.setCentralWidget(self.centralwidget)
