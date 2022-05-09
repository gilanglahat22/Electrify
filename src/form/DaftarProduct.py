import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from form.controller import widget, context
from form.CardProduct import CardProductWindow
from controller import insert_record, get_records
from sqlalchemy.sql import select
from model.product import Product

class DaftarProductWindow(QMainWindow):
    def __init__(self):
        super(DaftarProductWindow, self).__init__()
        loadUi(os.path.join(os.path.dirname(__file__),
               "..", "view/searchProduct.ui"), self)
        self.backButton.clicked.connect(self.back)
        datas = get_records(
            select(Product)
        )

        for i in datas:
            print(i.name)
            print(i.stock)
            cardproduct = CardProductWindow()
            cardproduct.set_data(i.name, i.stock)
            cardproduct.refresh()
            self.verticalLayout_5.addWidget(cardproduct)
    
    def back(self):
        widget.setCurrentIndex(widget.currentIndex()-2)
