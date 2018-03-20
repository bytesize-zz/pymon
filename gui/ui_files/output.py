# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'overviewtab.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1033, 819)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 1031, 791))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 50, 891, 541))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget.setMaximumSize(QtCore.QSize(320, 120))
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget_2.setMaximumSize(QtCore.QSize(320, 120))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)


        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

