import uuid

from sqlalchemy import Column, ForeignKey, Integer, String, null, Enum
from sqlalchemy.orm import declarative_base
from model.userdetail import UserDetail

Base = declarative_base()


class Ticket(Base):
    __tablename__ = 'ticket'
    user_id = Column(String(100), ForeignKey(UserDetail.user_id))
    title = Column(String(100))
    description = Column(String)
    priority = Column(Enum('1', '2', '3'))
    type = Column(Enum('1', '2', '3', '4'))
    attachment_url = Column(String)
    ticket_id = Column(String(100), primary_key=True, default=lambda: str(uuid.uuid4()))

    def set_feedback_id(self, feedback_id: str):
        self.feedback_id = feedback_id
        return self

    def set_description(self, description: str):
        self.description = description
        return self

    def set_type(self, type: str):
        self.type = type
        return self

    def set_priority(self, priority: str):
        self.priority = priority
        return self

    def set_title(self, title: str):
        self.title = title
        return self

    def set_attachment_url(self, url: str):
        self.attachment_url = url
        return self

    def set_user_id(self, user_id: str):
        self.user_id = user_id
        return self
