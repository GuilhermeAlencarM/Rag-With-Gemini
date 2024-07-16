from fastapi.middleware.cors import CORSMiddleware
from routers.question import question
from fastapi import FastAPI
from config.environment import config
import uvicorn

app = FastAPI()

app.include_router(question, prefix='/api')


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
