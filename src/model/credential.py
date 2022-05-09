import uuid
from sqlalchemy import Column, String, Enum
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Credential(Base):
    __tablename__ = 'credential'
    username = Column(String(100))
    password = Column(String)
    user_id = Column(String(100), primary_key=True, default=lambda: str(uuid.uuid4()))
    role = Column(Enum('Pelanggan', 'Teknisi', 'Admin'))

    def set_user_id(self, user_id: str):
        self.user_id = user_id
        return self

    def set_password(self, password: str):
        self.password = password
        return self

    def set_username(self, username: str):
        self.username = username
        return self
    
    def set_role(self, role: str):
        self.role = role
        return self
