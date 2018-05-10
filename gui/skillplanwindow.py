from PyQt5.QtWidgets import QWidget, QSizePolicy, QLabel, QVBoxLayout, QHBoxLayout, QTableWidget, QMainWindow,\
    QTableWidgetItem, QCheckBox, QAbstractItemView, QHeaderView, QTableView, QPushButton, QInputDialog, QApplication, \
    QLineEdit, QTextEdit, QComboBox, QAction
from PyQt5.QtCore import QSize, QAbstractTableModel, Qt, QVariant
from PyQt5.QtGui import QPalette, QPixmap, QFont, QIcon

import functools
import config
from db.databaseHandler import DatabaseHandler
from db.databaseTables import SkillPlan

class SkillPlannerWindow(QMainWindow):
    def __init__(self, plan_id, parent=None):
        super(SkillPlannerWindow, self).__init__(parent)
        self.dbHandler = DatabaseHandler()
        self.plan = None
        self.loadPlan(plan_id)

        if self.plan is not None:
            self.user_id = self.plan.owner_id
            self.character_name = self.dbHandler.getCharacter(self.user_id).name

        self.set_main_window()
        self.initLayout()

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

    def initLayout(self):
        self.centralwidget = QWidget(self)
        self.layout = QVBoxLayout(self.centralwidget)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(5)
        self.setCentralWidget(self.centralwidget)

        self.plansCombo = QComboBox(self)
        self.plansCombo.addItem("Select Plan")
        self.plansCombo.addItem("New Plan")
        self.plansCombo.addItem("Create Plan from Skill Queue")

        self.plansCombo.activated.connect(self.handlePlansCombo)

        self.fillPlansCombo()


        self.layout.addLayout(self.firstLineOptions())

    def firstLineOptions(self):
        '''
        First Line
        Options: Select Plan
        Export Plan to
        Delete Plan
        Print Plan (drucken)
        Copy to clipboard
        Implant calculator
        atrribute optimizer
        :return:
        '''


        hbox = QHBoxLayout()
        hbox.addWidget(self.plansCombo)
        hbox.addStretch(1)

        return hbox

    def skillPlannerTabs(self):
        print("")


    def handlePlansCombo(self, index):

        itemData = self.plansCombo.itemData(index)
        itemText = self.plansCombo.itemText(index)
        if itemData is not None:
            print(self.plansCombo.itemData(index))

    def fillPlansCombo(self):

        plan_list = self.dbHandler.getCharacterPlans(self.user_id)

        for plan in plan_list:
            self.plansCombo.addItem(plan.name, plan.id)

        self.layout.update()

    def loadPlan(self, plan_id):
        if plan_id is not None:
            self.plan = self.dbHandler.getPlan(plan_id)
            # update skill list window
