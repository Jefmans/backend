from fastapi import APIRouter, Query
from elasticsearch import Elasticsearch
import requests
import os

router = APIRouter()

# es = Elasticsearch("http://elasticsearch:9200")
# es = Elasticsearch("http://65.109.3.143:9200")

es = Elasticsearch(os.getenv("ES_HOST", "http://elasticsearch:9200"))


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
        # hits = response["hits"]["hits"]
        # return [{"id": hit["_id"], "data": hit["_source"]} for hit in hits]
        return response
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


@router.get("/es-debug")
def es_debug():
    try:
        response = es.perform_request(
            method="GET",
            path="/",
            headers={"Accept": "application/json"}
        )
        return response
    except Exception as e:
        return {"status": "error", "detail": str(e)}


@router.get("/search/quick")
def quick_search():
    try:
        query = {"query": {"match_all": {}}}
        res = requests.post("http://65.109.3.143:9200/my-index/_search",
                            headers={"Content-Type": "application/json"},
                            json=query)
        return res.json()
    except Exception as e:
        return {"status": "error", "detail": str(e)}


# @router.get("/my-test")
# def test_search():
#     es.search(index="my-index", query={"match": {"foo": {"query": "foo"}}})

#     return "test"

@router.get("/info")
def get_info():
    response = es.search(
    index="my-index",
    query={"match": {'age': {'query':'30'}}}
    )

    return response