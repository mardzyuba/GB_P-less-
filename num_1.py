# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

file_open = open('text_1.txt', 'w+')
while True:
    in_text = input("Введите данные, завершением ввода будет пробел и enter: \n")
    if in_text == " ":
        file_open = open('text_1.txt')
        print("\nPrint file:\n----------\n{0}---------- \nEnd file.".format(file_open.read()))
    elif in_text:
        file_open.write(in_text + "\n")
    else:
        print("Exit.\n")

    file_open.close()
