from __future__ import print_function
import config
from service.updateHandler import UpdateHandler

# gui imports
from gui.mainwindow import GeneralMainDesign
from PyQt5.QtWidgets import QApplication

import threading
import sys
import datetime

if __name__ == "__main__":
    config.TIME_DIFFERENCE = datetime.datetime.now() - datetime.datetime.utcnow()

    app = QApplication(sys.argv)
    updateHandler = UpdateHandler()
    # updateHandler.updateAll()
    mainwindow = GeneralMainDesign()
    mainwindow.startUpdateTimer()

    updateThread = threading.Thread(target=updateHandler.updateAll, args=(mainwindow.gui_queue,))
    updateThread.name = "UpdateHandler"
    updateThread.daemon = True
    updateThread.start()

    # mainwindow.show()
    sys.exit(app.exec_())

