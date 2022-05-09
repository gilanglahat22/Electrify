import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from form.controller import widget


class FirstWindow(QMainWindow):
    def __init__(self):
        super(FirstWindow, self).__init__()
        loadUi(os.path.join(os.path.dirname(__file__), "..", "view/firstpage.ui"), self)
        self.sign_in.clicked.connect(self.goToSign_in)
        self.sign_up.clicked.connect(self.goToSign_up)

    def goToSign_up(self):
        widget.setCurrentIndex(widget.currentIndex()+1)
    def goToSign_in(self):
        widget.setCurrentIndex(widget.currentIndex()+2)
        