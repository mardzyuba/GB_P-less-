# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

# 1 вариант
a_a = float(input("Введите аргумент-число а >>"))
b_b = float(input("Введите аргумент-число b >>"))
c_c = float(input("Введите аргумент-число c >>"))


def my_func(a, b, c):
    min_x = min(a, b)
    min_x = min(min_x, c)

    return a + b + c - min_x


print(a_a, b_b, c_c, "сумма наибольших двух аргументов = ", my_func(a_a, b_b, c_c))

# 2 вариант

a_1 = float(input("Введите аргумент-число а >>"))
b_2 = float(input("Введите аргумент-число b >>"))
c_3 = float(input("Введите аргумент-число c >>"))


def my_func_1(x, y, z):
    if x >= y >= z:
        return x + y
    elif y < x < z:
        return x + z
    else:
        return y + z


print(a_1, b_2, c_3, "сумма наибольших двух аргументов = ", my_func_1(a_1, b_2, c_3))
