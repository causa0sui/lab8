from abc import ABC, abstractmethod

class Strategia(ABC):
    @abstractmethod
    def ruch(self):
        pass
