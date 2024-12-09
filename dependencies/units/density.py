from dependencies.units.unit import Unit

density_conversions_from_kgm3 = {
    'slugft3': 1 / 515.379,
}


class Density(Unit):
    def __init__(self, kgm3=None, slugft3=None):
        self._kgm3, self._slugft3 = None, None
        if kgm3 is not None:
            self.kgm3 = kgm3
        elif slugft3 is not None:
            self.slugft3 = slugft3
        super().__init__(primary_unit="kgm3")

    def set_all(self):
        """After setting the area in kgm3, set the density for all other units"""
        for k, v in density_conversions_from_kgm3.items():
            setattr(self, f'_{k}', self._kgm3 * v)

    @property
    def kgm3(self):
        return self._kgm3

    @kgm3.setter
    def kgm3(self, value):
        self._kgm3 = value
        self.set_all()

    @property
    def slugft3(self):
        return self._slugft3

    @slugft3.setter
    def slugft3(self, value):
        self._kgm3 = value / density_conversions_from_kgm3['slugft3']
        self.set_all()
