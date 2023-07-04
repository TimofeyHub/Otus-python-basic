from homework_02.base import Vehicle
from homework_02.engine import Engine

"""
создайте класс `Car`, наследник `Vehicle`
"""


class Car(Vehicle):
    def __init__(
            self,
            weight,
            fuel,
            fuel_consumption,
    ):
        super().__init__(weight, fuel, fuel_consumption)
        self._engine = None

    @property
    def engine(self):
        return self._engine

    def set_engine(self, engine: Engine):
        self._engine = engine
