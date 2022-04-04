from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    def __init__(self, weight = 1000, fuel = 100, fuel_consumption = 10):
        self.weight = weight                       #масса
        self.fuel = fuel                           #топливо
        self.fuel_consumption = fuel_consumption   #расход топлива
        self.started = False                        # запущено?


    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
                print('Двигатель заведен')
            else:
                # raise TypeError('LowFuelError')
                raise LowFuelError
        else:
            print('Дивгатель уже заведен')


    def move(self, distance):
        fuel_on_distance = self.fuel_consumption * distance
        if fuel_on_distance <= self.fuel:
            fuel_all = self.fuel
            self.fuel -= fuel_on_distance
            print(f'До движения топлива: {fuel_all}, расход топлива на дистанцию {distance} составляет {fuel_on_distance}. На момент приезда топлива останется {self.fuel}')
        else:
            #raise TypeError('NotEnoughFuel')
            raise NotEnoughFuel


# if __name__ == '__main__':
#     try:
#         # cc =Vehicle(100,1000,10,False)
#         cc = Vehicle(1, 2, 3)
#         # cc.fuel(100)
#         print(cc.fuel)
#         print(vars(cc))
#
#         cc.fuel = 0
#         cc.start()
#     except LowFuelError:
#         print('Err____________________________ LowFuelError')
#


    # print('-------------------')
    # vv = Vehicle()
    # #print(vv.fuel)
    # print(vars(vv))
#    pass
    #car = Vehicle()
    #car.setFuel(90)
    #car.setFuelConsumption(10)
    #.start()
    #car.move(1)

#    weight = fake.pyint(150, 1000)
#    fuel = fake.pyint(30, 80)
#    fuel_consumption = fake.pyint(CONSUMPTION_MIN, 18)
#    vehicle = Vehicle(weight, fuel, fuel_consumption)


