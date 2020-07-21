from __future__ import annotations

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

from app.base import Base


class Singleton(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance


class SqlDbConnection(object, metaclass=Singleton):
    def __init__(self, url: str):
        self.url = url
        self.session = None

    def __call__(self):
        engine = db.create_engine(self.url, connect_args={"check_same_thread": False}, echo=True)
        Base.metadata.create_all(engine)
        Session: db.orm.session.sessionmaker = sessionmaker(bind=engine)
        self.session = Session()
