# component.py
from abc import ABC, abstractmethod


class BookComponent(ABC):
    @abstractmethod
    def search(self, keyword):
        pass
