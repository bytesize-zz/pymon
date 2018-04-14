from PyQt5.QtWidgets import QTabWidget, QWidget, QLabel, QVBoxLayout, QScrollArea, QSizePolicy
from PyQt5 import QtCore
from PyQt5.QtGui import QPalette, QPixmap, QFont

from gui.widgets.completedSkillsWidget import CompletedSkillsWidget, SkillGroupWidget
from gui.widgets.skillQueueWidget import SkillQueueWidget, QueueItem

# Database Imports
from db.databaseTables import User
from db.databaseHandler import DatabaseHandler

class FunctionTabWidget(QTabWidget):
    def __init__(self, user, parent=None):
        super(FunctionTabWidget, self).__init__(parent)

        self.user = user
        self.dbHandler = DatabaseHandler()
        self.setBackgroundColor()

        self.createCompletedSkills(user)
        self.createSkillQueue(user)

    def createCompletedSkills(self, user):
        completedSkillsTab = CompletedSkillsWidget(user)
        self.addTab(completedSkillsTab, "Skills")

    def createSkillQueue(self, user):
        skillQueueTab = SkillQueueWidget(user)
        self.addTab(skillQueueTab, "SkillQueue")

    def setBackgroundColor(self):
        self.setAutoFillBackground(True)
        # Background Color
        pal = QPalette()
        pal.setColor(self.backgroundRole(), QtCore.Qt.white)
        self.setPalette(pal)

