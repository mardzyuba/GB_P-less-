# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

change_file = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new_file = []

with open("text_4.txt") as my_file:
    for i in my_file:
        i = i.split(" ", 1)
        new_file.append(change_file[i[0]] + " " + i[1])
    print(f"{new_file} ")

with open("text_4_new.txt", "w", encoding="utf-8") as my_file_2:
    my_file_2.writelines(new_file)
