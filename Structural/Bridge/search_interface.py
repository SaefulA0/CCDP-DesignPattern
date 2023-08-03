# search_interface.py
from abc import ABC, abstractmethod


class SearchImplementation(ABC):
    @abstractmethod
    def search(self, keyword):
        pass
