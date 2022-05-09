import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from form.controller import widget, context


class DetailProductWindow(QMainWindow):
    def __init__(self):
        super(DetailProductWindow, self).__init__()
        loadUi(os.path.join(os.path.dirname(__file__),
               "..", "view/productDetail.ui"), self)
        self.BackBtn.clicked.connect(self.back)
        self.nameLabel.setText(context["nama_product"])
        self.stockLabel.setText(context["stock_product"])
        self.CariTeknisiBtn.clicked.connect(self.cariTeknisi)

    def refresh(self):
        self.nameLabel.setText(context["nama_product"])
        self.stockLabel.setText(str(context["stock_product"]))

    def back(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

    def cariTeknisi(self):
        widget.setCurrentIndex(widget.currentIndex()+1)
