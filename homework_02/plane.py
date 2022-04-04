"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload
#from base import Vehicle
#from exceptions import CargoOverload

class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)

        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, add_cargo):
        new_cargo = self.cargo + add_cargo
        if new_cargo <= self.max_cargo:
            self.cargo = new_cargo
        else:
            #raise TypeError('CargoOverload')
            raise CargoOverload

    def remove_all_cargo(self):
        res = self.cargo
        self.cargo = 0
        return res

#plane1 = Plane(1000,)
# print('123')