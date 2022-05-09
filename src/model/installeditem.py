from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, null, Date
from sqlalchemy.orm import declarative_base
from userdetail import UserDetail
from orders import Order
from product import Product

Base = declarative_base()


class InstalledItem(Base):
    __tablename__ = 'installeditem'
    quantity = Column(Integer)
    technician_id = Column(String(100), ForeignKey(UserDetail.user_id))
    order_id = Column(String(100), ForeignKey(
        Order.order_id), primary_key=True)
    product_id = Column(String(100), ForeignKey(
        Product.product_id), primary_key=True)
    installation_date = Column(Date, primary_key=True)

    def set_quantity(self, quantity: int):
        self.quantity = quantity
        return self

    def set_technician_id(self, technician_id: int):
        self.technician_id = technician_id
        return self

    def set_order_id(self, order_id: str):
        self.order_id = order_id
        return self

    def set_product_id(self, product_id: str):
        self.product_id = product_id
        return self

    def set_installation_date(self, timestamp: datetime):
        self.installation_date = timestamp
        return self
