# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def cloth_exp(self):
        pass


class Coat(Clothes):

    def __init__(self, name: str, v: float):
        super().__init__(name)
        self.v = v

    @property
    def cloth_exp(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, name: str, h: float) -> object:
        super().__init__(name)
        self.h = h

    @property
    def cloth_exp(self):
        return self.h * 2 + 0.3


num_1 = Suit("Костюм", 1.8)
num_2 = Coat("Пальто", 48)

print(f'{num_1.name}: Расход ткани - {num_1.cloth_exp:.2f} м2'
      f'\n{num_2.name}: Расход ткани - {num_2.cloth_exp:.2f} м2'
      f'\nОбщий расход ткани - {num_2.cloth_exp + num_2.cloth_exp:.2f} м2')
