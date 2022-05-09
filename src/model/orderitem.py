from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, PrimaryKeyConstraint, String, null, DateTime
from sqlalchemy.orm import declarative_base
from model.orders import Order
from model.product import Product

Base = declarative_base()


class OrderItem(Base):
    __tablename__ = 'orderitem'
    quantity = Column(Integer)
    order_id = Column(String(100), ForeignKey(Order.order_id), primary_key=True)
    product_id = Column(String(100), ForeignKey(Product.product_id), primary_key=True)

    def set_product_id(self, product_id: str):
        self.product_id = product_id
        return self

    def set_quantity(self, quantity: int):
        self.quantity = quantity
        return self

    def set_order_id(self, order_id: str):
        self.order_id = order_id
        return self
