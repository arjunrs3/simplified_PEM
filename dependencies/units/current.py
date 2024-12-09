from dependencies.units.unit import Unit


class Current(Unit):
    def __init__(self, A=None):
        self._A = None
        if A is not None:
            self.A = A
        super().__init__(primary_unit="A")

    def set_all(self):
        pass

    @property
    def A(self):
        return self._A

    @A.setter
    def A(self, value):
        self._A = value
        self.set_all()
