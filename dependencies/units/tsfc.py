from dependencies.units.unit import Unit

class TSFC(Unit):
    def __init__(self, kgsN=None, lblbfhr=None):
        self._kgsN = None
        self._lblbfhr = None
        if kgsN is not None:
            self.kgsN = kgsN
            self._lblbfhr = kgsN * 3600 * 2.20462 / 0.224809
        if lblbfhr is not None:
            self.lblbfhr = lblbfhr
        super().__init__(primary_unit="kgsN")

    def set_all(self):
        pass

    @property
    def kgsN(self):
        return self._kgsN

    @kgsN.setter
    def kgsN(self, value):
        self._kgsN = value
        self._lblbfhr = value * 3600 * 2.20462 / 0.224809
        self.set_all()

    @property
    def lblbfhr(self):
        return self._lblbfhr

    @lblbfhr.setter
    def lblbfhr(self, value):
        self._lblbfhr = value
        self._kgsN = value / 3600 / 2.2042 * 0.224809
