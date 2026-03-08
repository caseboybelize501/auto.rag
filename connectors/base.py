from abc import ABC, abstractmethod

class Connector(ABC):
    @abstractmethod
    def fetch(self):
        pass

    @abstractmethod
    def register(self):
        pass
