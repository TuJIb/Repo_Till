"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)

        self.engine = None


    def set_engine(self, engine):
        self.engine = engine


# car1 = Car(1,2,3)
# print(car1.started)
# print(vars(car1))
# print('~~~~')
#
#
# car1.set_engine(Engine(11,22))
# print(vars(car1))