import os
from .base import Connector

class LocalFilesConnector(Connector):
    def __init__(self):
        self.path = os.getenv('LOCAL_DOCS_PATH', './docs')

    def fetch(self):
        # Placeholder for fetching documents
        pass

    def register(self):
        if os.path.exists(self.path):
            return {'source': 'local_files', 'type': 'filesystem', 'doc_count_estimate': 0, 'delta_sync': False}
        return None
