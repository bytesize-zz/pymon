from PyQt5.QtWidgets import QWidget, QSizePolicy, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout, QMainWindow, QApplication, \
    QGridLayout, QPushButton, QScrollArea, QFrame
from PyQt5 import QtCore
from PyQt5.QtGui import QPalette, QPixmap, QFont

import sys
from db.databaseHandler import DatabaseHandler
from db.databaseTables import CompletedSkillList, CompletedSkillItem, User, StaticSkills, StaticSkillGroups
from service.tools import getSkillTrainingTime


# ToDo Mouse Over and click Event/Action
class SkillQueueWidget(QWidget):
    def __init__(self, user, parent=None):
        QWidget.__init__(self, parent=parent)

        self.user = user
        self.dbHandler = DatabaseHandler()

        self.initiateLayout()
        self.createSkillQueue()

        #self.tabLayout.setContentsMargins(0,0,0,0)
        #self.tabLayout.setSpacing(0)

        self.setBackgroundColor()

    def initiateLayout(self):
        '''
            box is a Layout needed to Stretch the scrollArea
            scrollArea is needed to add the Scrollbar
            scrollContent is needed to display the scrollable Items inside the scrollArea
            scrollLayout is needed to stretch the Items inside scrollContent

        '''

        box = QVBoxLayout(self)
        box.setContentsMargins(0,0,0,0)
        box.setSpacing(0)

        self.setLayout(box)
        self.scrollArea = QScrollArea(self)
        box.addWidget(self.scrollArea)
        self.scrollArea.setWidgetResizable(True)
        self.scrollContent = QWidget(self.scrollArea)
        self.scrollLayout = QVBoxLayout(self.scrollContent)
        self.scrollLayout.setContentsMargins(2,2,2,2)
        self.scrollLayout.setSpacing(4)
        self.scrollLayout.setAlignment(QtCore.Qt.AlignTop)
        self.scrollContent.setLayout(self.scrollLayout)

    def setBackgroundColor(self):
        self.setAutoFillBackground(True)
        # Background Color
        pal = QPalette()
        pal.setColor(self.backgroundRole(), QtCore.Qt.white)
        self.setPalette(pal)

    def createSkillQueue(self):
        skillQueue = self.dbHandler.getSkillQueue(self.user.get_id())

        if skillQueue is not None:
            for skill in skillQueue:
                widget = QueueItem(skill)
                self.scrollLayout.addWidget(widget)

        self.scrollArea.setWidget(self.scrollContent)  # Never forget this!


class QueueItem(QWidget):
    def __init__(self, skill, parent=None):
        QWidget.__init__(self, parent=parent)
        self.skill = skill

        self.setBackgroundColor()
        self.dbHandler = DatabaseHandler()

        self.staticData = self.dbHandler.getStaticSkillData(self.skill.skill_id)

        self.createLayout()

        if self.staticData is None:
            print("Queue Item Widget got a None Skill Static Data")
        else:
            self.updateLabels()
            self.startUpdateTimer()


    def createLayout(self):

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.firstLine())
        self.layout.addLayout(self.secondLine())
        self.setLayout(self.layout)

        self.set_size_policy()


    def firstLine(self):
        hbox = QHBoxLayout()

        self.titleLabel = QLabel("x. Skill Name")
        self.rankLabel = QLabel("Rank x")
        self.levelLabel = QLabel("Level X")

        self.titleLabel.setFont(QFont("Arial", 8, QFont.Bold))

        hbox.addWidget(self.titleLabel)
        hbox.addSpacing(5)
        hbox.addWidget(self.rankLabel)
        hbox.addStretch(1)
        hbox.addWidget(self.levelLabel)

        return hbox

    def secondLine(self):
        hbox = QHBoxLayout()

        self.spLabel = QLabel("SP: ")
        self.spPerHourLabel = QLabel("SP/Hour: ")
        self.trainingTimeLabel = QLabel("Training Time: ")
        self.progressLabel = QLabel(" % Done")


        hbox.addWidget(self.spLabel)
        hbox.addSpacing(5)
        hbox.addWidget(self.spPerHourLabel)
        hbox.addSpacing(5)
        hbox.addWidget(self.trainingTimeLabel)
        hbox.addStretch(1)
        hbox.addWidget(self.progressLabel)

        return hbox

    def updateLabels(self):
        pos = str(self.skill.queue_position + 1)  # Is mostly wrong, queue position doesn't get updated after skills are completed
        name = self.staticData.name
        self.titleLabel.setText(pos + ". " + name)
        self.levelLabel.setText("Level: " + str(self.skill.finished_level))
        if self.skill.finish_date is not None:
            self.trainingTimeLabel.setText("Training Time: " + getSkillTrainingTime(self.skill))
        self.layout.update()

    def setBackgroundColor(self):
        self.setAutoFillBackground(True)
        # Background Color
        pal = QPalette()
        mod = self.skill.queue_position % 2
        if mod == 0:
            pal.setColor(self.backgroundRole(), QtCore.Qt.lightGray)
        else:
            pal.setColor(self.backgroundRole(), QtCore.Qt.white)

        self.setPalette(pal)


    def set_size_policy(self):
        self.layout.setContentsMargins(1, 1, 1, 1)
        self.layout.setSpacing(1)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)

    def startUpdateTimer(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateLabels)
        self.timer.setSingleShot(False)
        self.timer.start(1000)

