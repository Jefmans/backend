# app/routes/search.py

from fastapi import APIRouter, Query
from elasticsearch import Elasticsearch

router = APIRouter()

es = Elasticsearch("http://elasticsearch:9200")

# @router.get("/search")
# def search(q: str = Query(..., description="Search term")):
#     response = es.search(
#         index="your-index-name",
#         query={"match": {"content": q}}
#     )
#     return response["hits"]


# @router.get("/search")
# def search_test_data():
#     response = es.search(
#         index="my-index",
#         query={"match_all": {}}
#     )
#     hits = response["hits"]["hits"]
#     return [{"id": hit["_id"], "data": hit["_source"]} for hit in hits]




@router.get("/search")
def search_test_data():
    response = es.search(
        index="my-index",
        body={
            "query": {
                "match_all": {}
            }
        },
        headers={"Content-Type": "application/json"}
    )
    hits = response["hits"]["hits"]
    return [{"id": hit["_id"], "data": hit["_source"]} for hit in hits]
