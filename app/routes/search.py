# app/routes/search.py

from fastapi import APIRouter, Query
from elasticsearch import Elasticsearch

router = APIRouter()

es = Elasticsearch("http://elasticsearch:9200")

@router.get("/search/1")
def search(q: str = Query(..., description="Search term")):
    response = es.search(
        index="my-index",
        query={"match": {"content": q}}
    )
    return response["hits"]


@router.get("/search/2")
def search_test_data():
    try:
        response = es.search(
            index="my-index",
            query={"match_all": {}}
        )
        hits = response["hits"]["hits"]
        return [{"id": hit["_id"], "data": hit["_source"]} for hit in hits]
    except Exception as e:
        return {"status": "error", "detail": str(e)}

@router.get("/search/3")
def search(q: str = Query(None, description="Search term")):
    if not q:
        return {"detail": "Missing search query"}
    
    response = es.search(
        index="my-index",
        query={"match": {"content": q}}
    )
    return response["hits"]
