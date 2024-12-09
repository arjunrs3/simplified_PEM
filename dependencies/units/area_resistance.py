from dependencies.units.unit import Unit


class AreaResistance(Unit):
    def __init__(self, Ohmcm2=None):
        self._Ohmcm2 = None
        if Ohmcm2 is not None:
            self.Ohmcm2 = Ohmcm2
        super().__init__(primary_unit="Ohmcm2")

    def set_all(self):
        pass

    @property
    def Ohmcm2(self):
        return self._Ohmcm2

    @Ohmcm2.setter
    def Ohmcm2(self, value):
        self._Ohmcm2 = value
        self.set_all()
