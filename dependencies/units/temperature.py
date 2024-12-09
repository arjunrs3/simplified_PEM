from dependencies.units.unit import Unit
temperature_conversions_from_K = {
    'C': lambda K: K - 273.15,
    'F': lambda K: (K - 273.15) * (9 / 5) + 32,
    'R': lambda K: 9/5 * K,
}

temperature_conversions_to_K = {
    'C': lambda C: C + 273.15,
    'F': lambda F: (F - 32) * (5 / 9) + 273.15,
    'R': lambda R: 5/9 * R,
}


class Temperature(Unit):
    def __init__(self, K=None, C=None, F=None, R=None):
        self._K, self._C, self._F, self._R = None, None, None, None
        if K is not None:
            self.K = K
        elif C is not None:
            self.C = C
        elif F is not None:
            self.F = F
        elif R is not None:
            self.R = R
        super().__init__(primary_unit="K")

    def set_all(self):
        """After setting the temperature in K, set the temperature for all other units"""
        for k, v in temperature_conversions_from_K.items():
            setattr(self, f'_{k}', v(self._K))

    @property
    def K(self):
        return self._K

    @K.setter
    def K(self, value):
        self._K = value
        self.set_all()

    @property
    def C(self):
        return self._C

    @C.setter
    def C(self, value):
        self._K = temperature_conversions_to_K['C'](value)
        self.set_all()

    @property
    def F(self):
        return self._F

    @F.setter
    def F(self, value):
        self._K = temperature_conversions_to_K['F'](value)
        self.set_all()

    @property
    def R(self):
        return self._R

    @R.setter
    def R(self, value):
        self._K = temperature_conversions_to_K['R'](value)
        self.set_all()
