from PyQt5.QtWidgets import QWidget, QSizePolicy, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout, QMainWindow, QApplication, \
    QGridLayout, QPushButton, QScrollArea, QFrame
from PyQt5 import QtCore
from PyQt5.QtGui import QPalette, QPixmap, QFont

import sys
import datetime

from db.databaseHandler import DatabaseHandler
from db.databaseTables import CompletedSkillList, CompletedSkillItem, User, StaticSkills, StaticSkillGroups
from service import tools
from service.tools import format

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

        now = datetime.datetime.utcnow()

        # ToDo: Optimize with pythontricks
        if skillQueue is not None:
            queue_position = 1
            for skill in skillQueue:
                if (skill.finish_date is None) or (skill.finish_date > now):  # Skip completed Skills
                    widget = QueueItem(self.user.id, skill, queue_position)
                    self.scrollLayout.addWidget(widget)
                    queue_position += 1

        self.scrollArea.setWidget(self.scrollContent)  # Never forget this!


class QueueItem(QWidget):
    def __init__(self, user_id,  skill, queue_position, parent=None):
        QWidget.__init__(self, parent=parent)
        self.skill = skill
        self.user_id = user_id
        self.queue_position = queue_position

        self.setBackgroundColor()
        self.dbHandler = DatabaseHandler()

        self.staticData = self.dbHandler.getStaticSkillData(self.skill.skill_id)

        self.createLayout()

        if self.staticData is None:
            print("Queue Item Widget got a None Skill Static Data")
        else:
            # Int Values of the Characters primary and secondary Attributes, used for calculation
            charAttributes = self.dbHandler.getCharacterAttributes(self.user_id)
            charPrimaryAtt = tools.getCharPrimaryValue(charAttributes, self.staticData)
            charSecondaryAtt = tools.getCharSecondaryValue(charAttributes, self.staticData)
            self.spPerMinute = tools.spPerMinute(charPrimaryAtt, charSecondaryAtt)

            # Fill the Labels with Data, and update it every second for the 1st Skill in the Queue
            self.updateLabels()
            if self.queue_position == 1:
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
        #First Line ToDo: Optimize
        pos = str(self.queue_position)
        name = self.staticData.name
        self.titleLabel.setText(pos + ". " + name)
        self.rankLabel.setText("(Rank " + str(self.staticData.rank) + ")")
        self.levelLabel.setText("Level " + str(self.skill.finished_level))
        if self.skill.finish_date is not None:
            self.trainingTimeLabel.setText("Training Time: " + tools.getSkillTrainingTime(self.skill))     # -

        # Second Line
        skillTrainingProgress = tools.getSkillTrainingProgress(self.skill, self.spPerMinute)    # +

        self.spLabel.setText("SP: " + format(self.skill.level_start_sp + skillTrainingProgress) + "/"      # +
                             + format(self.skill.level_end_sp))
        self.spPerHourLabel.setText("SP/Hour: " + str(int(60*self.spPerMinute)))        # -

        self.progressLabel.setText(str(round(skillTrainingProgress /
                                             (self.skill.level_end_sp - self.skill.level_start_sp)
                                             * 100, 1)) + " % Done")  # +
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

