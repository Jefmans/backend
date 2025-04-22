from fastapi import FastAPI
# from .routes import router
from app.routes import search

app = FastAPI()
# app.include_router(router)


app.include_router(search.router, prefix="/api")