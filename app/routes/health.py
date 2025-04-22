from fastapi import APIRouter
from elasticsearch import Elasticsearch

router = APIRouter()

es = Elasticsearch("http://elasticsearch:9200")

@router.get("/es-health")
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
