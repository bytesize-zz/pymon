from PyQt5.QtWidgets import QWidget, QSizePolicy, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5 import QtCore
from PyQt5.QtGui import QPalette, QPixmap, QFont


# ToDo Mouse Over and click Event/Action
class CharacterOverviewWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setAutoFillBackground(True)
        # self.installEventFilter()


        pal = QPalette()
        pal.setColor(self.backgroundRole(), QtCore.Qt.red)
        self.setPalette(pal)

        # Character Image
        characterImage = QLabel()
        characterImage.setPixmap(QPixmap('image.png').scaled(120, 120))
        characterImage.resize(120, 120)

        # Labels
        self.characterNameLabel = QLabel("Name")
        self.characterBalanceLabel = QLabel("Balance")
        self.characterSkillpointsLabel = QLabel("Skillpoints")
        self.characterSkillRemainingTimeLabel = QLabel("Skill Remaining Time")
        self.characterSkillNameLabel = QLabel("Skillname")
        self.characterQueueEndDateLabel = QLabel("Queue End Date")
        self.characterQueueRemainingTimeLabel = QLabel("Queue Remaining Time")

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
        vbox.addWidget(self.characterQueueEndDateLabel)
        vbox.addWidget(self.characterQueueRemainingTimeLabel)

        hbox = QHBoxLayout()
        hbox.addWidget(characterImage)
        hbox.addSpacing(10)
        hbox.addLayout(vbox)
        hbox.addStretch(1)


        self.setLayout(hbox)


        self.set_size_policy()

    def eventFilter(self, object, event):
        if event.type() == QtCore.QEvent.HoverMove:
            print("Mouseover")

    def set_size_policy(self):
        self.setMaximumSize(350, 150)
        #self.setMinimumSize(320, 120)

    def setLabelFonts(self):
        self.characterNameLabel.setFont(QFont("Comic Sans MS", 14, QFont.Bold))
        self.characterBalanceLabel.setFont(QFont("Arial", 12, QFont.Bold))
        self.characterSkillpointsLabel.setFont(QFont("Arial", 10))
        self.characterSkillRemainingTimeLabel.setFont(QFont("Arial", 10))

