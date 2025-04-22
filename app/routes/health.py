
from fastapi import APIRouter, Query
from elasticsearch import Elasticsearch

router = APIRouter()
es = Elasticsearch("http://elasticsearch:9200")

@router.get("/es-health")
def elasticsearch_health():
    try:
        es_info = es.info()
        return {"status": "ok", "version": es_info["version"]["number"]}
    except Exception as e:
        return {"status": "error", "detail": str(e)}
