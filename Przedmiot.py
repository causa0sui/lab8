from abc import ABC, abstractmethod

class Przedmiot(ABC):
    @abstractmethod
    def wygrywa_z(self, przedmiot):
        pass

    def wygrywa_z_kamieniem(self):
        return False

    def wygrywa_z_papierem(self):
        return False

    def wygrywa_z_nożycami(self):
        return False
