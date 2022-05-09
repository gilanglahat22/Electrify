import os

from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from form.controller import widget, success_notification, failed_notification


class TeknisiWindow(QMainWindow):
    def __init__(self):
        super(TeknisiWindow, self).__init__()
        loadUi(os.path.join(os.path.dirname(__file__),
               "..", "view/Teknisi.ui"), self)
        self.ReqListBtn.clicked.connect(self.gotoDaftarPermintaan)

    def gotoDaftarPermintaan(self):
        widget.setCurrentIndex(widget.currentIndex()+4)
