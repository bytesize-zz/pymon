from PyQt5.QtWidgets import QWidget, QSizePolicy, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout, QMainWindow, QApplication, \
    QGridLayout, QPushButton, QScrollArea, QFrame
from PyQt5 import QtCore
from PyQt5.QtGui import QPalette, QPixmap, QFont

import sys
import math
from db.databaseHandler import DatabaseHandler
from db.databaseTables import CompletedSkillList, CompletedSkillItem, User, StaticSkills, StaticSkillGroups
from service import tools
from service.tools import format

#hyper Parameter
dbHandler = DatabaseHandler()

# ToDo Mouse Over and click Event/Action
class CompletedSkillsWidget(QWidget):
    def __init__(self, user, parent=None):
        QWidget.__init__(self, parent=parent)

        self.user = user
        self.dbHandler = DatabaseHandler()

        self.initiateLayout()
        self.createGroupList()

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
        self.scrollLayout.setContentsMargins(0,0,0,0)
        self.scrollLayout.setSpacing(0)
        self.scrollLayout.setAlignment(QtCore.Qt.AlignTop)
        self.scrollContent.setLayout(self.scrollLayout)


    def createGroupList(self):
        groups = self.dbHandler.getStaticSkillGroups()

        if groups is not None:
            for grp in groups:
                grpWidget = SkillGroupWidget(self.user.id, grp)
                self.scrollLayout.addWidget(grpWidget)
                for skillWidget in grpWidget.getChildWidgets():
                    self.scrollLayout.addWidget(skillWidget)

        self.scrollArea.setWidget(self.scrollContent) # Never forget this!!


    def setBackgroundColor(self):
        self.setAutoFillBackground(True)
        # Background Color
        pal = QPalette()
        pal.setColor(self.backgroundRole(), QtCore.Qt.lightGray)
        self.setPalette(pal)

class SkillGroupWidget(QWidget):
    def __init__(self, user_id,  group, parent=None):
        QWidget.__init__(self, parent=parent)
        self.collapse = False  # un/visible status of self.skills
        self.group = group  # This group
        self.user_id = user_id
        self.skills = []  # List of Skills belonging to this group
        self.skillWidgets = []

        self.createSkillWidgets()

        self.setBackgroundColor()
        self.layout = QHBoxLayout()
        #self.layout.setAlignment(QtCore.Qt.AlignTop)
        self.layout.setContentsMargins(1, 1, 1, 1)
        #self.layout.setSpacing(0)

        self.nameLabel = QLabel("Name")
        self.nameLabel.setFixedWidth(200)
        self.countLabel = QLabel("1 of 1 skills")
        self.countLabel.setFixedWidth(100)
        self.spLabel = QLabel("1.000.000 Points")
        self.spLabel.setFixedWidth(100)

        self.layout.addWidget(self.nameLabel)
        self.layout.addWidget(self.countLabel)
        self.layout.addWidget(self.spLabel)
        self.layout.addStretch(1)
        self.setLayout(self.layout)
        self.set_size_policy()
        self.setLabelStyle()

        self.updateLabels()

    def updateLabels(self):
        self.nameLabel.setText(self.group.name)
        #self.countLabel.setText("x")
        #self.spLabel.setText("x")
        self.layout.update()

    def setLabelStyle(self):
        self.nameLabel.setStyleSheet('QLabel { font-size: 12px; color: white; font-weight: bold}')
        self.countLabel.setStyleSheet('QLabel { font-size: 12px; color: white}')
        self.spLabel.setStyleSheet('QLabel { font-size: 12px; color: white}')

    def setBackgroundColor(self):
        self.setAutoFillBackground(True)
        # Background Color
        pal = QPalette()
        pal.setColor(self.backgroundRole(), QtCore.Qt.black)
        self.setPalette(pal)

    def set_size_policy(self):
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)

    def mousePressEvent(self, *args, **kwargs):
        self.toggleGroupCollapse()

    def toggleGroupCollapse(self):
        if self.collapse:
            for widget in self.skillWidgets:
                widget.setVisible(False)
            self.collapse = False
        else:
            for widget in self.skillWidgets:
                widget.setVisible(True)
            self.collapse = True


    def createSkillWidgets(self):
        self.skills = dbHandler.getGroupSkills(self.user_id, self.group.group_id)

        for i, skill in enumerate(self.skills):
            widget = CompletedSkillsItem(self.user_id, skill, i)
            widget.setVisible(False)
            #widget.setHidden(True)
            #widget.hide()
            self.skillWidgets.append(widget)

    def getChildWidgets(self):
        return self.skillWidgets


class CompletedSkillsItem(QWidget):
    def __init__(self, user_id,  skill, position, parent=None):
        QWidget.__init__(self, parent=parent)
        self.skill = skill
        self.position = position
        self.user_id = user_id
        self.dbHandler = DatabaseHandler()
        self.staticData = self.dbHandler.getStaticSkillData(self.skill.skill_id)
        self.skillQueueItem = None

        # ToDo: If this skill is in this User's skillQueue activate updateTimer and update labels


        self.setBackgroundColor()
        self.createLayout()

        self.checkSkillQueue()

        if self.staticData is None:
            print("Completed Skill Item Widget got a None Skill Static Data")
        else:
            # Int Values of the Characters primary and secondary Attributes, used for calculation
            charAttributes = self.dbHandler.getCharacterAttributes(self.user_id)
            charPrimaryAtt = tools.getCharPrimaryValue(charAttributes, self.staticData)
            charSecondaryAtt = tools.getCharSecondaryValue(charAttributes, self.staticData)
            self.spPerMinute = tools.spPerMinute(charPrimaryAtt, charSecondaryAtt)

            # Fill the Labels with Data, and update it every second for the 1st Skill in the Queue
            self.updateLabels()


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
        self.progressLabel = QLabel(" % Done")

        hbox.addWidget(self.spLabel)
        hbox.addStretch(1)
        hbox.addWidget(self.progressLabel)

        return hbox

    def updateLabels(self):
        #First Line ToDo: Optimize
        #pos = str(self.queue_position)
        name = self.staticData.name
        self.titleLabel.setText(name)
        self.rankLabel.setText("(Rank " + str(self.staticData.rank) + ")")
        self.levelLabel.setText("Level " + str(self.skill.trained_skill_level))

        # Second Line
        if self.skill.trained_skill_level == 5:
            modifier = 4
        else:
            modifier = self.skill.trained_skill_level

        # Eve training multiplier formula: SP = 250 * multiplier * sqrt(32)^(level-1)
        skill_level_end_sp = 250 * self.staticData.rank * math.sqrt(32) ** modifier

        if self.skillQueueItem is None:
            skillTrainingProgress = 0
        else:
            skillTrainingProgress = tools.getSkillTrainingProgress(self.skillQueueItem, self.spPerMinute)

        self.spLabel.setText("SP: " + format(self.skill.skillpoints_in_skill + skillTrainingProgress) + "/"
                             + format(round(skill_level_end_sp)))

        self.progressLabel.setText(str(round(skillTrainingProgress /
                                             (skill_level_end_sp - self.skill.skillpoints_in_skill)
                                             * 100, 1)) + " % Done")  # +

        self.layout.update()

    def checkSkillQueue(self):
        # ToDO: Might need improvement check if skill is already completed
        # we want to know if this skill is in this users skill queue
        self.skillQueueItem = dbHandler.getSkillQueueItem(self.user_id, self.skill.skill_id)
        if self.skillQueueItem is not None:
            self.startUpdateTimer()


    def setBackgroundColor(self):
        self.setAutoFillBackground(True)
        # Background Color
        pal = QPalette()
        mod = self.position % 2
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