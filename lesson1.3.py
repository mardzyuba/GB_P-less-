# 3 Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input("Введите число >>>"))
nn = int(str(n)+str(n))
nnn = int(str(n)+str(n)+str(n))
summa = n + nn + nnn
print("{} + {} + {} = {}".format(n, nn, nnn, summa))
