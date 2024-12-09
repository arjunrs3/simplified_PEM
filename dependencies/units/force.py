from dependencies.units.unit import Unit

class Force(Unit):
    """Base-level class for a force dimension with various available units. Note that 'lbf' represents pound-force."""
    def __init__(self, N=None, lbf=None):
        self._N = None
        self._lbf = None
        self.N_to_lbf = 0.224809
        if N is not None:
            self.N= N
        elif lbf is not None:
            self.lbf = lbf
        else:
            pass
        super().__init__(primary_unit="N")

    @property
    def N(self):
        return self._N

    @N.setter
    def N(self, N):
        self._N = N
        self._lbf = self.N_to_lbf * N

    @property
    def lbf(self):
        return self._lbf

    @lbf.setter
    def lbf(self, lbf):
        self._lbf = lbf
        self._N = lbf / self.N_to_lbf
