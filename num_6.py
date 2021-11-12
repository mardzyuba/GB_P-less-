# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий
# по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
from typing import List

import tools, os

def run():
    path = tools.get_dir("Lesson 5")
    if path is None:
        print("Директория с данными не обнаружена. Проверьте, что Вы загрузили все файлы проекта.")
        return

    path = os.path.join(path, "text_6.txt")
    if not os.path.exists(path) or not os.path.isfile(path):
        print("Файл с данным для этого задания не обнаружен.\r\n" + path +
              "\r\nПроверьте, что Вы загрузили все файлы проекта.")
        return


with open("text_6.txt") as my_file:
    result_list = my_file.read().split('\n')
dictionary = {pair[0].strip(): pair[1].strip() for pair in (line.split(': ') for line in result_list if line) if
              len(pair) == 2}
names = {"лаб)": "Лабораторная работа", "л)": "Лекция", "пр)": "Практические занятия"}
for key in dictionary.keys():
    dictionary[key] = {names[pair[1]]: int(pair[0]) for pair in (parts.split('(') for parts in dictionary[key].split())
                       if len(pair) == 2}

print("Всего занятий: ",
      *(f" {key}-{sum} ч." for key, sum in {(key, sum(dictionary[key].values())) for key in dictionary.keys()}))
