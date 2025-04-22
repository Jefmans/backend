
from fastapi import APIRouter, Query
from elasticsearch import Elasticsearch

router = APIRouter()
es = Elasticsearch("http://elasticsearch:9200")

@router.get("/es-health/1")
def elasticsearch_health():
    try:
        es_info = es.info()
        return {"status": "ok", "version": es_info["version"]["number"]}
    except Exception as e:
        return {"status": "error", "detail": str(e)}


@router.get("/es-health/2")
def elasticsearch_health():
    try:
        # use perform_request to bypass client validation
        response = es.perform_request(
            method="GET",
            path="/",
            headers={"Accept": "application/json"}
        )
        return {
            "status": "ok",
            "version": response["version"]["number"],
            "cluster_name": response["cluster_name"]
        }
    except Exception as e:
        return {"status": "error", "detail": str(e)}
    

@router.get("/es-health/3")
def elasticsearch_health():
    try:
        # Use raw HTTP call to completely bypass elasticsearch-py quirks
        res = requests.get("http://elasticsearch:9200/", headers={
            "Accept": "application/json"
        })
        res.raise_for_status()
        data = res.json()
        return {
            "status": "ok",
            "version": data["version"]["number"],
            "cluster_name": data["cluster_name"]
        }
    except Exception as e:
        return {"status": "error", "detail": str(e)}    