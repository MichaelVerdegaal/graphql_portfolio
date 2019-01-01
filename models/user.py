from sqlalchemy import Column, BigInteger, String
from sqlalchemy.ext.declarative import declarative_base

from util.db_session import session

Base = declarative_base()
# We will need this for querying
Base.query = session.query_property()


class UserModel(Base):
    __tablename__ = 'users'

    uid = Column(BigInteger, primary_key=True)
    name = Column(String)
    motto = Column(String)

    def __repr__(self):
        return f'UID: {self.uid}, NAME: {self.name}, MOTTO: {self.motto}'
