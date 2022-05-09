from datetime import datetime
from sqlalchemy import Column, ForeignKey, String, DateTime, null
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Chat(Base):
    __tablename__ = 'chat'
    sender_id = Column(String(100), ForeignKey("credential.user_id"))
    receiver_id = Column(String(100), ForeignKey("credential.user_id"))
    message = Column(String)
    timestamp = Column(DateTime)

    def set_sender(self, sender_id: str):
        self.sender_id = sender_id
        return self

    def set_receiver(self, receiver_id: str):
        self.receiver_id = receiver_id
        return self

    def set_message(self, message: str):
        self.message = message
        return self

    def set_timestamp(self, timestamp: datetime):
        self.timestamp = timestamp
        return self
