from dependencies.units.unit import Unit

class KinematicViscosity(Unit):
    def __init__(self, m2s=None):
        self._m2s = None
        if m2s is not None:
            self.m2s = m2s
        super().__init__(primary_unit="m2s")

    def set_all(self):
        pass

    @property
    def m2s(self):
        return self._m2s

    @m2s.setter
    def m2s(self, value):
        self._m2s = value
        self.set_all()
