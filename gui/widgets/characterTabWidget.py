from PyQt5.QtWidgets import QWidget, QSizePolicy, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5 import QtCore
from PyQt5.QtGui import QPalette, QPixmap, QFont

from db.databaseTables import User, Character, SkillQueue
from db.databaseHandler import DatabaseHandler


class CharacterTabWidget(QWidget):
    def __init__(self, parent=None):
        super(CharacterTabWidget, self).__init__(parent)
        self.parent = parent
        self.dbHandler = DatabaseHandler()  # ToDo: Dangerous to start an own instance of dbHandler?