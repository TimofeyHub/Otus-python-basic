from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(
            self,
            weight: int,
            fuel: int,
            fuel_consumption: int,
    ):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self._stared = False

    @property
    def started(self):
        return self._stared

    @started.setter
    def started(self, start_flag: bool):
        self._stared = start_flag

    def start(self) -> None:
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError(self.fuel)

    def move(self, distance: int) -> None:
        fuel_left = self.fuel - distance * self.fuel_consumption
        if fuel_left >= 0:
            self.fuel = fuel_left
        else:
            raise NotEnoughFuel(fuel_left)
