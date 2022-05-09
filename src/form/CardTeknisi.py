import os
import datetime
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from form.controller import widget, context, error_notification, success_notification
from model.orders import Order
from model.orderitem import OrderItem
from controller import get_one_record, insert_record
from sqlalchemy.sql import select

class CardTeknisiWindow(QMainWindow):
    
    def __init__(self):
        super(CardTeknisiWindow, self).__init__()
        loadUi(os.path.join(os.path.dirname(__file__),
               "..", "view/cardTeknisi.ui"), self)
        
        self.orderButton.clicked.connect(self.addOrder)

    def addOrder(self):
        try:
            date = datetime.datetime.now()
            newOrder = Order().set_timestamp(date).set_customer_id(context["user_id"])
            insert_record(newOrder)

            newOrderItem = OrderItem().set_order_id(newOrder.order_id).set_product_id(context["product_id"]).set_quantity(1)
            insert_record(newOrderItem)
            success_notification("Berhasil menambahkan pesanan", "Sistem Pesanan")
            widget.setCurrentIndex(3)
        except Exception as e:
            error_notification("Gagal menambahkan pesanan", e, "Sistem Pesanan")

    def setCustomerid(self, _customer_id):
        self.customer_id = _customer_id