from dependencies.units.unit import Unit

class GasConstant(Unit):
    def __init__(self, JKmol=None):
        self._JKmol = None
        if JKmol is not None:
            self.JKmol = JKmol
        super().__init__(primary_unit="JKmol")

    def set_all(self):
        pass

    @property
    def JKmol(self):
        return self._JKmol

    @JKmol.setter
    def JKmol(self, value):
        self._JKmol = value
        self.set_all()
