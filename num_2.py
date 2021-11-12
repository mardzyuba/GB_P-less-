# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_file = open("text_2.txt", "r")
count_1 = sum(1 for line in my_file)
print(f"Количество строк в файле: {count_1}")

my_file.close()

with open("text_2.txt", "r") as my_f:
    for x, line in enumerate(my_f):
        if 1 == len(line.split(' ')):
            print(f"В строке * {x + 1} - {len(line.split(' '))} количество слов")
        elif 1 < len(line.split(' ')) < 10:
            print(f"В строке * {x + 1} - {len(line.split(' '))} количество слов")
        elif len(line.split(' ')) >= 10:
            print(f"В строке * {x + 1} - {len(line.split(' '))} количество слов")
