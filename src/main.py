import sys

from form.login import LoginWindow
from form.Pelanggan import PelangganWindow
from form.Admin import AdminWindow
from form.Teknisi import TeknisiWindow
from form.DaftarPermintaan import DaftarPermintaanWindow
from form.DetailProduct import DetailProductWindow
from form.firstpage import FirstWindow
from form.sign_up import SignUp_Window
from form.controller import widget, app
from form.DaftarProduct import DaftarProductWindow
from form.CardTeknisi import CardTeknisiWindow
from form.TicketWindow import TicketWindow
from controller.Auth import login as login_db
from form.DaftarTeknisi import DaftarTeknisiWindow
from form.MyOrder import MyOrderWindow
from form.controller import context

First = FirstWindow()
Register = SignUp_Window()
login = LoginWindow()
pelanggan = PelangganWindow()
teknisi = TeknisiWindow()
admin = AdminWindow()
cardTeknisi = CardTeknisiWindow()
daftarproduct = DaftarProductWindow()
detailproduct = DetailProductWindow()
daftarpermintaan = DaftarPermintaanWindow()
myorder = MyOrderWindow()
daftarteknisi = DaftarTeknisiWindow()

widget.addWidget(First)
widget.addWidget(Register)
widget.addWidget(login)
widget.addWidget(pelanggan)
widget.addWidget(teknisi)
widget.addWidget(daftarproduct)
widget.addWidget(detailproduct)
widget.addWidget(daftarteknisi)
widget.addWidget(daftarpermintaan)
widget.addWidget(myorder)
widget.addWidget(admin)
widget.addWidget(TicketWindow())

context["detail-product-updater"] = detailproduct.refresh

widget.setCurrentIndex(0)
widget.setFixedWidth(1119)
widget.setFixedHeight(889)
widget.show()

try:
    sys.exit(app.exec_())
except SystemExit:
    print("Exit")
