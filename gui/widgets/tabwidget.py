from PyQt5.QtWidgets import QTabWidget, QWidget, QFrame
from PyQt5.QtGui import QFont

from gui.widgets.overviewFrame import OverviewFrame

class TabWidget(QTabWidget):
    """Tab widget of related collection/s"""

    def __init__(self, parent=None):
        super(TabWidget, self).__init__(parent)
        self.set_font()

        # Overview Tab
        self.createOverviewTab()

        #self._retranslate_status_tips()

    def createOverviewTab(self):
        self.overviewTab = QWidget()
        self.overviewFrame = QFrame()
        self.addTab(self.overviewTab, "Overview")
        #self.overviewTab.addWidget(overviewFrame)

    def createCharacterTab(self):
        self.characterTab = QWidget()
        self.addTab(self.characterTab, "Character Name")

    def set_font(self):
        font = QFont()
        font.setPointSize(10)
        self.setFont(font)

    #def _retranslate_status_tips(self):
        # self.tab_audio.setStatusTip("Audio collection of related culture...")