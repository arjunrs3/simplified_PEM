from dependencies.units.unit import Unit

class Voltage(Unit):
    def __init__(self, V=None):
        self._V = None
        if V is not None:
            self.V = V
        super().__init__(primary_unit="V")

    def set_all(self):
        pass

    @property
    def V(self):
        return self._V

    @V.setter
    def V(self, value):
        self._V = value
        self.set_all()
