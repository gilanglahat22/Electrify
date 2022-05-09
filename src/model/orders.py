from datetime import datetime
from sqlalchemy import Column, ForeignKey, String, null, DateTime
from sqlalchemy.orm import declarative_base
import uuid
from model.userdetail import UserDetail

Base = declarative_base()


class Order(Base):
    __tablename__ = 'orders'
    timestamp = Column(DateTime)
    customer_id = Column(String, ForeignKey(UserDetail.user_id))
    order_id = Column(String(100),
                      primary_key=True, default=lambda: str(uuid.uuid4()))

    def set_timestamp(self, timestamp: datetime):
        self.timestamp = timestamp
        return self

    def set_customer_id(self, customer_id: str):
        self.customer_id = customer_id
        return self

    def set_order_id(self, order_id: str):
        self.order_id = order_id
        return self
