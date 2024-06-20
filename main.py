from fastapi import FastAPI
from src.router.todos import Todo1

app = FastAPI()
app.include_router(Todo1)