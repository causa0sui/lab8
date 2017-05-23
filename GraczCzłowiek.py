from Gracz import Gracz
from StrategiaWczytywana import StrategiaWczytywana

class GraczCzłowiek(Gracz):
    def __init__(self):
        super().__init__(StrategiaWczytywana())

    def czy_chcesz_grać(self):
        xd = input("Czy chcesz grać xDDDDDD???")
        if xd == "N" or xd == "Nie" or xd == "n" or xd ==  "No" or xd == "Nyet" or xd == "no" or xd == "нет":
            print(xd)
            return False
        else:
            return True
