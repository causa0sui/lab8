from abc import ABC, abstractmethod

class Gracz(ABC):
    def __init__(self, strategia):
        self.__strategia = strategia

    @abstractmethod
    def czy_chcesz_grać(self):
        pass

    def twój_ruch(self):
        return self.__strategia.ruch()
