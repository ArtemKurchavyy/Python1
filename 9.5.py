class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки "{self.title}"')


a = Pen('Ручка')
a.draw()


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки "{self.title}"')


b = Pencil('Карандаш')
b.draw()


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки "{self.title}"')


c = Handle('Маркер')
c.draw()

