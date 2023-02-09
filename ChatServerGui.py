# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\pabst\PycharmProjects\Übungen\ChatServerGui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(329, 429)
        MainWindow.setWindowTitle("Chat Server")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 133, 20))
        self.lineEdit.setText("127.0.0.1")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 10, 71, 16))
        self.label_2.setText("Portnummer")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 30, 133, 20))
        self.lineEdit_2.setText("65432")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label.setText("Lokale IP Adresse")
        self.label.setObjectName("label")
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(10, 60, 231, 16))
        self.statusLabel.setText("Verbindungsstatus")
        self.statusLabel.setObjectName("statusLabel")
        self.messageEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.messageEdit.setGeometry(QtCore.QRect(10, 150, 301, 71))
        self.messageEdit.setObjectName("messageEdit")
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(10, 230, 75, 23))
        self.sendButton.setText("Senden")
        self.sendButton.setObjectName("sendButton")
        self.receivedEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.receivedEdit.setGeometry(QtCore.QRect(10, 300, 301, 71))
        self.receivedEdit.setObjectName("receivedEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 280, 121, 16))
        self.label_4.setText("Empfangene Nachrichten")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 101, 16))
        self.label_3.setText("Nachricht eingeben")
        self.label_3.setObjectName("label_3")
        self.monitorButton = QtWidgets.QPushButton(self.centralwidget)
        self.monitorButton.setGeometry(QtCore.QRect(20, 90, 141, 23))
        self.monitorButton.setCheckable(True)
        self.monitorButton.setObjectName("monitorButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 329, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.monitorButton.clicked['bool'].connect(MainWindow.start_stop_monitoring)
        self.sendButton.clicked.connect(MainWindow.send_message)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.monitorButton.setText(_translate("MainWindow", "Überwachung starten"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
