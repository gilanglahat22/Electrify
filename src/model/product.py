import uuid
from datetime import datetime
from sqlalchemy import Column, ForeignKey, String, null, DateTime, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'
    name = Column(String(100))
    stock = Column(Integer)
    product_id = Column(String(100),
                        primary_key=True, default=lambda: str(uuid.uuid4()))

    def set_name(self, name: str):
        self.name = name
        return self

    def set_stock(self, stock: int):
        self.stock = stock
        return self

    def set_product_id(self, product_id: str):
        self.product_id = product_id
        return self
