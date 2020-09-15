import os
from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from src.db.base_class import Base

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = config('PORT_APP', default=8000)
HOST = config('HOST_APP')
BASE_PATH = config('BASE_PATH')
ENVIRONMENT = config('ENVIRONMENT')
SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')


class DatabasePSQL:

    @classmethod
    def session_database(cls):
        engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)
        db: Session = session()
        return db


