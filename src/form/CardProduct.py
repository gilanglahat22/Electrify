import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMainWindow
from PyQt5.uic import loadUi
from model.product import Product
from form.controller import widget, context
from sqlalchemy.sql import select
from controller import get_one_record, insert_record

class CardProductWindow(QMainWindow):
    
    nama_product = ""
    stock_product = ""
    product_id = ""
    
    def __init__(self):
        super(CardProductWindow, self).__init__()
        loadUi(os.path.join(os.path.dirname(__file__),
               "..", "view/cardProduct.ui"), self)
        self.detailButton.clicked.connect(self.gotoDetailProduct)

    def set_data(self, name, stock):
        self.nama_product = name
        self.stock_product = stock
        data = get_one_record(
            select(Product.product_id).where(Product.name == self.nama_product, Product.stock == self.stock_product)
        )
        self.product_id = data

    def refresh(self):
        self.namaProduct.setText(self.nama_product)
        self.stockLabel.setText(str(self.stock_product))

    def gotoDetailProduct(self):
        global context
        context["product_id"] = self.product_id
        context["nama_product"] = self.nama_product
        context["stock_product"] = self.stock_product
        context["detail-product-updater"]()
        widget.setCurrentIndex(widget.currentIndex()+1)