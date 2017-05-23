from Przedmiot import Przedmiot

class Nożyce(Przedmiot):
    def wygrywa_z(self, przedmiot):
        return not przedmiot.wygrywa_z_nożycami()

    def wygrywa_z_papierem(self):
        return True

    def __str__(self):
        return "Nożyce"
