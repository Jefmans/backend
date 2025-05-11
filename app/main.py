from fastapi import FastAPI
# from .routes import router
from app.routes import search, health

# app = FastAPI()
# # app.include_router(router)

app = FastAPI(
    docs_url="/docs",  # Make sure the documentation URL is correct
    redoc_url="/redoc",  # Make sure ReDoc URL is correct if you're using it
)


app.include_router(search.router, prefix="/api")
app.include_router(health.router, prefix="/api")