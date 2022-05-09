import uuid
from sqlalchemy import Column, ForeignKey, String, null
from sqlalchemy.orm import declarative_base
from model.credential import Credential

Base = declarative_base()


class TechnicianCertificate(Base):
    __tablename__ = 'techniciancertificate'
    certificate_name = Column(String(300))
    certificate_url = Column(String)
    user_id = Column(String(100), ForeignKey(Credential.user_id))
    certificate_id = Column(String(100),
                            primary_key=True,
                            default=lambda: str(uuid.uuid4()))

    def set_certificate_name(self, certificate_name: str):
        self.certificate_name = certificate_name
        return self

    def set_certificate_url(self, certificate_url: str):
        self.certificate_url = certificate_url
        return self

    def set_user_id(self, user_id: str):
        self.user_id = user_id
        return self
