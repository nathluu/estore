from __future__ import annotations

from typing import TYPE_CHECKING

from app.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from app.user.model import User


class Credential(Base):
    __tablename__ = "credentials"
    username = Column(String, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), unique=True, nullable=False)
    password = Column(String)
    email = Column(String)
    phone = Column(String)
    access_token = Column(String)
    refresh_token = Column(String)
    user: User = relationship("User", uselist=False, back_populates="credential")
