import os
import requests
from .base import Connector

class NotionConnector(Connector):
    def __init__(self):
        self.token = os.getenv('NOTION_TOKEN')

    def fetch(self):
        # Placeholder for fetching documents
        pass

    def register(self):
        response = requests.get('https://api.notion.com/v1/users/me', headers={'Authorization': f'Bearer {self.token}'})
        if response.status_code == 200:
            return {'source': 'notion', 'type': 'api', 'doc_count_estimate': 0, 'delta_sync': True}
        return None
