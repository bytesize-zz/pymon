from PyQt5.QtWidgets import QWidget, QSizePolicy, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5 import QtCore
from PyQt5.QtGui import QPalette, QPixmap, QFont

from db.databaseTables import User, Character, SkillQueue
from db.databaseHandler import DatabaseHandler

from gui.widgets.functionTabWidget import FunctionTabWidget

from urllib import request
from service.tools import offset, remapTime

import datetime
import config

class CharacterTabWidget(QWidget):
    def __init__(self, user,  parent=None):
        super(CharacterTabWidget, self).__init__(parent)
        self.parent = parent
        self.user = user
        self.dbHandler = DatabaseHandler()

        try:
            self.character = self.dbHandler.getCharacter(user.get_id())
            self.attributes = self.dbHandler.getCharacterAttributes(user.get_id())
        except Exception as e:
            print("Exception in CharacterTab: " + str(e))

            if self.character is None:
                print("Character Tab has a None Character")

        self.layout = self.createLayout()
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        self.startUpdateTimer()


    def startUpdateTimer(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateLabels)
        self.timer.setSingleShot(False)
        self.timer.start(1000)

    def updateLabels(self):
        self.layout.update()

    def createLayout(self):
        vBox = QVBoxLayout()
        vBox.addLayout(self.horizontalTop())
        vBox.addSpacing(5)
        vBox.addLayout(self.horizontalMiddle())
        self.functionTab = FunctionTabWidget(self.user)
        vBox.addWidget(self.functionTab)
        #vBox.addStretch(1)

        return vBox

    def horizontalTop(self):
        # Character Image
        characterImage = QLabel()
        pixmap = QPixmap(self.getCharacterPortrait())

        if pixmap is None:
            pixmap = QPixmap('image.png')

        characterImage.setPixmap(pixmap.scaled(150, 150))
        characterImage.resize(150, 150)

        hBox = QHBoxLayout()
        hBox.setAlignment(QtCore.Qt.AlignTop)
        hBox.addWidget(characterImage)
        hBox.addSpacing(5)

        # Character General Information
        vBox = QVBoxLayout()
        #vBox.setAlignment(QtCore.Qt.AlignLeft)
        vBox.setAlignment(QtCore.Qt.AlignTop)
        vBox.setSpacing(0)
        vBox.setContentsMargins(0,0,0,0)

        nameLabel = QLabel(self.character.name)
        nameLabel.setFont(QFont("Arial", 14, QFont.Bold))

        balanceLabel = QLabel("Balance: " + format(self.character.balance, ",") + " ISK")
        corpLabel = QLabel("Corporation: ")
        allyLabel = QLabel("Alliance: ")
        secLabel = QLabel("Security Status: " + str(round(self.character.security_status, 2)))
        fatigueLabel = QLabel("Jump Fatigue: ")
        shipLabel = QLabel("Active Ship: ")
        locationLabel = QLabel("Located in: ")
        dockedLabel = QLabel("Docked at: ")

        vBox.addWidget(nameLabel)
        vBox.addWidget(balanceLabel)
        vBox.addWidget(corpLabel)
        vBox.addWidget(allyLabel)
        vBox.addWidget(secLabel)
        vBox.addWidget(fatigueLabel)
        vBox.addWidget(shipLabel)
        vBox.addWidget(locationLabel)
        vBox.addWidget(dockedLabel)
        #vBox.addStretch(1)

        hBox.addLayout(vBox)
        hBox.addStretch(1)

        #ToDo: Update Timer + Force update button

        return hBox

    def horizontalMiddle(self):
        # Account Subscription Status
        vBox1 = QVBoxLayout()
        vBox1.setAlignment(QtCore.Qt.AlignTop)
        subscriptionStatusLabel = QLabel("AccountStatus: " + "Omega")
        subsriptionTimeLabel = QLabel("Remaining Time")

        subscriptionStatusLabel.setFixedWidth(155)  # To indent the Middle hBox. size: pixmap + spacing

        vBox1.addWidget(subscriptionStatusLabel)
        vBox1.addWidget(subsriptionTimeLabel)
        #vBox1.addStretch(1)

        # Character Stats
        vBox2 = QVBoxLayout()
        vBox2.setAlignment(QtCore.Qt.AlignTop)
        intelligenceLabel = QLabel("Intelligence: " + offset(8) + str(self.attributes.intelligence))  # 12
        perceptionLabel = QLabel("Perception: " + offset(9) + str(self.attributes.perception))  # 10
        charismaLabel = QLabel("Charisma: " + offset(11) + str(self.attributes.charisma))  # 8
        willpowerLabel = QLabel("Willpower: " + offset(11) + str(self.attributes.willpower))  # 9
        memoryLabel = QLabel("Memory: " + offset(13) + str(self.attributes.memory))  # 6

        intelligenceLabel.setFixedWidth(120)

        vBox2.addWidget(intelligenceLabel)
        vBox2.addWidget(perceptionLabel)
        vBox2.addWidget(charismaLabel)
        vBox2.addWidget(willpowerLabel)
        vBox2.addWidget(memoryLabel)
        #vBox2.addStretch(1)

        #Clone Jump Status
        vBox3 = QVBoxLayout()
        vBox3.setAlignment(QtCore.Qt.AlignTop)
        bonusRemapLabel = QLabel("Bonus Remap: " + str(self.attributes.bonus_remaps))
        neuralRemapLabel = QLabel("Next Neural Remap: " + remapTime(self.attributes.accrued_remap_cooldown_date))
        cloneJumpLabel = QLabel("Next Clone Jump: ")


        vBox3.addWidget(bonusRemapLabel)
        vBox3.addWidget(neuralRemapLabel)
        vBox3.addWidget(cloneJumpLabel)
        #vBox3.addStretch(1)

        # Skills Statistics
        vBox4 = QVBoxLayout()
        vBox4.setAlignment(QtCore.Qt.AlignTop)
        knownSkillsLabel = QLabel("Known Skills: ")
        skillsAt5Label = QLabel("Skills at Level V: ")
        totalSPLabel = QLabel("Total SP: " + format(self.character.total_sp, ","))
        if self.character.unallocated_sp is None:
            tmp = 0
        else:
            tmp = self.character.unallocated_sp
        unallocatedSP = QLabel("Unallocated SP: " + format(tmp, ","))

        vBox4.addWidget(knownSkillsLabel)
        vBox4.addWidget(skillsAt5Label)
        vBox4.addWidget(totalSPLabel)
        vBox4.addWidget(unallocatedSP)
        #vBox4.addStretch(1)


        # Complete horizontal Middle
        hBox = QHBoxLayout()

        hBox.addLayout(vBox1)
        hBox.addLayout(vBox2)
        hBox.addSpacing(20)
        hBox.addLayout(vBox3)
        hBox.addStretch(1)
        hBox.addLayout(vBox4)

        return hBox

    def getCharacterPortrait(self):
        # Gets url to the character Portrait from db and sets the shown image to it
        # ToDo: Needs to be changed, so that the image is be save on the harddrive
        pixmap = QPixmap()
        try:
            portraitUrl = self.dbHandler.getCharacterPortrait(self.user.get_id())
            if portraitUrl is not None:
                data = request.urlopen(portraitUrl.px256x256).read()
                pixmap.loadFromData(data)
            else:
                print("No portrait URL for " + self.user.CharacterName + " in the Database")
        except Exception as e:
            print(e)

        return pixmap

