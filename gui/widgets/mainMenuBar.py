from PyQt5.QtWidgets import QMenuBar, QMenu

class MainMenuBar(QMenuBar):
    def __init__(self, parent=None):
        QMenuBar.__init__(self, parent)


        # Move Menubar from the MainWindow here if possible
