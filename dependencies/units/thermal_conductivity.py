from dependencies.units.unit import Unit

class ThermalConductivity(Unit):
    def __init__(self, Wmk=None):
        self._Wmk = None
        if Wmk is not None:
            self.Wmk = Wmk
        super().__init__(primary_unit="Wmk")

    def set_all(self):
        pass

    @property
    def Wmk(self):
        return self._Wmk

    @Wmk.setter
    def Wmk(self, value):
        self._Wmk = value
        self.set_all()
