from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class QuestionRequest(BaseModel):
    question: str
    document_path: str = Field('/home/guilherme/Documentos/development/rag-v1/docs/04_2024.pdf')