from dependencies.units.unit import Unit


class CurrentDensity(Unit):
    def __init__(self, Am2=None, Acm2=None):
        self._Am2 = None
        self._Acm2 = None
        if Am2 is not None:
            self.Am2 = Am2
            self.Acm2 = self.Am2 / 100 / 100
        if Acm2 is not None: 
            self.Acm2 = Acm2
            self.Am2 = self.Acm2 * 100 * 100
        super().__init__(primary_unit="Acm2")

    def set_all(self):
        pass

    @property
    def Am2(self):
        return self._Am2

    @Am2.setter
    def Am2(self, value):
        self._Am2 = value
        self._Acm2 = value / 100 / 100
        self.set_all()

    @property
    def Acm2(self): 
        return self._Acm2
    
    @Acm2.setter
    def Acm2(self, value): 
        self._Acm2 = value
        self._Am2 = value * 100 * 100
        self.set_all
