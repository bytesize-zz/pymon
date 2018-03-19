# https://github.com/MTG/dunya-desktop/blob/master/dunyadesktop_app/general_design.py
import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from service.esi import login

import config

# from widgets.dockwidget import DockWidget, DockWidgetContentsLeft,  DockWidgetContentsTop
# from widgets.queryframe import QueryFrame
from gui.widgets.progressbar import ProgressBar
from gui.widgets.tabwidget import TabWidget

class GeneralMainDesign(QMainWindow):
    """General design of the main window"""
    def __init__(self):
        super().__init__()
        self.init_MainWindow()

    def init_MainWindow(self):
        self.set_main_window()
        self.centralwidget = QWidget(self)

        layout = QVBoxLayout(self.centralwidget)
        layout.setContentsMargins(0, 0, 2, 0)
        layout.setSpacing(0)

        # query frame
        # self.frame_query = QueryFrame()
        # self._set_frame()
        # layout.addWidget(self.frame_query)

        self.setCentralWidget(self.centralwidget)

        # status bar
        self.statusbar = QStatusBar(self)
        self.set_status_bar()
        self.setStatusBar(self.statusbar)

        # MainMenuBar
        self.menubar = self.menuBar()
        self.set_main_menubar()

        # Tab Widget
        self.tab_widget = TabWidget(self)
        layout.addWidget(self.tab_widget)

        self.show()
        # self.progress_bar = ProgressBar(self)
        # self.statusbar.addPermanentWidget(self.progress_bar)
        # self.progress_bar.setVisible(True)

        # self.dw_top = DockWidget(460, 90, 20000, 50)
        # self.dw_top.setTitleBarWidget(QWidget())
        # self.dwc_top = DockWidgetContentsTop()
        # .dw_top.setWidget(self.dwc_top)
        # self.addDockWidget(QtCore.Qt.TopDockWidgetArea, self.dw_top)

        # dockwidget collection (left side)
        # self.dw_collections = DockWidget(350, 620, 700, 20000)
        # self.dw_collections.setTitleBarWidget(QWidget())
        # self.dwc_left = DockWidgetContentsLeft(self)
        # self.dw_collections.setWidget(self.dwc_left)
        # self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dw_collections)

        QMetaObject.connectSlotsByName(self)

    def set_main_window(self):
        """Sets the size policies of the main window"""
        self.resize(config.GUI_MAIN_WINDOW_STANDARD_WIDTH, config.GUI_MAIN_WINDOW_STANDARD_HEIGHT)
        size_policy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)
        self.setMinimumSize(QSize(config.GUI_MAIN_WINDOW_MINIMUM_WIDTH, config.GUI_MAIN_WINDOW_MINIMUM_HEIGHT))

        # main window icon
        self.setWindowIcon(QIcon(""))
        self.setWindowTitle(config.APP_NAME)

    def set_main_menubar(self):
        # .menubar.setGeometry(QRect(0, 0, 908, 21))
        self.menubar.setObjectName("menubar")

        # File Menu
        self.fileMenu = self.menubar.addMenu('&File')
        #File Menu Actions
        addCharAction = QAction("&Add Character", self)
        manageCharAction = QAction("&Manage Character", self)
        exitAction = QAction("&Exit", self)
        #File Menu Action Triggers
        addCharAction.triggered.connect(self.addCharacterTriggered)
        # manageCharAction.triggered.connect()
        exitAction.triggered.connect(self.exitTriggered)

        self.fileMenu.addAction(addCharAction)
        self.fileMenu.addAction(manageCharAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(exitAction)

        # Plans Menu
        self.plansMenu = self.menubar.addMenu('&Plans')
        addPlanAction = QAction("&Add Plan", self)
        createSkillQueuePlanAction = QAction("&Create Plan from Skillqueue", self)
        importPlanfromFileAction = QAction("&Import Plan from File", self)
        managePlanPlanAction = QAction("&Manage Plans", self)

        self.plansMenu.addAction(addPlanAction)
        self.plansMenu.addAction(createSkillQueuePlanAction)
        self.plansMenu.addAction(importPlanfromFileAction)
        self.plansMenu.addAction(managePlanPlanAction)

        # Tools Menu
        self.toolsMenu = self.menubar.addMenu('&Tools')
        manageNotificationsAction = QAction("&Manage Notifications", self)
        optionsAction = QAction("&Options", self)

        self.toolsMenu.addAction(manageNotificationsAction)
        self.toolsMenu.addSeparator()
        self.toolsMenu.addAction(optionsAction)

        #Help Menu
        self.helpMenu = self.menubar.addMenu('&Help')
        helpAction = QAction("&Help", self)
        aboutAction = QAction("&About", self)

        self.helpMenu.addAction(helpAction)
        self.helpMenu.addSeparator()
        self.helpMenu.addAction(aboutAction)


    def set_frame(self):
        self.frame_query.setFrameShape(QFrame.StyledPanel)
        self.frame_query.setFrameShadow(QFrame.Raised)

    def set_status_bar(self):
        self.statusbar.setMinimumSize(QSize(0, 18))
        font = QFont()
        font.setPointSize(9)
        self.statusbar.setFont(font)

    ################
    #
    # Benubar Action trigger Functions
    #
    ################

    def exitTriggered(self):
         self.close()

    def addCharacterTriggered(self):
        login()  # Start Login Process to Eve SSO (service.esi.login())
        self.tab_widget.createCharacterTab()
