from fastapi import FastAPI
from src.router.users import User1

app = FastAPI()
app.include_router(User1)