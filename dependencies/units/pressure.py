from dependencies.units.unit import Unit
pressure_conversions_from_Pa = {
    'kPa': 0.001,
    'psi': 0.0001450377,
    'psf': 0.020885,
    'bar': 1e-5,
    'atm': 1 / 101325,
}


class Pressure(Unit):
    def __init__(self, Pa=None, kPa=None, psi=None, psf=None, bar=None, atm=None):
        self._Pa, self._kPa, self._psi, self._psf, self._bar, self._atm = None, None, None, None, None, None
        if Pa is not None:
            self.Pa = Pa
        elif kPa is not None:
            self.kPa = kPa
        elif psi is not None:
            self.psi = psi
        elif psf is not None:
            self.psf = psf
        elif bar is not None:
            self.bar = bar
        elif atm is not None:
            self.atm = atm
        super().__init__(primary_unit="Pa")

    def set_all(self):
        """After setting the temperature in K, set the temperature for all other units"""
        for k, v in pressure_conversions_from_Pa.items():
            setattr(self, f'_{k}', self._Pa * v)

    @property
    def Pa(self):
        return self._Pa

    @Pa.setter
    def Pa(self, value):
        self._Pa = value
        self.set_all()

    @property
    def kPa(self):
        return self._kPa

    @kPa.setter
    def kPa(self, value):
        self._Pa = value / pressure_conversions_from_Pa['kPa']
        self.set_all()

    @property
    def psi(self):
        return self._psi

    @psi.setter
    def psi(self, value):
        self._Pa = value / pressure_conversions_from_Pa['psi']
        self.set_all()

    @property
    def psf(self):
        return self._psf

    @psf.setter
    def psf(self, value):
        self._Pa = value / pressure_conversions_from_Pa['psf']
        self.set_all()

    @property
    def bar(self):
        return self._bar

    @bar.setter
    def bar(self, value):
        self._Pa = value / pressure_conversions_from_Pa['bar']
        self.set_all()

    @property
    def atm(self):
        return self._atm

    @atm.setter
    def atm(self, value):
        self._Pa = value / pressure_conversions_from_Pa['atm']
        self.set_all()
