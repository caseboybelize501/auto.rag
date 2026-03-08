from pydantic import BaseModel
from typing import List

class SourceProfile(BaseModel):
    source: str
    type: str
    doc_count_estimate: int
    delta_sync: bool

class SourceStatus(BaseModel):
    sources: List[SourceProfile]
