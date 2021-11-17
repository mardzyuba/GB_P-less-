# 4.Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("\nМашина начала движение")

    def stop(self):
        print(f"Машина остановилась")

    def turn(self, direction):
        d = direction
        print(f"Машина повернула {d}")

    def show_speed(self):
        print(f'Текущая скорость = {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Текущая скорость: {self.speed}.\n"
                  f"Внимание!Превышение скорости на {self.speed - 60} км/ч")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"Текущая скорость: {self.speed}.\n"
                  f"Внимание!Превышение скорости на {self.speed - 40} км/ч")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


car_1 = TownCar(130, "Black", "Toyota", False)
car_2 = SportCar(90, "White", "Honda", False)
car_3 = WorkCar(57, "Grey", "Hyundai", False)
car_4 = PoliceCar(40, "White", "Kia", True)

car_1.go()
car_1.show_speed()
car_1.turn("налево")
car_1.stop()

car_2.go()
car_2.show_speed()
car_2.turn("направо")
car_2.stop()

car_3.go()
car_3.show_speed()
car_3.stop()

car_4.go()
car_4.show_speed()
car_4.stop()
car_4.go()
