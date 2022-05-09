from typing import Any

from database.db import Session
from model.credential import Credential
from model.techiniciancertificate import TechnicianCertificate
from model.userdetail import UserDetail
from sqlalchemy.sql import select
import bcrypt


def register(username: str, password: str, role: str)-> bool:
    salt = bcrypt.gensalt()
    hashed_passwd = bcrypt.hashpw(bytes(password, "utf-8"), salt).decode("utf-8")
    isExist, Id = login(username, password, role)
    if (not isExist):
        cred = Credential() \
            .set_username(username) \
            .set_password(hashed_passwd) \
            .set_role(role)
        Session.add(cred)
        Session.commit()
        return True
    else:
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("This account is already exist !")
        msgBox.setWindowTitle("Message")
        msgBox.exec()
        return False


def login(username: str, password: str, role:str) -> (bool, str):
    try:
        query = select(Credential.user_id, Credential.password, Credential.role).where(Credential.username == username, Credential.role == role)
        user_data = Session.execute(query).first()

        is_match = bcrypt.checkpw(bytes(password, "utf-8"), bytes(user_data.password, "utf-8"))

        if not is_match:
            return is_match, None
        else:
            return is_match, user_data.user_id
    except AttributeError:
        return False, None


def get_user_detail(user_id: str) -> UserDetail:
    try:
        query = select(UserDetail).where(UserDetail.user_id == user_id)
        user_data = Session.execute(query).first()

        return user_data[0]
    except TypeError:
        return None


def get_technician_certificate(technician_id: str) -> TechnicianCertificate :
    try:
        query = select(TechnicianCertificate).where(TechnicianCertificate.user_id == technician_id)
        data = Session.execute(query).first()

        return data[0]
    except TypeError:
        return None
