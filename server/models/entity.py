from pydantic import BaseModel
from typing import List

class Entity(BaseModel):
    id: str
    type: str
    name: str
    attributes: dict

class Relation(BaseModel):
    from_id: str
    to_id: str
    type: str
    context: str
    date: str

class EntityWithRelations(BaseModel):
    entity: Entity
    relations: List[Relation]
