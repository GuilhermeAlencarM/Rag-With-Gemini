
from config.database import SessionLocal, engine
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import models
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

models.Base.metadata.create_all(bind=engine)

chatbot = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@chatbot.post("/users/")
def create_user(db: Session = Depends(get_db)):
    pass
