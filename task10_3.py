class Car:
    def __init__(self, color, car_type, year):
        self.color = color
        self.car_type = car_type
        self.year = year

    def start(self):
        print("Автомобиль заведен")

    def stop(self):
        print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year

    def set_type(self, car_type):
        self.car_type = car_type

    def set_color(self, color):
        self.color = color


my_car = Car("белый", "седан", 2022)
my_car.start()
my_car.stop()
my_car.set_year(2023)
print(my_car.year)
my_car.set_type("хэтчбек")
print(my_car.car_type)
my_car.set_color("красный")
print(my_car.color)


