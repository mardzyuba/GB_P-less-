# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

my_list = [
    ['Зима', ['12', '1', '2']],
    ['Весна', ['3', '4', '5']],
    ['Лето', ['6', '7', '8']],
    ['Осень', ['9', '10', '11']]
]

my_dict = {
    'Зима': ['12', '1', '2'],
    'Весна': ['3', '4', '5'],
    'Лето': ['6', '7', '8'],
    'Осень': ['9', '10', '11']
}

while True:
    month_number = input('Пожалуйста введите номер месяца: ')
    if month_number not in sum(my_dict.values(), []):
        print('Неправильно введенный номер месяца. Попробуйте еще раз')
        continue

    break

for season, months in my_list:
    if month_number in months:
        print(f'В списке указано, что месяц с номером "{month_number}" это "{season}"')

for season, months in my_dict.items():
    if month_number in months:
        print(f'В словаре указано, что месяц с номером "{month_number}" это "{season}"')
