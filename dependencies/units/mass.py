from dependencies.units.unit import Unit

class Mass(Unit):
    """Base-level class for a mass dimension with various available units. Note that 'lb' represents pound-mass."""
    def __init__(self, kg=None, lb=None):
        self._kg = None
        self._lb = None
        self.kg_to_lb = 2.20462262185
        if kg is not None:
            self.kg = kg
        elif lb is not None:
            self.lb = lb
        else:
            pass
        super().__init__(primary_unit="kg")

    @property
    def kg(self):
        return self._kg

    @kg.setter
    def kg(self, kg):
        self._kg = kg
        self._lb = self.kg_to_lb * kg

    @property
    def lb(self):
        return self._lb

    @lb.setter
    def lb(self, lb):
        self._lb = lb
        self._kg = lb / self.kg_to_lb
