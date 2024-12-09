from dependencies.units.unit import Unit

class MassFlowRate(Unit):
    def __init__(self, kgs=None, lbs=None):
        self._kgs = None
        self._lbs = None
        self.kgs_to_lbs = 2.20462
        if kgs is not None:
            self.kgs = kgs
            self.lbs = self.kgs * self.kgs_to_lbs
        if lbs is not None: 
            self.lbs = lbs
            self.kgs = self.lbs / self.kgs_to_lbs
        super().__init__(primary_unit="kgs")

    def set_all(self):
        pass

    @property
    def kgs(self):
        return self._kgs

    @kgs.setter
    def kgs(self, value):
        self._kgs = value
        self._lbs = value * self.kgs_to_lbs
        self.set_all()

    @property
    def lbs(self): 
        return self._lbs
    
    @lbs.setter
    def lbs(self, value): 
        self._lbs = value
        self._kgs = value / self.kgs_to_lbs
        self.set_all
