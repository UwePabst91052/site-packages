# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\pabst\PycharmProjects\Übungen\ChatClientGui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(340, 423)
        MainWindow.setWindowTitle("Chat Client")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 133, 20))
        self.lineEdit.setText("127.0.0.1")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 30, 133, 20))
        self.lineEdit_2.setText("65432")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label.setText("Lokale IP Adresse")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 10, 71, 16))
        self.label_2.setText("Portnummer")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 101, 16))
        self.label_3.setText("Nachricht eingeben")
        self.label_3.setObjectName("label_3")
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(10, 250, 75, 23))
        self.sendButton.setText("Senden")
        self.sendButton.setObjectName("sendButton")
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(10, 110, 75, 23))
        self.connectButton.setText("Verbinden")
        self.connectButton.setObjectName("connectButton")
        self.disconnectButton = QtWidgets.QPushButton(self.centralwidget)
        self.disconnectButton.setGeometry(QtCore.QRect(180, 110, 75, 23))
        self.disconnectButton.setText("Trennen")
        self.disconnectButton.setObjectName("disconnectButton")
        self.messageEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.messageEdit.setGeometry(QtCore.QRect(10, 160, 301, 71))
        self.messageEdit.setObjectName("messageEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 300, 121, 16))
        self.label_4.setText("Empfangene Nachrichten")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 91, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 80, 131, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.listChatters = QtWidgets.QListWidget(self.centralwidget)
        self.listChatters.setGeometry(QtCore.QRect(150, 240, 161, 71))
        self.listChatters.setObjectName("listChatters")
        self.listMessages = QtWidgets.QListWidget(self.centralwidget)
        self.listMessages.setGeometry(QtCore.QRect(10, 320, 301, 61))
        self.listMessages.setObjectName("listMessages")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.connectButton.clicked.connect(MainWindow.connect_server)
        self.sendButton.clicked.connect(MainWindow.send_message)
        self.disconnectButton.clicked.connect(MainWindow.disconnect_server)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label_5.setText(_translate("MainWindow", "Chat Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
