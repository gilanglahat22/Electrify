import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from controller.Auth import register
from form.controller import widget,success_notification, error_notification


class SignUp_Window(QMainWindow):
    def __init__(self):
        super(SignUp_Window, self).__init__()
        loadUi(os.path.join(os.path.dirname(__file__), "..", "view/signup.ui"), self)
        self.sign_up.clicked.connect(self.goToSign_in)
        self.BackButton.clicked.connect(self.goBack)

    def goToSign_in(self):
        try:
            if (self.password.text() == self.confirm_password.text()):
                isRegistered = register(self.username.text(), self.password.text(), self.Role.currentText())
                if (isRegistered):
                    widget.setCurrentIndex(widget.currentIndex()+1)
                    success_notification("Berhasil mendaftarkan user", "Registrasi")
            else:
                QMessageBox.information(self, "Warning", "Your confirm password is not suitable!")
        except Exception as e:
            error_notification("Terjadi kesalahan saat menambahkan user", e, "Registrasi")
        
    def goBack(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
