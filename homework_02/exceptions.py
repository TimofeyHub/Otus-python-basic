"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    def __init__(self, fuel_value: int):
        self.fuel_value = fuel_value

    def __str__(self):
        return f"Недостаточно топлива для запуска двигателя: {self.fuel_value} л ."


class NotEnoughFuel(Exception):
    def __init__(self, need_fuel: int):
        self.need_fuel = need_fuel

    def __str__(self):
        return f"Для преодоления указанной дистанции необходимо ещё {self.need_fuel} л топлива."


class CargoOverload(Exception):
    def __init__(self, overload_weight: int):
        self.overload_weght = overload_weight

    def __str__(self):
        return f"Перегруз {self.overload_weght} кг ."
