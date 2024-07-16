from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import mapped_column
from pgvector.sqlalchemy import Vector
from config.database import Base


class TextEmbedding(Base):
    __tablename__ = "document"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    embedding = mapped_column(Vector(3))
