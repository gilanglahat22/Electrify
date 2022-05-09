import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from controller.Auth import login
from form.controller import widget, context, failed_notification, success_notification, error_notification

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi(os.path.join(os.path.dirname(__file__), "..", "view/login.ui"), self)
        self.pushButton.clicked.connect(self.goToMainwindow)
        self.create_account.clicked.connect(self.goToSignUp)
        self.password_box.setEchoMode(QtWidgets.QLineEdit.Password)

    def goToMainwindow(self):
        global context
        try:
            islogin, id = login(self.Username.text(), self.password_box.text(), self.Role.currentText())
            if islogin == True:
                if(self.Role.currentText() == "Pelanggan"):
                    widget.setCurrentIndex(widget.currentIndex()+1)
                elif (self.Role.currentText() == "Teknisi"):
                    widget.setCurrentIndex(widget.currentIndex()+2)
                    widget.currentWidget().label_name.setText(self.Username.text())
                else:
                    widget.setCurrentIndex(widget.currentIndex()+3)
                username = self.Username.text()
                print(username)
                context["user_id"] = id
                success_notification("Berhasil Login", "Sukses")
            else:
                failed_notification("Pasangan Username, Password, dan Role tidak ditemukan", "Gagal Login")
        except Exception as e:
            error_notification("Terjadi kesalahan saat melakukan login", e, "Sistem Login")

    def goToSignUp(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
