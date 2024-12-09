from dependencies.units.unit import Unit

temperature_specific_energy_conversions_from_gmol = {
    "kgkmol": 1.0,
}


class MolarMass(Unit):
    """Base-level class for a molar mass dimension with various available units."""
    def __init__(self, gmol=None, kgkmol=None):
        self._gmol, self._kgkmol = None, None
        if gmol is not None:
            self.gmol = gmol
        elif kgkmol is not None:
            self.kgkmol = kgkmol
        else:
            pass
        super().__init__(primary_unit="gmol")

    def set_all(self):
        for k, v in temperature_specific_energy_conversions_from_gmol.items():
            setattr(self, f"_{k}", self._gmol * v)

    @property
    def gmol(self):
        return self._gmol

    @gmol.setter
    def gmol(self, value):
        self._gmol = value
        self.set_all()

    @property
    def kgkmol(self):
        return self._kgkmol

    @kgkmol.setter
    def kgkmol(self, value):
        self._kgkmol = value / temperature_specific_energy_conversions_from_gmol["kgkmol"]
        self.set_all()
