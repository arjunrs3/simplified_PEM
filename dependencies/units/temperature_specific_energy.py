from dependencies.units.unit import Unit
temperature_specific_energy_conversions_from_JkgK = {
    "btulbmR": 1 / 4186.8,
    "kJkgK": 1 / 1000.0
}


class TemperatureSpecificEnergy(Unit):
    def __init__(self, JkgK=None, kJkgK=None, btulbmR=None):
        self._JkgK, self._kJkgK, self._btulbmR = None, None, None
        if JkgK is not None:
            self.JkgK = JkgK
        elif btulbmR is not None:
            self.btulbmR = btulbmR
        elif kJkgK is not None:
            self.kJkgK = kJkgK
        super().__init__(primary_unit="JkgK")

    def set_all(self):
        for k, v in temperature_specific_energy_conversions_from_JkgK.items():
            setattr(self, f"_{k}", self._JkgK * v)

    @property
    def JkgK(self):
        return self._JkgK

    @JkgK.setter
    def JkgK(self, value):
        self._JkgK = value
        self.set_all()

    @property
    def kJkgK(self):
        return self._kJkgK

    @kJkgK.setter
    def kJkgK(self, value):
        self._JkgK = value / temperature_specific_energy_conversions_from_JkgK["kJkgK"]
        self.set_all()

    @property
    def btulbmR(self):
        return self._btulbmR

    @btulbmR.setter
    def btulbmR(self, value):
        self._JkgK = value / temperature_specific_energy_conversions_from_JkgK["btulbmR"]
        self.set_all()
