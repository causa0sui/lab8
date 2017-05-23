class MiejsceRozgrywki():
    MAX_RUND = 42
    def __init__(self, gracz1, gracz2):
        self.__gracz1 = gracz1
        self.__gracz2 = gracz2

    def przeprowadź_grę(self):
        aktualna_ilość_ukończonych_rund = 0

        while self.__gracz1.czy_chcesz_grać() and self.__gracz2.czy_chcesz_grać() and aktualna_ilość_ukończonych_rund < self.MAX_RUND:
            przedmiot_pierwszy = self.__gracz1.twój_ruch()
            przedmiot_drugi = self.__gracz2.twój_ruch()
            print("Gracz 1 użył przedmiotu: {0}, Gracz 2 użył przedmiotu {1}".format(przedmiot_pierwszy, przedmiot_drugi))

            if przedmiot_pierwszy.wygrywa_z(przedmiot_drugi) and przedmiot_drugi.wygrywa_z(przedmiot_pierwszy):
                print("Remis")
            elif przedmiot_pierwszy.wygrywa_z(przedmiot_drugi):
                print("Gracz 1 wygrał rundę {0}".format(aktualna_ilość_ukończonych_rund))
            elif przedmiot_drugi.wygrywa_z(przedmiot_pierwszy):
                print("Gracz 2 wygrał rundę {0}".format(aktualna_ilość_ukończonych_rund))

            aktualna_ilość_ukończonych_rund += 1
