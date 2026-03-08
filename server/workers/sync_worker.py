from celery import Celery

celery_app = Celery('sync_worker', broker='redis://localhost:6379/0')

class SyncWorker:
    @celery_app.task
    def sync(self, source):
        # Placeholder for sync task
        pass
