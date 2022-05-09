from datetime import datetime
from sqlalchemy import Column, ForeignKey, String, null
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class UserDetail(Base):
    __tablename__ = 'userdetail'
    name = Column(String(100))
    address = Column(String)
    telephone = Column(String(50))
    user_id = Column(String(100),
                     ForeignKey("credential.user_id"),
                     primary_key=True)

    def set_user_id(self, user_id: str):
        self.user_id = user_id
        return self

    def set_password(self, password: str):
        self.password = password
        return self

    def set_username(self, username: datetime):
        self.username = username
        return self
