from dependencies.units.unit import Unit
time_conversions_from_seconds = {
    "minutes": 1 / 60,
    "hours": 1 / 3600
}


class Time(Unit):
    def __init__(self, seconds=None, minutes=None, hours=None):
        self._seconds, self._hours, self._minutes = None, None, None
        if seconds is not None:
            self.seconds = seconds
        elif minutes is not None:
            self.minutes = minutes
        elif hours is not None:
            self.hours = hours
        super().__init__(primary_unit="seconds")

    def set_all(self):
        """After setting the time in seconds, set the time for all other units"""
        for k, v in time_conversions_from_seconds.items():
            setattr(self, f'_{k}', self._seconds * v)

    @property
    def seconds(self):
        return self._seconds

    @seconds.setter
    def seconds(self, value):
        self._seconds = value
        self.set_all()

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, value):
        self._seconds = value / time_conversions_from_seconds['minutes']
        self.set_all()

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, value):
        self._seconds = value / time_conversions_from_seconds['hours']
        self.set_all()
