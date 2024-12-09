from dependencies.units.unit import Unit

class DynamicViscosity(Unit):
    def __init__(self, kgms=None):
        self._kgms = None
        if kgms is not None:
            self.kgms = kgms
        super().__init__(primary_unit="kgms")

    def set_all(self):
        pass

    @property
    def kgms(self):
        return self._kgms

    @kgms.setter
    def kgms(self, value):
        self._kgms = value
        self.set_all()
