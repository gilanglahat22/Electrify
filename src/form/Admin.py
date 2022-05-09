import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from form.controller import widget


class AdminWindow(QMainWindow):
    def __init__(self):
        super(AdminWindow, self).__init__()
        loadUi(os.path.join(os.path.dirname(__file__), "..", "view/Admin.ui"), self)
