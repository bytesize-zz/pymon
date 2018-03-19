from PyQt5.QtWidgets import QFrame, QSizePolicy,QLabel
from PyQt5.QtCore import QSize, Qt


class OverviewFrame(QFrame):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent=parent)

        self.label = QLabel("Test")


    def _set_size_policy(self):
        size_policy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)