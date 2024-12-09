from dependencies.units.unit import Unit
velocity_conversions_from_ms = {
    'fts': 1 / 0.3048,
    'mph': 2.2369362912,
    'kph': 3.6,
    'knots': 1.94384
}


class Velocity(Unit):
    def __init__(self, ms=None, fts=None, mph=None, kph=None, knots=None):
        self._ms, self._fts, self._mph, self._kph, self._knots = None, None, None, None, None
        if ms is not None:
            self.ms = ms
        elif fts is not None:
            self.fts = fts
        elif mph is not None:
            self.mph = mph
        elif kph is not None:
            self.kph = kph
        elif knots is not None: 
            self.knots = knots
        super().__init__(primary_unit="ms")

    def set_all(self):
        """After setting the velocity in m/s, set the velocity for all other units"""
        for k, v in velocity_conversions_from_ms.items():
            setattr(self, f'_{k}', self._ms * v)

    @property
    def ms(self):
        return self._ms

    @ms.setter
    def ms(self, value):
        self._ms = value
        self.set_all()

    @property
    def fts(self):
        return self._fts

    @fts.setter
    def fts(self, value):
        self._ms = value / velocity_conversions_from_ms['fts']
        self.set_all()

    @property
    def mph(self):
        return self._mph

    @mph.setter
    def mph(self, value):
        self._ms = value / velocity_conversions_from_ms['mph']
        self.set_all()

    @property
    def kph(self):
        return self._kph

    @kph.setter
    def kph(self, value):
        self._ms = value / velocity_conversions_from_ms['kph']
        self.set_all()

    @property
    def knots(self):
        return self._knots

    @knots.setter
    def knots(self, value):
        self._ms = value / velocity_conversions_from_ms['knots']
        self.set_all()
