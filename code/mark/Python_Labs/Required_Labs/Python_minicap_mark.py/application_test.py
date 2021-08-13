from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
import csv
import json
import sys
from card_display import Card_Display as card


class Ui_MainWindow:
    def __init__(self, subject_dict):
        self.row = 0
        self.subject_dict = subject_dict

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(513, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(40, 31, 441, 221))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemSelectionChanged.connect(self.selectionChanged)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 310, 221, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.clicked.connect(self.open_card_display)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 410, 221, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 310, 221, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(270, 410, 221, 71))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(QtWidgets.QApplication.quit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 513, 22))
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
        self.pushButton_2.setText(_translate("MainWindow", "Study"))
        self.pushButton_3.setText(_translate("MainWindow", "Add Cards to Subject"))
        self.pushButton_4.setText(_translate("MainWindow", "Add New Subject"))
        self.pushButton_5.setText(_translate("MainWindow", "Quit"))

    def add_item_to_list(self, item):
        self.listWidget.addItem(item)

    def selectionChanged(self):
        self.row = self.listWidget.currentRow()
        
    def open_card_display(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = card(self.subject_dict)
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def close_application(self):
        QtWidgets.QApplication.quit()

def start_window(list_of_subjects, subject_dict):
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(subject_dict)
    ui.setupUi(MainWindow)
    for subject in list_of_subjects:
        ui.add_item_to_list(subject)
    MainWindow.show()
    sys.exit(app.exec_())
