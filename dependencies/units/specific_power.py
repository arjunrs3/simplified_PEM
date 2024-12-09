from dependencies.units.unit import Unit

class SpecificPower(Unit):
    def __init__(self, Wkg=None, kWkg=None):
        self._Wkg = None
        self._kWkg = None
        if Wkg is not None:
            self.Wkg = Wkg
            self.kWkg = self.Wkg / 1000
        if kWkg is not None: 
            self.kWkg = kWkg
            self.Wkg = self.kWkg * 1000
        super().__init__(primary_unit="Wkg")

    def set_all(self):
        pass

    @property
    def Wkg(self):
        return self._Wkg

    @Wkg.setter
    def Wkg(self, value):
        self._Wkg = value
        self._kWkg = value / 1000
        self.set_all()

    @property
    def kWkg(self): 
        return self._kWkg
    
    @kWkg.setter
    def kWkg(self, value): 
        self._kWkg = value
        self._Wkg = value * 1000
        self.set_all
