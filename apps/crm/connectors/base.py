from abc import ABC, abstractmethod


class BaseConnector(ABC):

    @abstractmethod
    def fetch(self):
        pass

    @abstractmethod
    def transform(self, item):
        pass