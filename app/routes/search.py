# app/routes/search.py

from fastapi import APIRouter, Query
from elasticsearch import Elasticsearch

router = APIRouter()

es = Elasticsearch("http://elasticsearch:9200")

@router.get("/search")
def search(q: str = Query(..., description="Search term")):
    response = es.search(
        index="your-index-name",
        query={"match": {"content": q}}
    )
    return response["hits"]
