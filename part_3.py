# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка и тд.
# сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).


class Cell:
    """В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число)."""

    def __init__(self, cell_parameter: int):
        self.cell_parameter = cell_parameter

    def __str__(self):
        return f"{self.cell_parameter}"

    """Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
     (с округлением до целого)"""

    def __add__(self, other):
        return Cell(round(self.cell_parameter + other.cell_parameter))

    """Участвуют две клетки. Операцию необходимо выполнять 
    только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение."""

    def __sub__(self, other):
        if self.cell_parameter - other.cell_parameter > 0:
            return Cell(round(self.cell_parameter - other.cell_parameter))
        else:
            return "Разность количества ячеек двух клеток меньше, либо равно нулю"

    """Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества
         ячеек этих двух клеток."""

    def __mul__(self, other):
        return Cell(self.cell_parameter * other.cell_parameter)

    """Создается общая клетка из двух. Число ячеек общей клетки определяется как 
    целочисленное деление количества ячеек этих двух клеток."""

    def __truediv__(self, other):
        return Cell(self.cell_parameter // other.cell_parameter)

    def make_order(self, quantity):
        rows = self.cell_parameter // quantity
        return "{0}\n{1}".format('\n'.join(''.join('*' for i in range(quantity)) for i in range(rows)),
                                 "".join("*" for i in range(self.cell_parameter % quantity)))


cell1 = Cell(40)
cell2 = Cell(30)

print(cell1 + cell2)
print(cell1 - cell2)
print(cell2 - cell1)
print(cell1 * cell2)
print(cell1 / cell2)

print(cell1.make_order(5))
