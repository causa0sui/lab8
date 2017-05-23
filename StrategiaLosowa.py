from Strategia import Strategia
from random import randint
from Kamień import Kamień
from Nożyce import Nożyce
from Papier import Papier

class StrategiaLosowa(Strategia):
    def ruch(self):
        xd = randint(1, 3)
        if xd == 1:
            return Papier()
        elif xd == 2:
            return Kamień()
        else:
            return Nożyce()
