from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import mapped_column
from pgvector.sqlalchemy import Vector
from config.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


class TextEmbedding(Base):
    __tablename__ = "document"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    embedding = mapped_column(Vector(3))
