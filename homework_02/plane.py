from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

"""
создайте класс `Plane`, наследник `Vehicle`
"""


class Plane(Vehicle):

    def __init__(
            self,
            weight,
            fuel,
            fuel_consumption,
            max_cargo
    ):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self._cargo = 0

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, cargo_value: int):
        self._cargo = cargo_value

    def load_cargo(self, cargo_weight: int) -> None:
        sum_cargo_weight = cargo_weight + self.cargo
        if sum_cargo_weight <= self.max_cargo:
            self.cargo = sum_cargo_weight
        else:
            raise CargoOverload(abs(sum_cargo_weight - self.max_cargo))

    def remove_all_cargo(self) -> int:
        removed_cargo = self.cargo
        self.cargo = 0
        return removed_cargo
