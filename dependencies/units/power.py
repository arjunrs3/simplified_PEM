from dependencies.units.unit import Unit

class Power(Unit):
    def __init__(self, W=None, hp=None):
        self._W = None
        self._hp = None
        if W is not None:
            self.W = W
            self.hp = W / 745.7
        if hp is not None:
            self.hp = hp 
            self.W = hp * 745.7
        super().__init__(primary_unit="W")

    def set_all(self):
        pass

    @property
    def W(self):
        return self._W

    @W.setter
    def W(self, value):
        self._W = value
        self.set_all()

    @property 
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, value): 
        self._hp = value
        self.set_all()