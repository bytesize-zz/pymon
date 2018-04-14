# https://github.com/MTG/dunya-desktop/blob/master/dunyadesktop_app/general_design.py

# ToDo: Optimize Imports
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from service.esi import Esi
import config
from Lib import queue

# Import of neccessary Widgets
from gui.widgets.mainTabWidget import MainTabWidget
from gui.charManagerWindow import CharManagerWindow

class GeneralMainDesign(QMainWindow):
    """General design of the main window"""
    def __init__(self):
        super().__init__()
        self.init_MainWindow()

        self.gui_queue = queue.Queue()

    def init_MainWindow(self):
        self.set_main_window()

        self.createLayout()

        # query frame
        # self.frame_query = QueryFrame()
        # self._set_frame()
        # layout.addWidget(self.frame_query)

        # status bar
        self.statusbar = QStatusBar(self)
        self.set_status_bar()
        self.setStatusBar(self.statusbar)

        # MainMenuBar
        self.menubar = self.menuBar()
        self.set_main_menubar()

        # Tab Widget
        self.createTabwidget()

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
        # Standard Values for this Window
        standard_width = 960
        standard_height = 720
        minimum_width = 544
        minimum_height = 480

        """Sets the size policies of the main window"""
        self.resize(standard_width, standard_height)
        size_policy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)
        self.setMinimumSize(QSize(minimum_width, minimum_height))

        # main window icon
        self.setWindowIcon(QIcon(""))
        self.setWindowTitle(config.APP_NAME)

    def set_main_menubar(self):
        # Create Menu Bar with Actions
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
        manageCharAction.triggered.connect(self.manageCharacterTriggered)
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
        #reloadUI = QAction("&Reload UI", self)
        optionsAction = QAction("&Options", self)

        #reloadUI.triggered.connect(self.writeToQueue)

        self.toolsMenu.addAction(manageNotificationsAction)
        #self.toolsMenu.addAction(reloadUI)
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
    # Menubar Action trigger Functions
    #
    ################

    def exitTriggered(self):
        # Close the Application
         self.close()

    def addCharacterTriggered(self):
        self.startUpdateTimer()  # ToDo: Configure Timer for a maximum run time
        Esi(self.gui_queue)

    def manageCharacterTriggered(self):
        # Open New Window Character Manager
        self.charManager = CharManagerWindow(self)
        self.charManager.show()

    def deleteLayout(self):
        print("Deleting Layout..")
        while self.layout.count() > 0:
            item = self.layout.takeAt(0)
            if not item:
                continue

            w = item.widget()
            if w:
                w.deleteLater()
        print("Layout deleted.")

    def createLayout(self):
        print("creating Layout...")
        self.centralwidget = QWidget(self)
        self.layout = QVBoxLayout(self.centralwidget)
        self.layout.setContentsMargins(0, 0, 2, 0)
        self.layout.setSpacing(0)
        self.setCentralWidget(self.centralwidget)
        print("Layout created.")

    def createTabwidget(self):
        print("creating Tabwidget ...")
        self.tab_widget = MainTabWidget(self)
        self.layout.addWidget(self.tab_widget)
        print("Tabwidget created.")

    def reprintUI(self):
        # repaint Function: delete old layout and children, then paint a new one
        # should only be neccessary after adding a new Character
        try:
            self.deleteLayout()
            self.createLayout()
            self.createTabwidget()
        except Exception as e:
            print(e)

    def hearAtQueue(self):
        if self.gui_queue.empty() is False:
            msg = self.gui_queue.get()
            if msg == "Reprint MainWindow":
                self.reprintUI()
                self.timer.stop()

    def startUpdateTimer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.hearAtQueue)
        self.timer.setSingleShot(False)
        self.timer.start(1000)
