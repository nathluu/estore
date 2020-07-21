from app.base import Base
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey


class ProductCategory(Base):
    __tablename__ = "product_categories"
    product_category_id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    parent_category_id = Column(Integer)
    max_reward_points_encash = Column(Integer)


class Product(Base):
    __tablename__ = "products"
    product_id = Column(Integer, primary_key=True)
    provider_id = Column(Integer, ForeignKey("users.user_id"))
    product_category_id = Column(Integer, ForeignKey("product_categories.product_category_id"))


class ProductDetails(Base):
    __tablename__ = "product_details"
    product_id = Column(Integer, ForeignKey("products.product_id"), unique=True, nullable=False)
    description = Column(String)
    image = Column(String)


class ProductPrice(Base):
    __tablename__ = "product_prices"
    price_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.product_id"))
    base_price = Column(Integer)
    create_date = Column(Date)
    expiry_date = Column(Date)
    active = Column(String)


class ProductDiscount(Base):
    __tablename__ = "product_discounts"
    discount_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    discount_value = Column(Integer)
    discount_unit = Column(String)
    create_date = Column(DateTime)
    valid_until = Column(DateTime)
    coupon_code = Column(String)
    minimum_order_value = Column(Integer)
    maximum_discount_amount = Column(Integer)
    redeem_allowed = Column(String)


class ProductCategoryDiscount(Base):
    __tablename__ = "product_discounts"
    discount_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("product_categories.product_category_id"), nullable=False)
    discount_value = Column(Integer)
    discount_unit = Column(String)
    create_date = Column(DateTime)
    valid_until = Column(DateTime)
    coupon_code = Column(String)
    minimum_order_value = Column(Integer)
    maximum_discount_amount = Column(Integer)
    redeem_allowed = Column(String)
