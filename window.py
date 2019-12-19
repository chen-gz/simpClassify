# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui',
# licensing of 'window.ui' applies.
#
# Created: Tue Dec 17 15:27:33 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(312, 174)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(60, 120, 80, 18))
        self.openButton.setObjectName("openButton")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(170, 120, 80, 18))
        self.startButton.setObjectName("startButton")
        self.pathEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pathEdit.setGeometry(QtCore.QRect(50, 60, 221, 31))
        self.pathEdit.setObjectName("pathEdit")
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(50, 10, 201, 31))
        self.statusLabel.setObjectName("statusLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.openButton, QtCore.SIGNAL("clicked()"), MainWindow.getPath)
        QtCore.QObject.connect(self.startButton, QtCore.SIGNAL("clicked()"), MainWindow.start)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.openButton.setText(QtWidgets.QApplication.translate("MainWindow", "open", None, -1))
        self.startButton.setText(QtWidgets.QApplication.translate("MainWindow", "start", None, -1))
        self.statusLabel.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))

