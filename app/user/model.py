from __future__ import annotations
from app.auth.model import Credential
from app.base import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship


class MembershipType(Base):
    __tablename__ = "membership_types"
    membership_type_id = Column(Integer, primary_key=True, autoincrement=True)
    create_date = Column(Date)
    valid_until = Column(Date)
    discount_value = Column(Integer)
    discount_unit = Column(String)
    free_shipping = Column(String)


class RewardPointLog(Base):
    __tablename__ = "reward_point_logs"
    log_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    reward_type = Column(String)
    reward_points = Column(Integer)
    create_date = Column(Date)
    expiry_date = Column(Date)


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    avatar = Column(String)
    birthday = Column(Date)
    address = Column(String)
    website = Column(String)
    registration_date = Column(Date)
    promotional_reward_points = Column(Integer)
    non_promotional_reward_points = Column(Integer)
    membership_type_id = Column(Integer, ForeignKey("membership_types.membership_type_id"))
    credential: Credential = relationship("Credential", uselist=False, back_populates="user", )
