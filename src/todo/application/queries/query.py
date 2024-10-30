from abc import ABC, abstractmethod

class Query(ABC):
    @abstractmethod
    def is_query(self):
        pass
