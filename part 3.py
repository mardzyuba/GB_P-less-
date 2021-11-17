# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    name: str
    surname: str
    position: str
    income: dict

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")

    def get_position_place(self):
        return f"{self.position}"


worker_1 = Position("Иван", "Скобанев", "Дизайнер", {"wage": 50000, "bonus": 5000})
worker_2 = Position("Елена", "Акипова", "Маркетолог", {"wage": 60000, "bonus": 7000})

print(f"1. Личные данные:  {worker_1.get_full_name()},\nДолжность: {worker_1.get_position_place()},\n "
      f"Зарплата сотрудника:  {worker_1.get_total_income()}")
print(f"2. Личные данные:  {worker_2.get_full_name()},\n Должность: {worker_2.get_position_place()},\n"
      f" Зарплата сотрудника:  {worker_2.get_total_income()}")
