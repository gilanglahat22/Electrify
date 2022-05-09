import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from form.CardTeknisi import CardTeknisiWindow
from form.controller import widget
from controller import insert_record, get_records
from model.credential import Credential
from sqlalchemy.sql import select

class DaftarTeknisiWindow(QMainWindow):
    
    def __init__(self):
        super(DaftarTeknisiWindow, self).__init__()
        loadUi(os.path.join(os.path.dirname(__file__),
               "..", "view/searchTeknisi.ui"), self)
        self.backButton.clicked.connect(self.back)
        
        datas = get_records(
            select(Credential).where(Credential.role == 'Teknisi')
        )

        for i in datas:
            cardteknisi = CardTeknisiWindow()
            cardteknisi.namaTeknisi.setText(i.username)
            cardteknisi.txtAlamat.setText("Bandung")
            cardteknisi.txtRating.setText("4.5/5")
            self.verticalLayout_12.addWidget(cardteknisi)
    
    def back(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
    
