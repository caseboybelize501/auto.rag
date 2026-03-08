from fastapi import APIRouter, HTTPException
from ..models.source import SourceProfile
from ..connectors.connector_manager import ConnectorManager

router = APIRouter()

connector_manager = ConnectorManager()

@router.get('/sources')
def get_sources():
    profiles = connector_manager.register_sources()
    return {'sources': profiles}

@router.post('/sources/{source_type}/sync')
def trigger_sync(source_type: str):
    # Placeholder for triggering sync
    return {'job_id': '123', 'estimated_docs': 100}
