from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

from util.db_session import session

Base = declarative_base()
Base.query = session.query_property()


class MiscSkillsModel(Base):
    __tablename__ = 'misc_skills'

    title = Column(String, primary_key=True)
    description = Column(String, nullable=True)



