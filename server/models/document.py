from pydantic import BaseModel

class Document(BaseModel):
    doc_id: str
    source: str
    title: str
    body: str
    author: str
    created_at: str
    modified_at: str
    url: str
    version_hash: str
