# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\54720\Documents\codeblocks\aima-python\Npuzzle.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(617, 774)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_restart = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_restart.setGeometry(QtCore.QRect(30, 580, 112, 34))
        self.pushButton_restart.setObjectName("pushButton_restart")
        self.pushButton_solve = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_solve.setGeometry(QtCore.QRect(30, 680, 112, 34))
        self.pushButton_solve.setObjectName("pushButton_solve")
        self.lineEdit_Message = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Message.setGeometry(QtCore.QRect(160, 580, 421, 131))
        self.lineEdit_Message.setText("")
        self.lineEdit_Message.setReadOnly(True)
        self.lineEdit_Message.setObjectName("lineEdit_Message")
        self.GameName = QtWidgets.QLabel(self.centralwidget)
        self.GameName.setGeometry(QtCore.QRect(260, 30, 81, 18))
        self.GameName.setObjectName("GameName")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 60, 551, 501))
        self.widget.setObjectName("widget")
        self.ButtonLayout = QtWidgets.QGridLayout(self.widget)
        self.ButtonLayout.setContentsMargins(0, 0, 0, 0)
        self.ButtonLayout.setObjectName("ButtonLayout")
        # self.pushButton = QtWidgets.QPushButton(self.widget)
        # self.pushButton.setObjectName("pushButton")
        # self.ButtonLayout.addWidget(self.pushButton, 0, 0)
        # self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        # self.pushButton_3.setObjectName("pushButton_3")
        # self.ButtonLayout.addWidget(self.pushButton_3, 0, 1)
        # self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        # self.pushButton_2.setObjectName("pushButton_2")
        # self.ButtonLayout.addWidget(self.pushButton_2, 0, 2)
        # self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        # self.pushButton_5.setObjectName("pushButton_5")
        # self.ButtonLayout.addWidget(self.pushButton_5, 1, 0)
        # self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        # self.pushButton_6.setObjectName("pushButton_6")
        # self.ButtonLayout.addWidget(self.pushButton_6, 1, 1)
        # self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        # self.pushButton_8.setObjectName("pushButton_8")
        # self.ButtonLayout.addWidget(self.pushButton_8, 1, 2)
        # self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        # self.pushButton_4.setObjectName("pushButton_4")
        # self.ButtonLayout.addWidget(self.pushButton_4, 2, 0)
        # self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        # self.pushButton_9.setObjectName("pushButton_9")
        # self.ButtonLayout.addWidget(self.pushButton_9, 2, 1)
        # self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        # self.pushButton_7.setObjectName("pushButton_7")
        # self.ButtonLayout.addWidget(self.pushButton_7, 3, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 617, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_restart.setText(_translate("MainWindow", "重新随机"))
        self.pushButton_solve.setText(_translate("MainWindow", "机器解答"))
        self.GameName.setText(_translate("MainWindow", "TextLabel"))

