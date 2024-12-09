import numpy as np

from dependencies.units.unit import Unit


angle_conversions_from_rads = {
    'degs': lambda r: np.rad2deg(r),
}

angle_conversions_to_rads = {
    'degs': lambda d: np.deg2rad(d),
}


class AngleRate(Unit):
    def __init__(self, rads=None, degs=None):
        self._rads, self._degs = None, None
        if rads is not None:
            self.rads = rads
        elif degs is not None:
            self.degs = degs
        super().__init__(primary_unit="rads")

    def set_all(self):
        """After setting the temperature in rad, set the temperature for all other units"""
        for k, v in angle_conversions_from_rads.items():
            setattr(self, f'_{k}', v(self._rads))

    @property
    def rads(self):
        return self._rads

    @rads.setter
    def rads(self, value):
        self._rads = value
        self.set_all()

    @property
    def degs(self):
        return self._degs

    @degs.setter
    def degs(self, value):
        self._rads = angle_conversions_to_rads['degs'](value)
        self.set_all()
