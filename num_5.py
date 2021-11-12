# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


import random

my_list = tuple([random.randint(1, 9) for i in range(10)])
print(my_list)

with open("text_5.txt", "w") as my_file:
    print(*my_list, file=my_file)

with open("text_5.txt") as my_file_2:
    result = sum(map(int, my_file_2.read().split()))
    print(f"Сумма чисел в файле равна -  {result}")
