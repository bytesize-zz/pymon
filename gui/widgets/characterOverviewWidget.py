from PyQt5.QtWidgets import QWidget, QSizePolicy, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5 import QtCore
from PyQt5.QtGui import QPalette, QPixmap, QFont

from db.databaseTables import User, Character, SkillQueue
from db.databaseHandler import DatabaseHandler

import urllib, io
from urllib import request
import service.tools

# ToDo Mouse Over and click Event/Action
class CharacterOverviewWidget(QWidget):
    def __init__(self, user, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setAutoFillBackground(True)
        # self.installEventFilter()
        self.user = user
        self.dbHandler = DatabaseHandler()

        self.character = self.dbHandler.getCharacter(user.get_id())

        # Background Color
        #pal = QPalette()
        #pal.setColor(self.backgroundRole(), QtCore.Qt.red)
        #self.setPalette(pal)

        # Character Image
        self.characterImage = QLabel()
        self.pixmap = QPixmap('image.png')
        self.characterImage.setPixmap(self.pixmap.scaled(120, 120))
        self.characterImage.resize(120, 120)

        # Labels
        self.characterNameLabel = QLabel("Name")
        self.characterBalanceLabel = QLabel("Balance")
        self.characterSkillpointsLabel = QLabel("Skillpoints")
        self.characterSkillRemainingTimeLabel = QLabel("Skill Remaining Time")
        self.characterSkillNameLabel = QLabel("Skillname")
        self.characterSkillEndDateLabel = QLabel("Queue End Date")
        self.characterQueueRemainingTimeLabel = QLabel("Queue Remaining Time")

        self.setLabels()
        self.setCharacterPortrait()
        self.setLabelFonts()

        vbox= QVBoxLayout()
        vbox.setSpacing(1)
        vbox.setAlignment(QtCore.Qt.AlignTop)
        vbox.addWidget(self.characterNameLabel)
        vbox.addWidget(self.characterBalanceLabel)
        vbox.addWidget(self.characterSkillpointsLabel)
        vbox.addSpacing(10)
        vbox.addWidget(self.characterSkillRemainingTimeLabel)
        vbox.addSpacing(5)
        vbox.addWidget(self.characterSkillNameLabel)
        vbox.addWidget(self.characterSkillEndDateLabel)
        vbox.addWidget(self.characterQueueRemainingTimeLabel)

        hbox = QHBoxLayout()
        hbox.addWidget(self.characterImage)
        hbox.addSpacing(10)
        hbox.addLayout(vbox)
        hbox.addStretch(1)

        self.setLayout(hbox)

        self.set_size_policy()

    def setLabels(self):
        self.characterNameLabel.setText(self.character.name)
        self.characterBalanceLabel.setText(format(self.character.balance, ",") + " ISK")
        self.characterSkillpointsLabel.setText(format(self.character.total_sp, ",") + " SP")

        lastSkill = self.dbHandler.getSkillQueueLast(self.user.get_id())
        firstSkill = self.dbHandler.getSkillQueueFirst(self.user.get_id())

        #self.characterSkillRemainingTimeLabel.setText(service.tools.getSkillRemainingTime(firstSkill))
        self.characterSkillEndDateLabel.setText(str(firstSkill.finish_date))
        #self.characterQueueRemainingTimeLabel.setText(service.tools.getQueueRemainingTime(lastSkill))


    def setCharacterPortrait(self):
        # Gets url to the character Portrait from db and sets the shown image to it
        # ToDo: Needs to be changed, so that the image is be save on the harddrive
        portraitUrl = self.dbHandler.getCharacterPortrait(self.user.get_id())
        if portraitUrl is not None:
            data = request.urlopen(portraitUrl.px128x128).read()
            self.pixmap.loadFromData(data)
            self.characterImage.setPixmap(self.pixmap.scaled(120, 120))
        else:
            print("No portrait URL for " + self.user.CharacterName + " in the Database")

    def eventFilter(self, object, event):
        if event.type() == QtCore.QEvent.HoverMove:
            print("Mouseover")

    def set_size_policy(self):
        self.setMaximumSize(350, 150)
        #self.setMinimumSize(320, 120)

    def setLabelFonts(self):
        self.characterNameLabel.setFont(QFont("Arial", 14, QFont.Bold))
        self.characterBalanceLabel.setFont(QFont("Arial", 12, QFont.Bold))
        self.characterSkillpointsLabel.setFont(QFont("Arial", 10))
        self.characterSkillRemainingTimeLabel.setFont(QFont("Arial", 10))

