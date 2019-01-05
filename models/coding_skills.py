from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

from util.db_session import session

Base = declarative_base()
Base.query = session.query_property()


class CodingSkillsModel(Base):
    __tablename__ = 'coding_skills'

    title = Column(String, primary_key=True)
    # TODO turn into enum
    category = Column(String)
    percentage = Column(Integer)
    color = Column(String, nullable=True)

