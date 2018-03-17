import sys
import config
from PyQt5.QtWidgets import QApplication, QWidget


app = QApplication(sys.argv)

window = QWidget()
window.setGeometry(50, 50, 500, 300)
window.setWindowTitle(config.APP_NAME)

window.show()
sys.exit(app.exec_())
