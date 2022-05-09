import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.uic import loadUi
from form.controller import widget

class PelangganWindow(QMainWindow):
    def __init__(self):
        super(PelangganWindow, self).__init__()
        loadUi(os.path.join(os.path.dirname(__file__),
               "..", "view/Pelanggan.ui"), self)
        self.CariProductBtn.clicked.connect(self.gotoDaftarProduct)
        self.PesananAndaBtn.clicked.connect(self.gotoPesanan)
        self.ExitButton.clicked.connect(self.gotoLogin)
        self.Help.clicked.connect(self.gotoHelp)

    def gotoDaftarProduct(self):
        widget.setCurrentIndex(widget.currentIndex()+2)
    def gotoLogin(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
    def gotoPesanan(self):
        widget.setCurrentIndex(widget.currentIndex()+6)
    def gotoHelp(self):
        widget.setCurrentIndex(widget.currentIndex()+8)
    
