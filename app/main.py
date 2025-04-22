from fastapi import FastAPI
# from .routes import router
from app.routes import search, health

app = FastAPI()
# app.include_router(router)


app.include_router(search.router, prefix="/api")
app.include_router(health.router, prefix="/api")