from fastapi import APIRouter, HTTPException
from ..models.query import QueryRequest, QueryResponse
from ..engine.query_engine import QueryEngine

router = APIRouter()

query_engine = QueryEngine()

@router.post('/query', response_model=QueryResponse)
def query_endpoint(request: QueryRequest):
    try:
        response = query_engine.query(request.query, request.filters)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
