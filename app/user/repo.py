from __future__ import annotations
from sqlalchemy.orm import Session

from app.auth.model import Credential
from app.user.dto import UserDtoIn
from app.user.model import User


class UserRepo(object):
    def __init__(self, session: Session):
        self.sess: Session = session

    def save(self, user: UserDtoIn):
        cred = Credential(username=user.username, password=user.password, email=user.email, phone=user.phone)
        user_db = User(first_name=user.first_name, last_name=user.last_name, address=user.address,
                       website=user.website, credential=cred)
        self.sess.add(user_db)
        self.sess.commit()
        return user_db.user_id

