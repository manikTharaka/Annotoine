# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ImLabel = QtWidgets.QLabel(self.centralwidget)
        self.ImLabel.setText("")
        self.ImLabel.setObjectName("ImLabel")
        self.horizontalLayout.addWidget(self.ImLabel)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.openVideoAction = QtWidgets.QAction(MainWindow)
        self.openVideoAction.setObjectName("openVideoAction")
        self.openImageAction = QtWidgets.QAction(MainWindow)
        self.openImageAction.setObjectName("openImageAction")
        self.actionRectangle = QtWidgets.QAction(MainWindow)
        self.actionRectangle.setObjectName("actionRectangle")
        self.actionNext = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Anno/res/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNext.setIcon(icon)
        self.actionNext.setObjectName("actionNext")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.openVideoAction)
        self.menuFile.addAction(self.openImageAction)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.actionRectangle)
        self.toolBar.addAction(self.actionNext)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.openVideoAction.setText(_translate("MainWindow", "Open Video"))
        self.openImageAction.setText(_translate("MainWindow", "Open Images"))
        self.openImageAction.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionRectangle.setText(_translate("MainWindow", "Rectangle"))
        self.actionNext.setText(_translate("MainWindow", "Next"))
        self.actionNext.setShortcut(_translate("MainWindow", "Right"))
        self.actionSave.setText(_translate("MainWindow", "Save"))

