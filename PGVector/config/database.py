from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database

import os

load_dotenv()


def get_engine(user, password, host, port, db):
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url)
    return engine


engine = get_engine(os.getenv('DATABASE_USERNAME'), os.getenv(
    'DATABASE_PASSWORD'), os.getenv('DATABASE_HOST'), os.getenv('DATABASE_PORT'), os.getenv('DATABASE_NAME'))
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
session.execute(text('CREATE EXTENSION IF NOT EXISTS vector'))
Base = declarative_base()
