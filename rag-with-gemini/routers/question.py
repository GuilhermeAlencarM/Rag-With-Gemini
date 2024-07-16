
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from models.request import QuestionRequest
from usecase.rag_usecase import RAGUseCase
from fastapi import HTTPException
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

question = APIRouter()

@question.post("/generate_answer/")
async def generate_answer(request: QuestionRequest, rag_use_case: RAGUseCase = Depends()):
    try:
        retriever = rag_use_case.process_document(request.document_path)
        answer = rag_use_case.generate_answer(request.question, retriever)
        return JSONResponse(content={"answer": answer}, status_code=200)
    except Exception as e:
        logger.error(f"Error generating answer: {e}")
        raise HTTPException(status_code=500, detail="Erro ao gerar a resposta.")