from celery import Celery

celery_app = Celery('extraction_worker', broker='redis://localhost:6379/0')

class ExtractionWorker:
    @celery_app.task
    def extract(self, document):
        # Placeholder for extraction task
        pass
