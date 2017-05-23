from Przedmiot import Przedmiot

class Kamień(Przedmiot):
    def wygrywa_z(self, przedmiot):
        return not przedmiot.wygrywa_z_kamieniem()

    def wygrywa_z_nożycami(self):
        return True

    def __str__(self):
        return "Kamień"
