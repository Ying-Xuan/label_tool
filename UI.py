# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tool/ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QMenuBar, QStatusBar, QApplication, QMainWindow
from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication, Qt
from PyQt5.QtGui import QFont

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 850)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.open_folder_buttom = QPushButton(self.centralwidget)
        self.open_folder_buttom.setGeometry(QRect(300, 20, 171, 51))
        font = QFont()
        font.setPointSize(20)
        self.open_folder_buttom.setFont(font)
        self.open_folder_buttom.setLayoutDirection(Qt.RightToLeft)
        self.open_folder_buttom.setObjectName("open_folder_buttom")
        self.img_label = QLabel(self.centralwidget)
        self.img_label.setGeometry(QRect(30, 160, 800, 600))
        self.img_label.setObjectName("img_label")
        self.open_csv_buttom = QPushButton(self.centralwidget)
        self.open_csv_buttom.setGeometry(QRect(70, 20, 171, 51))
        font = QFont()
        font.setPointSize(20)
        self.open_csv_buttom.setFont(font)
        self.open_csv_buttom.setLayoutDirection(Qt.RightToLeft)
        self.open_csv_buttom.setObjectName("open_csv_buttom")
        self.img_path_label = QLabel(self.centralwidget)
        self.img_path_label.setGeometry(QRect(70, 90, 1151, 51))
        font = QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.img_path_label.setFont(font)
        self.img_path_label.setObjectName("img_path_label")
        self.left_buttom = QPushButton(self.centralwidget)
        self.left_buttom.setGeometry(QRect(910, 190, 131, 71))
        font = QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        self.left_buttom.setFont(font)
        self.left_buttom.setObjectName("left_buttom")
        self.last_buttom = QPushButton(self.centralwidget)
        self.last_buttom.setGeometry(QRect(1190, 450, 81, 61))
        font = QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.last_buttom.setFont(font)
        self.last_buttom.setObjectName("last_buttom")
        self.right_buttom = QPushButton(self.centralwidget)
        self.right_buttom.setGeometry(QRect(1090, 190, 131, 71))
        font = QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        self.right_buttom.setFont(font)
        self.right_buttom.setObjectName("right_buttom")
        self.invalid_buttom = QPushButton(self.centralwidget)
        self.invalid_buttom.setGeometry(QRect(1000, 310, 131, 71))
        font = QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        self.invalid_buttom.setFont(font)
        self.invalid_buttom.setObjectName("invalid_buttom")
        self.next_buttom = QPushButton(self.centralwidget)
        self.next_buttom.setGeometry(QRect(900, 450, 281, 61))
        font = QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        self.next_buttom.setFont(font)
        self.next_buttom.setObjectName("next_buttom")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 1300, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open_folder_buttom.setText(_translate("MainWindow", "open folder"))
        self.img_label.setText(_translate("MainWindow", "TextLabel"))
        self.open_csv_buttom.setText(_translate("MainWindow", "open csv"))
        self.img_path_label.setText(_translate("MainWindow", "img_path"))
        self.left_buttom.setText(_translate("MainWindow", "左眼"))
        self.last_buttom.setText(_translate("MainWindow", "上一張"))
        self.right_buttom.setText(_translate("MainWindow", "右眼"))
        self.invalid_buttom.setText(_translate("MainWindow", "無效"))
        self.next_buttom.setText(_translate("MainWindow", "下一張"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

