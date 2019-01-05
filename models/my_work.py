from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

from util.db_session import session

Base = declarative_base()
Base.query = session.query_property()


class MyWorkModel(Base):
    __tablename__ = 'my_work'

    title = Column(String, primary_key=True)
    url = Column(String)
    description = Column(String, nullable=True)



