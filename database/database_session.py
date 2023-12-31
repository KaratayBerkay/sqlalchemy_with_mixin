from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, DeclarativeBase

import db_settings as settings


class Base(DeclarativeBase):
    __abstract__ = True


sqlalchemy_database_uri = settings.DATABASE_URL

engine = create_engine(url=sqlalchemy_database_uri)
session = scoped_session(sessionmaker(bind=engine))
print('settings.DATABASE_URL', settings.DATABASE_URL)
