from sqlalchemy import Column, ForeignKey, Integer, PrimaryKeyConstraint, String, null, DateTime
from sqlalchemy.orm import declarative_base
from userdetail import UserDetail
from orders import Order

Base = declarative_base()


class Feedback(Base):
    __tablename__ = 'feedback'
    user_id = Column(String(100), ForeignKey(UserDetail.user_id))
    order_id = Column(String(100), ForeignKey(Order.order_id))
    rating = Column(Integer)
    description = Column(String)
    feedback_id = Column(String(100), primary_key=True)

    def feedback_id(self, feedback_id: str):
        self.feedback_id = feedback_id
        return self

    def set_description(self, description: str):
        self.description = description
        return self

    def set_rating(self, rating: int):
        self.rating = rating
        return self

    def set_user_id(self, user_id: str):
        self.user_id = user_id
        return self

    def set_order_id(self, order_id: str):
        self.order_id = order_id
        return self
