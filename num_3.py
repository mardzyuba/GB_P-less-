# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

my_file = open("text_3.txt")
list_person = {}
print(f"Список сотрудников с окладом менее 20К:")
for line in my_file:
    key, value = line.split()
    list_person[key] = float(value)
    if float(value) < 20000:
        print(f"{key} -  {value} y.e.")

salary = float(sum(list_person.values()))
avg_salary = round(salary/len(list_person), )
print(f"\n----------\n  Средний доход сотрудников равен {avg_salary} y.e.")
my_file.close()
