from PyQt5.QtWidgets import QWidget, QSizePolicy, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5 import QtCore
from PyQt5.QtGui import QPalette, QPixmap, QFont

from db.databaseTables import User, Character, SkillQueue
from db.databaseHandler import DatabaseHandler

from urllib import request

import config

class CharacterTabWidget(QWidget):
    def __init__(self, user,  parent=None):
        super(CharacterTabWidget, self).__init__(parent)
        self.parent = parent
        self.user = user
        self.dbHandler = DatabaseHandler()  # ToDo: Dangerous to start an own instance of dbHandler?

        self.character = self.dbHandler.getCharacter(user.get_id())

        self.setLayout(self.createLayout())


    def createLayout(self):
        print("creating Character Tab Layout...")
        vBox = QVBoxLayout()
        vBox.addLayout(self.horizontalTop())
        vBox.addLayout(self.horizontalMiddle())
        vBox.addStretch(1)
        print("Layout created.")

        return vBox

    def horizontalTop(self):
        # Character Image
        characterImage = QLabel()
        pixmap = QPixmap(self.getCharacterPortrait())

        if pixmap is None:
            pixmap = QPixmap('image.png')

        characterImage.setPixmap(pixmap.scaled(120, 120))
        characterImage.resize(120, 120)

        hBox = QHBoxLayout()
        hBox.addWidget(characterImage)

        vBox = QVBoxLayout()
        vBox.setAlignment(QtCore.Qt.AlignLeft)

        nameLabel = QLabel(self.character.name)
        nameLabel.setFont(QFont("Arial", 14, QFont.Bold))

        balanceLabel = QLabel("Balance: ")
        corpLabel = QLabel("Corporation: ")
        allyLabel = QLabel("Alliance: ")
        secLabel = QLabel("Security Status: ")
        fatigueLabel = QLabel("Jump Fatigue: ")

        vBox.addWidget(nameLabel)
        vBox.addWidget(balanceLabel)
        vBox.addWidget(corpLabel)
        vBox.addWidget(allyLabel)
        vBox.addWidget(secLabel)
        vBox.addWidget(fatigueLabel)

        hBox.addLayout(vBox)
        hBox.addStretch(1)

        return hBox

    def horizontalMiddle(self):
        hBox = QHBoxLayout()

        return hBox


    def getCharacterPortrait(self):
        # Gets url to the character Portrait from db and sets the shown image to it
        # ToDo: Needs to be changed, so that the image is be save on the harddrive
        pixmap = QPixmap()
        try:
            portraitUrl = self.dbHandler.getCharacterPortrait(self.user.get_id())
            if portraitUrl is not None:
                data = request.urlopen(portraitUrl.px128x128).read()
                pixmap.loadFromData(data)
            else:
                print("No portrait URL for " + self.user.CharacterName + " in the Database")
        except Exception as e:
            print(e)

        return pixmap
