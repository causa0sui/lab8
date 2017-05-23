from Przedmiot import Przedmiot

class Papier(Przedmiot):
    def wygrywa_z(self, przedmiot):
        return not przedmiot.wygrywa_z_papierem()

    def wygrywa_z_kamieniem(self):
        return True

    def __str__(self):
        return "Papier"
