from PyQt5.QtWidgets import QWidget, QSizePolicy, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5 import QtCore
from PyQt5.QtGui import QPalette, QPixmap, QFont

from db.databaseTables import User, Character, SkillQueue
from db.databaseHandler import DatabaseHandler

from urllib import request

import datetime
import config

class CharacterTabWidget(QWidget):
    def __init__(self, user,  parent=None):
        super(CharacterTabWidget, self).__init__(parent)
        self.parent = parent
        self.user = user
        self.dbHandler = DatabaseHandler()  # ToDo: Dangerous to start an own instance of dbHandler?

        self.character = self.dbHandler.getCharacter(user.get_id())

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
        #print("creating Character Tab Layout...")
        vBox = QVBoxLayout()
        vBox.addLayout(self.horizontalTop())
        vBox.addSpacing(5)
        vBox.addLayout(self.horizontalMiddle())
        vBox.addStretch(1)
        #print("Layout created.")

        return vBox

    def createLayout2(self):
        hBox = QHBoxLayout()
        hBox.addLayout(self.setLeftVertical())
        hBox.addSpacing(5)
        hBox.addLayout(self.setMiddleVertical())
        hBox.addStretch(1)
        hBox.addLayout(self.setRightVertical())

        return hBox

    def horizontalTop(self):
        # Character Image
        characterImage = QLabel()
        pixmap = QPixmap(self.getCharacterPortrait())

        if pixmap is None:
            pixmap = QPixmap('image.png')

        characterImage.setPixmap(pixmap.scaled(150, 150))
        characterImage.resize(150, 150)

        hBox = QHBoxLayout()
        hBox.addWidget(characterImage)
        hBox.addSpacing(5)

        # Character General Information
        vBox = QVBoxLayout()
        vBox.setAlignment(QtCore.Qt.AlignLeft)

        nameLabel = QLabel(self.character.name)
        nameLabel.setFont(QFont("Arial", 14, QFont.Bold))

        balanceLabel = QLabel("Balance: ")
        corpLabel = QLabel("Corporation: ")
        allyLabel = QLabel("Alliance: ")
        secLabel = QLabel("Security Status: ")
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
        vBox.addStretch(1)

        hBox.addLayout(vBox)
        hBox.addStretch(1)

        #ToDo: Update Timer + Force update button

        return hBox

    def horizontalMiddle(self):
        # Account Subscription Status
        vBox1 = QVBoxLayout()
        subscriptionStatusLabel = QLabel("AccountStatus: " + "Omega")
        subsriptionTimeLabel = QLabel("Remaining Time")

        subscriptionStatusLabel.setFixedWidth(155)  # To indent the Middle hBox. size: pixmap + spacing

        vBox1.addWidget(subscriptionStatusLabel)
        vBox1.addWidget(subsriptionTimeLabel)
        vBox1.addStretch(1)

        # Character Stats
        vBox2 = QVBoxLayout()
        intelligenceLabel = QLabel("Intelligence: ")
        perceptionLabel = QLabel("Perception: ")
        charismaLabel = QLabel("Charisma: ")
        willpowerLabel = QLabel("Willpower: ")
        memoryLabel = QLabel("Memory: ")

        vBox2.addWidget(intelligenceLabel)
        vBox2.addWidget(perceptionLabel)
        vBox2.addWidget(charismaLabel)
        vBox2.addWidget(willpowerLabel)
        vBox2.addWidget(memoryLabel)

        #Clone Jump Status
        vBox3 = QVBoxLayout()
        bonusRemapLabel = QLabel("Bonus Remap: ")
        neuralRemapLabel = QLabel("Next Neural Remap: ")
        cloneJumpLabel = QLabel("Next Clone Jump: ")
        vBox2.addStretch(1)

        vBox3.addWidget(bonusRemapLabel)
        vBox3.addWidget(neuralRemapLabel)
        vBox3.addWidget(cloneJumpLabel)
        vBox3.addStretch(1)

        # Skills Statistics
        vBox4 = QVBoxLayout()
        knownSkillsLabel = QLabel("Known Skills: ")
        skillsAt5Label = QLabel("Skills at Level V: ")
        totalSPLabel = QLabel("Total SP: ")
        unallocatedSP = QLabel("Unallocated SP: ")

        vBox4.addWidget(knownSkillsLabel)
        vBox4.addWidget(skillsAt5Label)
        vBox4.addWidget(totalSPLabel)
        vBox4.addWidget(unallocatedSP)
        vBox4.addStretch(1)


        # Complete horizontal Middle
        hBox = QHBoxLayout()

        hBox.addLayout(vBox1)
        hBox.addLayout(vBox2)
        hBox.addSpacing(20)
        hBox.addLayout(vBox3)
        hBox.addStretch(1)
        hBox.addLayout(vBox4)

        return hBox

    def setLeftVertical(self):
        # Character Image
        characterImage = QLabel()
        pixmap = QPixmap(self.getCharacterPortrait())

        if pixmap is None:
            pixmap = QPixmap('image.png')

        characterImage.setPixmap(pixmap.scaled(150, 150))
        characterImage.resize(150, 150)

        vBox = QVBoxLayout()
        vBox.addWidget(characterImage)
        vBox.addSpacing(2)

        # Account Subscription Status
        subscriptionStatusLabel = QLabel("AccountStatus: " + "Omega")
        subsriptionTimeLabel = QLabel("Remaining Time")

        vBox.addWidget(subscriptionStatusLabel)
        vBox.addWidget(subsriptionTimeLabel)
        vBox.addStretch(1)

        return vBox


    def setMiddleVertical(self):
        # Character General Information
        vBox = QVBoxLayout()
        vBox.setAlignment(QtCore.Qt.AlignLeft)

        nameLabel = QLabel(self.character.name)
        nameLabel.setFont(QFont("Arial", 14, QFont.Bold))

        balanceLabel = QLabel("Balance: ")
        corpLabel = QLabel("Corporation: ")
        allyLabel = QLabel("Alliance: ")
        secLabel = QLabel("Security Status: ")
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

        # Character Stats
        vBox2 = QVBoxLayout()
        intelligenceLabel = QLabel("Intelligence: ")
        perceptionLabel = QLabel("Perception: ")
        charismaLabel = QLabel("Charisma: ")
        willpowerLabel = QLabel("Willpower: ")
        memoryLabel = QLabel("Memory: ")

        vBox2.addWidget(intelligenceLabel)
        vBox2.addWidget(perceptionLabel)
        vBox2.addWidget(charismaLabel)
        vBox2.addWidget(willpowerLabel)
        vBox2.addWidget(memoryLabel)

        # Clone Jump Status
        vBox3 = QVBoxLayout()
        bonusRemapLabel = QLabel("Bonus Remap: ")
        neuralRemapLabel = QLabel("Next Neural Remap: ")
        cloneJumpLabel = QLabel("Next Clone Jump: ")

        vBox3.addWidget(bonusRemapLabel)
        vBox3.addWidget(neuralRemapLabel)
        vBox3.addWidget(cloneJumpLabel)
        vBox3.addStretch(1)

        hBox = QHBoxLayout()
        hBox.addLayout(vBox2)
        hBox.addLayout(vBox3)

        vBox.addLayout(hBox)
        vBox.addStretch(1)

        return vBox

    def setRightVertical(self):


        # Skills Statistics
        vBox = QVBoxLayout()
        knownSkillsLabel = QLabel("Known Skills: ")
        skillsAt5Label = QLabel("Skills at Level V: ")
        totalSPLabel = QLabel("Total SP: ")
        unallocatedSP = QLabel("Unallocated SP: ")

        vBox.addStretch(1)
        vBox.addWidget(knownSkillsLabel)
        vBox.addWidget(skillsAt5Label)
        vBox.addWidget(totalSPLabel)
        vBox.addWidget(unallocatedSP)
        vBox.addStretch(1)

        return vBox

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

