from dependencies.units.unit import Unit

class PowerDensity(Unit):
    def __init__(self, Wm2=None, Wcm2=None):
        self._Wm2 = None
        self._Wcm2 = None
        if Wm2 is not None:
            self.Wm2 = Wm2
            self.Wcm2 = self.Wm2 / 100 / 100
        if Wcm2 is not None: 
            self.Wcm2 = Wcm2
            self.Wm2 = self.Wcm2 * 100 * 100
        super().__init__(primary_unit="Wm2")

    def set_all(self):
        pass

    @property
    def Wm2(self):
        return self._Wm2

    @Wm2.setter
    def Wm2(self, value):
        self._Wm2 = value
        self._Wcm2 = value / 100 / 100
        self.set_all()

    @property
    def Wcm2(self): 
        return self._Wcm2
    
    @Wcm2.setter
    def Wcm2(self, value): 
        self._Wcm2 = value
        self._Wm2 = value * 100 * 100
        self.set_all
