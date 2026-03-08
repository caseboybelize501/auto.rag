from fastapi import FastAPI
from .api import query, sources, graph, entities, health

app = FastAPI()

app.include_router(query.router, prefix='/v1', tags=['query'])
app.include_router(sources.router, prefix='/api', tags=['sources'])
app.include_router(graph.router, prefix='/api/graph', tags=['graph'])
app.include_router(entities.router, prefix='/api/entities', tags=['entities'])
app.include_router(health.router, prefix='/api', tags=['health'])
