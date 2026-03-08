from fastapi import APIRouter

router = APIRouter()

@router.get('/health')
def get_health():
    # Placeholder for health check
    return {'status': 'ok'}
