from dependencies.units.unit import Unit


class Acceleration(Unit):
    def __init__(self, ms2=None):
        self._ms2 = None
        if ms2 is not None:
            self.ms2 = ms2
        super().__init__(primary_unit="ms2")
    def set_all(self):
        pass

    @property
    def ms2(self):
        return self._ms2

    @ms2.setter
    def ms2(self, value):
        self._ms2 = value
        self.set_all()
