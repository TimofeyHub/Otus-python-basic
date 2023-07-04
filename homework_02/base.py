from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(
            self,
            weight,
            fuel,
            fuel_consumption,
    ):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self._stared = False

    @property
    def started(self):
        return self._stared

    @started.setter
    def started(self, value: bool):
        self._stared = value

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError(self.fuel)

    def move(self, distance: int):
        fuel_left = self.fuel - distance * self.fuel_consumption
        if fuel_left >= 0:
            self.fuel = fuel_left
        else:
            raise NotEnoughFuel(abs(fuel_left))
