from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, DeclarativeBase

from db_settings import settings


class Base(DeclarativeBase):
    __abstract__ = True


sqlalchemy_database_uri = settings.default_sqlalchemy_database_uri

engine = create_engine(url=sqlalchemy_database_uri)
session = scoped_session(sessionmaker(bind=engine))




