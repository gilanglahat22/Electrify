import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from form.controller import widget, success_notification
from PyQt5 import QtWidgets,QtCore
from model.orderitem import OrderItem
from model.userdetail import UserDetail
from model.orders import Order
from controller import get_records, get_one_record
from sqlalchemy.sql import select


class DaftarPermintaanWindow(QMainWindow):
    def __init__(self):
        super(DaftarPermintaanWindow, self).__init__()
        loadUi(os.path.join(os.path.dirname(__file__),
               "..", "view/DaftarPermintaan.ui"), self)
        self.HomeBtn.clicked.connect(self.gotoHome)

        data = get_records(select(OrderItem))
        for i in data:
            data2 = get_one_record(select(Order).where(Order.order_id == i.order_id))
            self.new_order(i.order_id,i.product_id,i.quantity,data2.customer_id)

    def gotoHome(self):
        widget.setCurrentIndex(widget.currentIndex()-4)

    def new_order(self, order_id,product_id,quantity, user_id):

        cardPermintaan = QtWidgets.QWidget(self.scrollRequestList)
        cardPermintaan.setMinimumSize(QtCore.QSize(0, 100))
        cardPermintaan.setMaximumSize(QtCore.QSize(16777215, 150))
        cardPermintaan.setStyleSheet("background-color: #fefeff")
        cardPermintaan.setObjectName("cardPermintaan")
        horizontalLayout_3 = QtWidgets.QHBoxLayout(cardPermintaan)
        horizontalLayout_3.setObjectName("horizontalLayout_3")
        framtitle = QtWidgets.QFrame(cardPermintaan)
        framtitle.setMinimumSize(QtCore.QSize(200, 0))
        framtitle.setMaximumSize(QtCore.QSize(200, 16777215))
        framtitle.setObjectName("framtitle")
        verticalLayout_4 = QtWidgets.QVBoxLayout(framtitle)
        verticalLayout_4.setObjectName("verticalLayout_4")
        label_order = QtWidgets.QLabel(framtitle)
        label_order.setObjectName("label_order")
        label_order.setText("order id")
        verticalLayout_4.addWidget(label_order)
        label_user = QtWidgets.QLabel(framtitle)
        label_user.setObjectName("label_user")
        label_user.setText("user id")
        verticalLayout_4.addWidget(label_user)
        label_product = QtWidgets.QLabel(framtitle)
        label_product.setObjectName("label_product")
        label_product.setText("product")
        verticalLayout_4.addWidget(label_product)
        label_quantity = QtWidgets.QLabel(framtitle)
        label_quantity.setObjectName("label_quantity")
        label_quantity.setText("quantity")
        verticalLayout_4.addWidget(label_quantity)
        horizontalLayout_3.addWidget(framtitle)
        frameinput = QtWidgets.QFrame(cardPermintaan)
        frameinput.setMinimumSize(QtCore.QSize(0, 0))
        frameinput.setMaximumSize(QtCore.QSize(16777215, 16777215))
        frameinput.setObjectName("frameinput")
        verticalLayout_8 = QtWidgets.QVBoxLayout(frameinput)
        verticalLayout_8.setObjectName("verticalLayout_8")
        orderinput = QtWidgets.QLabel(frameinput)
        orderinput.setObjectName("orderinput")
        orderinput.setText(order_id)
        verticalLayout_8.addWidget(orderinput)
        userinput = QtWidgets.QLabel(frameinput)
        userinput.setObjectName("userinput")
        userinput.setText(user_id)
        verticalLayout_8.addWidget(userinput)
        productinput = QtWidgets.QLabel(frameinput)
        productinput.setObjectName("productinput")
        productinput.setText(product_id)
        verticalLayout_8.addWidget(productinput)
        quantityinput = QtWidgets.QLabel(frameinput)
        quantityinput.setObjectName("quantityinput")
        quantityinput.setText(str(quantity))
        verticalLayout_8.addWidget(quantityinput)
        horizontalLayout_3.addWidget(frameinput)
        frameBtn = QtWidgets.QFrame(cardPermintaan)
        frameBtn.setMaximumSize(QtCore.QSize(100, 16777215))
        frameBtn.setObjectName("frameBtn")
        verticalLayout = QtWidgets.QVBoxLayout(frameBtn)
        verticalLayout.setObjectName("verticalLayout")
        AcceptBtn = QtWidgets.QPushButton(frameBtn)
        AcceptBtn.setMinimumSize(QtCore.QSize(0, 30))
        AcceptBtn.setStyleSheet("QPushButton#AcceptBtn{\n"
"background-color:rgb(0, 0, 0);\n"
"color:rgba(255,255,255,210);\n"
"border-radius:14px;\n"
"font: 11pt \"MS Shell Dlg 2\"; color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#AcceptBtn:hover{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#AcceptBtn:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(150, 123, 111, 255);\n"
"};")
        AcceptBtn.setObjectName("AcceptBtn")
        verticalLayout.addWidget(AcceptBtn)
        horizontalLayout_3.addWidget(frameBtn)
        AcceptBtn.setText("Accept")
        AcceptBtn.clicked.connect(self.accept_order)
        self.verticalLayout_5.addWidget(cardPermintaan)
    
    def accept_order(self):
        success_notification("Berhasil Menerima Pesanan", "Sistem Pesanan")
        self.gotoHome()