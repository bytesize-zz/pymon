from PyQt5.QtWidgets import QMenuBar, QMenu

class MainMenuBar(QMenuBar):
    def __init__(self, parent=None):
        QMenuBar.__init__(self, parent)
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 908, 21))
        self.setObjectName("menubar")

        self.menuFile = QMenu(self)
        self.menuFile.setObjectName("menuFile")
