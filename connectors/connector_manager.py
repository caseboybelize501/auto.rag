from . import confluence, notion, slack, google_drive, sharepoint, local_files

class ConnectorManager:
    def __init__(self):
        self.connectors = [
            confluence.ConfluenceConnector(),
            notion.NotionConnector(),
            slack.SlackConnector(),
            google_drive.GoogleDriveConnector(),
            sharepoint.SharePointConnector(),
            local_files.LocalFilesConnector()
        ]

    def register_sources(self):
        profiles = []
        for connector in self.connectors:
            profile = connector.register()
            if profile:
                profiles.append(profile)
        return profiles
