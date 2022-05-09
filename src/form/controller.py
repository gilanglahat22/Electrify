import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
context = {"nama_product": None, "stock_product": None}


def success_notification(message: str, title: str = "Informasi"):
    box = QMessageBox()
    box.setIcon(QMessageBox.Information)
    box.setText(message)
    box.setWindowTitle(title)
    box.exec()


def failed_notification(message: str, title: str):
    box = QMessageBox()
    box.setIcon(QMessageBox.Critical)
    box.setText(message)
    box.setWindowTitle(title)
    box.exec()


def error_notification(message: str, e:Exception, title: str):
    box = QMessageBox()
    box.setIcon(QMessageBox.Critical)
    box.setText(message)
    box.setWindowTitle(title)
    box.setDetailedText(str(e))
    box.exec()
