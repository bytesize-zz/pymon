from PyQt5.QtWidgets import QWidget, QSizePolicy, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout, QMainWindow, QApplication, \
    QGridLayout, QPushButton, QScrollArea, QFrame
from PyQt5 import QtCore
from PyQt5.QtGui import QPalette, QPixmap, QFont

import sys
from db.databaseHandler import DatabaseHandler
from db.databaseTables import CompletedSkillList, CompletedSkillItem, User, StaticSkills, StaticSkillGroups

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
                widget = SkillGroupWidget(grp)
                self.scrollLayout.addWidget(widget)
                #self.createSkillsFromGroup(grp)  # ToDo: Print the known Skills for every Group

        self.scrollArea.setWidget(self.scrollContent) # Never forget this!!

    def doSomething(self, name):
        # ToDo: hide/unhide grouped skills on Group Click
        print(name)

    def createSkillsFromGroup(self, group):
        skills = self.dbHandler.getSkillsFromGroup(group)
        for skill in skills:
            #newLine = SkillItem(skill)
            newLine = QLabel(skill.name)
            self.scrollLayout.addWidget(newLine)



    def setBackgroundColor(self):
        self.setAutoFillBackground(True)
        # Background Color
        pal = QPalette()
        pal.setColor(self.backgroundRole(), QtCore.Qt.gray)
        self.setPalette(pal)

class SkillGroupWidget(QWidget):
    def __init__(self, group, parent=None):
        QWidget.__init__(self, parent=parent)

        self.setBackgroundColor()
        self.group = group
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
        self.setLabels()
        self.set_size_policy()

    def setLabels(self):

        self.nameLabel.setText(self.group.name)
        #self.countLabel.setText("x")
        #self.spLabel.setText("x")
        self.layout.update()

    def setBackgroundColor(self):
        self.setAutoFillBackground(True)
        # Background Color
        pal = QPalette()
        pal.setColor(self.backgroundRole(), QtCore.Qt.darkGray)
        self.setPalette(pal)



    def set_size_policy(self):
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)

    def mousePressEvent(self, *args, **kwargs):
        print(self.group.name)

class SkillItem(QWidget):
    def __init__(self, skill, parent=None):
        QWidget.__init__(self, parent=parent)


        self.setBackgroundColor()


    def setBackgroundColor(self):
        self.setAutoFillBackground(True)
        # Background Color
        pal = QPalette()
        pal.setColor(self.backgroundRole(), QtCore.Qt.lightGray)
        self.setPalette(pal)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # updateHandler = UpdateHandler()
    # updateHandler.updateAll()
    mainwindow = QMainWindow()

    mainwindow.show()
    layout = QVBoxLayout()
    layout.addWidget(SkillGroupWidget("test"))
    sys.exit(app.exec_())