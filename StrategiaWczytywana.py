from Strategia import Strategia
from random import randint
from Kamień import Kamień
from Nożyce import Nożyce
from Papier import Papier

class StrategiaWczytywana(Strategia):
    def ruch(self):
        while True:
            xd = input("Co chcesz pokazać???? xDDDDDDD)))0))))00000)0!1!!!111!!!!!!!!")
            if xd.lower() == "papier":
                return Papier()
            elif xd.lower() == "kamień" or xd.lower() == "kamien":
                return Kamień()
            elif xd.lower() == "nożyce" or xd.lower() == "nozyce":
                return Nożyce()
