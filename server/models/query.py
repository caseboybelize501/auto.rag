from pydantic import BaseModel
from typing import List, Optional

class QueryRequest(BaseModel):
    query: str
    filters: Optional[dict] = None

class QueryResponse(BaseModel):
    answer: str
    sources: List[dict]
    graph_path: List[dict]
    entity_ids: List[str]
    confidence: float
