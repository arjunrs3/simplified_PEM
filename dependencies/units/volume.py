from dependencies.units.unit import Unit
volume_conversions_from_m3 = {
    'ft3': (1 / 0.3048) ** 3,
    'mm3': 1000 ** 3,
    'cm3': 100 ** 3,
    'in3': (12 / 0.3048) ** 3,
    'gal': 264.172052,
    'L': 1000
}


class Volume(Unit):
    def __init__(self, m3=None, mm3=None, cm3=None, ft3=None, in3=None, gal=None, L=None):
        self._m3, self._mm3, self._cm3, self._ft3, self._in3, self._gal, self._L = \
            None, None, None, None, None, None, None
        if m3 is not None:
            self.m3 = m3
        elif mm3 is not None:
            self.mm3 = mm3
        elif cm3 is not None:
            self.cm3 = cm3
        elif ft3 is not None:
            self.ft3 = ft3
        elif in3 is not None:
            self.in3 = in3
        elif gal is not None:
            self.gal = gal
        elif L is not None:
            self.L = L
        super().__init__(primary_unit="m3")

    def set_all(self):
        """After setting the area in m3, set the volume for all other units"""
        for k, v in volume_conversions_from_m3.items():
            setattr(self, f'_{k}', self._m3 * v)

    @property
    def m3(self):
        return self._m3

    @m3.setter
    def m3(self, value):
        self._m3 = value
        self.set_all()

    @property
    def mm3(self):
        return self._mm3

    @mm3.setter
    def mm3(self, value):
        self._m3 = value / volume_conversions_from_m3['mm3']
        self.set_all()

    @property
    def cm3(self):
        return self._cm3

    @cm3.setter
    def cm3(self, value):
        self._m3 = value / volume_conversions_from_m3['cm3']
        self.set_all()

    @property
    def ft3(self):
        return self._ft3

    @ft3.setter
    def ft3(self, value):
        self._m3 = value / volume_conversions_from_m3['ft3']
        self.set_all()

    @property
    def in3(self):
        return self._in3

    @in3.setter
    def in3(self, value):
        self._m3 = value / volume_conversions_from_m3['in3']
        self.set_all()

    @property
    def gal(self):
        return self._gal

    @gal.setter
    def gal(self, value):
        self._m3 = value / volume_conversions_from_m3['gal']
        self.set_all()

    @property
    def L(self):
        return self._L

    @L.setter
    def L(self, value):
        self._m3 = value / volume_conversions_from_m3['L']
        self.set_all()
