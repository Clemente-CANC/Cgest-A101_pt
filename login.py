# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 700)
        MainWindow.setMinimumSize(QtCore.QSize(500, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1155, 812))
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/Images/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-image: url(:/image/Images/foto.png);\n"
"background-position: center;")
        self.window = QtWidgets.QWidget(MainWindow)
        self.window.setObjectName("window")
        self.verticalLayout_main = QtWidgets.QVBoxLayout(self.window)
        self.verticalLayout_main.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_main.setSpacing(0)
        self.verticalLayout_main.setObjectName("verticalLayout_main")
        self.top_line = QtWidgets.QFrame(self.window)
        self.top_line.setMaximumSize(QtCore.QSize(16777215, 35))
        self.top_line.setStyleSheet("background-color:rgb(63, 63, 63, 190);\n"
"background-image: url();")
        self.top_line.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_line.setObjectName("top_line")
        self.horizontalLayout_top = QtWidgets.QHBoxLayout(self.top_line)
        self.horizontalLayout_top.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_top.setSpacing(0)
        self.horizontalLayout_top.setObjectName("horizontalLayout_top")
        self.frame_notification = QtWidgets.QFrame(self.top_line)
        self.frame_notification.setMaximumSize(QtCore.QSize(430, 16777215))
        self.frame_notification.setStyleSheet("background-color: rgb(124, 118, 115);\n"
"border-radius: 5px;")
        self.frame_notification.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_notification.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_notification.setObjectName("frame_notification")
        self.horizontalLayout_erro = QtWidgets.QHBoxLayout(self.frame_notification)
        self.horizontalLayout_erro.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_erro.setObjectName("horizontalLayout_erro")
        self.label_notification_message = QtWidgets.QLabel(self.frame_notification)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_notification_message.setFont(font)
        self.label_notification_message.setStyleSheet("color: rgb(230, 230, 231);")
        self.label_notification_message.setAlignment(QtCore.Qt.AlignCenter)
        self.label_notification_message.setObjectName("label_notification_message")
        self.horizontalLayout_erro.addWidget(self.label_notification_message)
        self.pushButton_close_notification = QtWidgets.QPushButton(self.frame_notification)
        self.pushButton_close_notification.setMaximumSize(QtCore.QSize(22, 22))
        self.pushButton_close_notification.setStyleSheet("QPushButton{\n"
"    background-image: url(:/image/Images/cil-x.png);\n"
"    background-position: center;\n"
"    background-repeat: none;\n"
"    background-color: rgb(161, 97, 79);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(212, 127, 104);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(212, 127, 104);\n"
"}\n"
"")
        self.pushButton_close_notification.setText("")
        self.pushButton_close_notification.setObjectName("pushButton_close_notification")
        self.horizontalLayout_erro.addWidget(self.pushButton_close_notification)
        self.horizontalLayout_top.addWidget(self.frame_notification)
        self.verticalLayout_main.addWidget(self.top_line)
        self.area_central = QtWidgets.QFrame(self.window)
        self.area_central.setStyleSheet("background-color: rgb(114, 115, 117, 0);\n"
        "background-image: url();\n"
        "\n"
        "\n"
        "")
        self.area_central.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.area_central.setFrameShadow(QtWidgets.QFrame.Raised)
        self.area_central.setObjectName("area_central")
        self.gridLayout_areacent = QtWidgets.QGridLayout(self.area_central)
        self.gridLayout_areacent.setObjectName("gridLayout_areacent")
        self.frame_logo = QtWidgets.QFrame(self.area_central)
        self.frame_logo.setEnabled(True)
        self.frame_logo.setMaximumSize(QtCore.QSize(16777215, 110))
        self.frame_logo.setStyleSheet("background-image: url(:/image/Images/canc_BS_logo.png);\n"
        "background-color: rgb(183, 110, 90, 150);\n"
        "border-radius: 45px;\n"
        "border: 4px solid rgb(183, 110, 90)\n"
        "")
        self.frame_logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_logo.setObjectName("frame_logo")
        self.gridLayout_areacent.addWidget(self.frame_logo, 0, 0, 1, 1)
        self.layout_main = QtWidgets.QFrame(self.area_central)
        self.layout_main.setMaximumSize(QtCore.QSize(450, 500))
        self.layout_main.setStyleSheet("background-color: rgb(14, 9, 9, 200);\n"
        "color: rgb(182, 157, 139);\n"
        "border-radius: 13px;\n"
        "background-image: url();")
        self.layout_main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.layout_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.layout_main.setObjectName("layout_main")
        self.label_title_text = QtWidgets.QLabel(self.layout_main)
        self.label_title_text.setGeometry(QtCore.QRect(130, 0, 191, 131))
        font = QtGui.QFont()
        font.setFamily("Alba Super")
        font.setPointSize(48)
        self.label_title_text.setFont(font)
        self.label_title_text.setStyleSheet("QLabel{    \n"
        "    color: rgb(183, 110, 90);\n"
        "    background-color: rgb(184, 170, 200, 0);\n"
        "}\n"
        "\n"
        "QLabel:hover{\n"
        "    \n"
        "    color:  rgb(201, 131, 90);\n"
        "}")
        self.label_title_text.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_text.setObjectName("label_title_text")
        self.frame_user_image = QtWidgets.QLabel(self.layout_main)
        self.frame_user_image.setGeometry(QtCore.QRect(159, 145, 131, 131))
        self.frame_user_image.setStyleSheet("QFrame{\n"
        "    border: 6px  solid rgb(161, 97, 79);\n"
        "    background-image: url(:/image/Images/profile-user.png);\n"
        "    background-position: center;\n"
        "    border-radius: 10px;\n"
        "    \n"
        "}\n"
        "\n"
        "QFrame:hover{\n"
        "    border: 6px  solid rgb(201, 131, 90);\n"
        "}")
        self.frame_user_image.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_user_image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_user_image.setPixmap(QtGui.QPixmap("Image/profile-user.png"))
        self.frame_user_image.setObjectName("frame_user_image")
        self.lineEdit_name_user = QtWidgets.QLineEdit(self.layout_main)
        self.lineEdit_name_user.setGeometry(QtCore.QRect(100, 290, 250, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.lineEdit_name_user.setFont(font)
        self.lineEdit_name_user.setStyleSheet("QLineEdit{\n"
        "    background-color: rgb(44, 34, 31, 160);\n"
        "    border-radius: 10px;\n"
        "    border: 2px solid rgb(161, 97, 79);\n"
        "    padding: 10px;\n"
        "}\n"
        "\n"
        "QLineEdit:hover{\n"
        "    border: 2px solid rgb(201, 131, 90);\n"
        "}\n"
        "\n"
        "QLineEdit:focus{\n"
        "    border: 2px solid rgb(201, 131, 90);\n"
        "}")
        self.lineEdit_name_user.setInputMask("")
        self.lineEdit_name_user.setText("")
        self.lineEdit_name_user.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_name_user.setPlaceholderText("Nome do usuário")
        self.lineEdit_name_user.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_name_user.setClearButtonEnabled(False)
        self.lineEdit_name_user.setObjectName("lineEdit_name_user")
        self.lineEdit_password = QtWidgets.QLineEdit(self.layout_main)
        self.lineEdit_password.setGeometry(QtCore.QRect(100, 350, 250, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("QLineEdit{\n"
        "    background-color: rgb(44, 34, 31, 160);\n"
        "    border-radius: 10px;\n"
        "    border: 2px solid rgb(161, 97, 79);\n"
        "    padding: 10px;\n"
        "}\n"
        "\n"
        "QLineEdit:hover{\n"
        "    border: 2px solid rgb(201, 131, 90);\n"
        "}\n"
        "\n"
        "QLineEdit:focus{\n"
        "    border: 2px solid rgb(201, 131, 90);\n"
        "}")
        self.lineEdit_password.setInputMask("")
        self.lineEdit_password.setText("")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_password.setPlaceholderText("senha")
        self.lineEdit_password.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_password.setClearButtonEnabled(False)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.pushButton_enter = QtWidgets.QPushButton(self.layout_main)
        self.pushButton_enter.setGeometry(QtCore.QRect(100, 410, 250, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.pushButton_enter.setFont(font)
        self.pushButton_enter.setStyleSheet("QPushButton{\n"
        "    background-color: rgb(161, 97, 79);\n"
        "    border-radius: 10px;\n"
        "    padding: 10px;\n"
        "    color: rgb(230, 230, 231);\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "    border: 2px solid rgb(212, 127, 104);\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(212, 127, 104);\n"
        "}")
        self.pushButton_enter.setObjectName("pushButton_enter")
        self.pushButton_add = QtWidgets.QPushButton(self.layout_main)
        self.pushButton_add.setGeometry(QtCore.QRect(400, 10, 41, 41))
        self.pushButton_add.setStyleSheet("QPushButton{\n"
        "    \n"
        "    background-image: url(:/image/Images/add_user.png);\n"
        "    background-position: center;\n"
        "    background-repeat: none;\n"
        "    background-color: rgb(161, 97, 79);\n"
        "    border-radius: 20px;\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "    border: 2px solid rgb(212, 127, 104);\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(212, 127, 104);\n"
        "}\n"
        "")
        self.pushButton_add.setText("")
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_recover_account = QtWidgets.QPushButton(self.layout_main)
        self.pushButton_recover_account.setGeometry(QtCore.QRect(120, 465, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.pushButton_recover_account.setFont(font)
        self.pushButton_recover_account.setStyleSheet("QPushButton{\n"
        "    background-color: rgb(184, 170, 200, 0);\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "    \n"
        "    color:  rgb(201, 131, 90);\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "    color:  rgb(190, 100, 80);\n"
        "}")
        self.pushButton_recover_account.setObjectName("pushButton_recover_account")
        self.pushButton_password = QtWidgets.QPushButton(self.layout_main)
        self.pushButton_password.setGeometry(QtCore.QRect(305, 355, 41, 41))
        self.pushButton_password.setStyleSheet("QPushButton{\n"
        "    background-image: url(:/image/Images/closed_lock1.png);\n"
        "    background-position: center;\n"
        "    background-repeat: none;\n"
        "    background-color: rgb(161, 97, 79, 0);\n"
        "    border-radius: 20px;\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "    border: 2px solid rgb(212, 127, 104);\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(212, 127, 104);\n"
        "}\n"
        "")
        self.pushButton_password.setText("")
        self.pushButton_password.setObjectName("pushButton_password")
        self.pushButton_about = QtWidgets.QPushButton(self.layout_main)
        self.pushButton_about.setGeometry(QtCore.QRect(10, 450, 41, 41))
        self.pushButton_about.setStyleSheet("QPushButton{\n"
        "    background-image: url(:/image/Images/about.png);\n"
        "    background-position: center;\n"
        "    background-repeat: none;\n"
        "    background-color: rgb(161, 97, 79);\n"
        "    border-radius: 20px;\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "    border: 2px solid rgb(212, 127, 104);\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(212, 127, 104);\n"
        "}\n"
        "")
        self.pushButton_about.setText("")
        self.pushButton_about.setObjectName("pushButton_about")
        self.gridLayout_areacent.addWidget(self.layout_main, 1, 0, 1, 1)
        self.verticalLayout_main.addWidget(self.area_central)
        self.down_line = QtWidgets.QFrame(self.window)
        self.down_line.setMaximumSize(QtCore.QSize(16777215, 30))
        self.down_line.setStyleSheet("background-color:rgb(63, 63, 63, 190);\n"
        "background-image: url();")
        self.down_line.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.down_line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.down_line.setObjectName("down_line")
        self.horizontalLayout_down = QtWidgets.QHBoxLayout(self.down_line)
        self.horizontalLayout_down.setObjectName("horizontalLayout_down")
        spacerItem = QtWidgets.QSpacerItem(911, 9, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_down.addItem(spacerItem)
        self.label_credit = QtWidgets.QLabel(self.down_line)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(10)
        self.label_credit.setFont(font)
        self.label_credit.setStyleSheet("background-color: rgb(255, 170, 255, 0);\n"
        "color: rgb(230, 230, 231);")
        self.label_credit.setObjectName("label_credit")
        self.horizontalLayout_down.addWidget(self.label_credit)
        self.verticalLayout_main.addWidget(self.down_line)
        MainWindow.setCentralWidget(self.window)

        self.retranslateUi(MainWindow)
        self.lineEdit_name_user.textEdited['QString'].connect(self.frame_notification.hide)
        self.lineEdit_password.textEdited['QString'].connect(self.frame_notification.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cgest "))
        self.label_notification_message.setText(_translate("MainWindow", "Erro"))
        self.label_title_text.setText(_translate("MainWindow", "<html><head/><body><p>Login</p></body></html>"))
        self.pushButton_enter.setText(_translate("MainWindow", "Entrar"))
        self.pushButton_recover_account.setText(_translate("MainWindow", "Esqueci a minha senha"))
        self.label_credit.setText(_translate("MainWindow", "Criado por : Clement Alberto N. Cazadi"))
import resource


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
