import logging
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain import PromptTemplate
import os

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

google_api_key=os.getenv('GOOGLE_API_KEY')
# genai.configure(api_key=google_api_key)

class RAGUseCase:
    def __init__(self):
        self.model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=google_api_key)

    def process_document(self, document_path):
        pdf_loader = PyPDFLoader(document_path)
        pages = pdf_loader.load_and_split()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
        context = "\n\n".join(str(p.page_content) for p in pages)
        texts = text_splitter.split_text(context)
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=google_api_key)
        vector_index = Chroma.from_texts(texts, embeddings).as_retriever(search_kwargs={"k": 5})
        return vector_index

    def generate_answer(self, question: str, retriever):
        template = """Use as seguintes partes do contexto para responder à pergunta no final. Se você não sabe a resposta, apenas diga que não sabe, não tente inventar uma resposta. Mantenha a resposta o mais concisa possível.
        {context}
        Pergunta: {question}
        Resposta útil:"""
        QA_CHAIN_PROMPT = PromptTemplate.from_template(template)
        qa_chain = RetrievalQA.from_chain_type(
            self.model,
            retriever=retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
        )
        result = qa_chain({"query": question})
        return result["result"]