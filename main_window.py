# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from doc import generate

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class Ui_MainWindow(object):

    # init custom vars
    items = ""
    filename = []
    key = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 50, 411, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
    #    self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
    #    self.lineEdit.setObjectName("lineEdit")
    #    self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
            # Call start
        self.pushButton.clicked.connect(self.start)
        self.gridLayout.addWidget(self.pushButton, 3, 2, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 130, 411, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(443, -30, 20, 601))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(480, 50, 192, 51))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
            # Onclick search file
        self.pushButton_2.clicked.connect(self.searchFiles)

        self.gridLayout_2.addWidget(self.pushButton_2, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
    #    self.label.setText(_translate("MainWindow", "Ersetze:"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.label_3.setText(_translate("MainWindow", "Teilnehmer"))
        self.label_4.setText(_translate("MainWindow", "Mehrere Teilnehmer mit komma trennen"))
        self.label_5.setText(_translate("MainWindow", "Dokument auswählen"))
        self.pushButton_2.setText(_translate("MainWindow", "Durchsuchen..."))
        


    # Custom functions:

    def searchFiles(self):
        _filename = QFileDialog.getOpenFileName(None, 'Open File')
        self.lineEdit_3.setText(_filename[0])

        
   

        global key
        key = 'participant'
        #self.lineEdit = key

        global filename
        filename = _filename[0]

       

    def start(self):
       
        foo = self.textEdit.toPlainText()
        items = foo.split(',')
        

        generate(filename, items, key)
        print(items)

       
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
