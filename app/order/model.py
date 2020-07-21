from app.base import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey


class Order(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    date_ordered = Column(Date)
    date_required = Column(Date)
    total_price = Column(Integer)
    status = Column(String)


class OrderLine(Base):
    __tablename__ = "order_lines"
    order_id = Column(Integer, ForeignKey("orders.order_id"), primary_key=True)
    product_id = Column(Integer, ForeignKey("products.product_id"), primary_key=True)
    quantity = Column(Integer)
