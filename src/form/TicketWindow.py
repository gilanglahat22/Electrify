import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from form.controller import widget, context
from model.ticket import Ticket
from controller import insert_record


class TicketWindow(QMainWindow):
    def __init__(self):
        super(TicketWindow, self).__init__()
        loadUi(os.path.join(os.path.dirname(__file__), "..", "view/Ticket.ui"), self)

        self.priorityBox.addItem("Normal", 0)
        self.priorityBox.addItem("Penting", 1)
        self.priorityBox.addItem("Darurat", 2)

        self.setWindowTitle("Pusat Bantuan")

        self.backButton.clicked.connect(self.back_to_parent)
        self.sendButton.clicked.connect(self.submit)

    def submit(self):
        try:
            tiket = Ticket()\
                .set_user_id(context["user_id"])\
                .set_description(self.deksripsiTextbox.toPlainText())\
                .set_title(self.judulTextbox.toPlainText())\
                .set_attachment_url(self.URLTextBox.toPlainText())

            if self.priorityBox.currentText() == "Normal":
                tiket.set_priority("1")
            elif self.priorityBox.currentText() == "Penting":
                tiket.set_priority("2")
            elif self.priorityBox.currentText() == "Darurat":
                tiket.set_priority("3")

            tiket.set_type("1")

            insert_record(tiket)

            box = QMessageBox()
            box.setIcon(QMessageBox.Information)
            box.setText("Berhasil Menambahkan Bantuan")
            box.setWindowTitle("Sukses")
            box.exec()
        except Exception as e:
            box = QMessageBox()
            box.setIcon(QMessageBox.Critical)
            box.setText("Gagal menambahkan data")
            box.setWindowTitle("Kesalahan")
            box.setStandardButtons(QMessageBox.Ok)
            box.setDetailedText(str(e))
            box.exec()

    def back_to_parent(self):
        widget.setCurrentIndex(3)
