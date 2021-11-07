# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

new_list = []
for el in range(100, 1000):
    if el % 2 == 0:
        new_list.append(el)


def my_func(prev_el, now_el):
    return prev_el * now_el


print(reduce(my_func, new_list))