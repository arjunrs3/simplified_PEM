from dependencies.units.unit import Unit

specific_energy_conversions_from_Jkg = {
    "btulbm": 1 / (2.326 * 1000.0),
    "kJkg": 1 / 1000.0
}


class SpecificEnergy(Unit):
    def __init__(self, Jkg=None, kJkg=None, btulbm=None):
        self._Jkg, self._kJkg, self._btulbm = None, None, None
        if Jkg is not None:
            self.Jkg = Jkg
        elif kJkg is not None:
            self.kJkg = kJkg
        elif btulbm is not None:
            self.btulbm = btulbm
        super().__init__(primary_unit="Jkg")

    def set_all(self):
        for k, v in specific_energy_conversions_from_Jkg.items():
            setattr(self, f"_{k}", self._Jkg * v)

    @property
    def Jkg(self):
        return self._Jkg

    @Jkg.setter
    def Jkg(self, value):
        self._Jkg = value
        self.set_all()

    @property
    def kJkg(self):
        return self._kJkg

    @kJkg.setter
    def kJkg(self, value):
        self._Jkg = value / specific_energy_conversions_from_Jkg["kJkg"]
        self.set_all()

    @property
    def btulbm(self):
        return self._btulbm

    @btulbm.setter
    def btulbm(self, value):
        self._Jkg = value / specific_energy_conversions_from_Jkg["btulbm"]
        self.set_all()
