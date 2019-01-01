from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from util import settings as setting

logger = setting.logger

try:
    engine = create_engine(setting.DATABASE_URL)
    Base = declarative_base()
    Base.metadata.create_all(engine)
    session = scoped_session(sessionmaker(bind=engine))
except:
    logger.error("Cannot connect to db")
