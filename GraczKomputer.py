from Gracz import Gracz
from StrategiaLosowa import StrategiaLosowa
class GraczKomputer(Gracz):
    def __init__(self):
        super().__init__(StrategiaLosowa())

    def czy_chcesz_grać(self):
        return True
