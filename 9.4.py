class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed}')

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def characteristics_of_cars(self):
        print(f'Автомобиль {self.name}, цвет {self.color}, полицейский {self.is_police}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed}')
        if self.speed > 60:
            print('Скорость превышена!')


a = TownCar(70, 'синий', 'Mazda', False)
a.characteristics_of_cars()
a.show_speed()


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def characteristics_of_cars(self):
        print(f'Автомобиль {self.name}, цвет {self.color}, полицейский {self.is_police}')


b = SportCar(150, 'красный', 'Ferrari', False)
b.characteristics_of_cars()
b.show_speed()


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def characteristics_of_cars(self):
        print(f'Автомобиль {self.name}, цвет {self.color}, полицейский {self.is_police}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed}')
        if self.speed > 40:
            print('Скорость превышена!')


c = WorkCar(45, 'зеленый', 'Уралец', False)
c.characteristics_of_cars()
c.show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def characteristics_of_cars(self):
        print(f'Автомобиль {self.name}, цвет {self.color}, полицейский {self.is_police}')


d = PoliceCar(60, 'белый', 'Ford', True)
d.characteristics_of_cars()
d.show_speed()
