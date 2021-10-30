# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.


products, order = [], 1
name, price, amount, unit = None, None, None, None

while True:
    if name is None:
        name = input('Введите название товара: ')
        if not name.isalnum():
            print('Наименование товара не может быть пустым. Попробуйте еще раз.')
            continue

        name = str(name)

    if price is None:
        price = input('Введите стоимость товара: ')
        if not price.isdigit():
            print('Цена должна быть целым числом. Попробуйте еще раз.')
            continue

        price = int(price)

    if amount is None:
        amount = input('Введите количество: ')
        if not amount.isdigit():
            print('Количество должно быть целым числом. Попробуйте еще раз.')
            continue

        amount = int(amount)

    if unit is None:
        unit = input('Введите единицу измерения: ')
    if not unit.isalpha():
        print('Единица изменерения не может быть пустой. Попробуйте еще раз.')
        continue

    unit = str(unit)

    products.append((order, {'name': name, 'price': price, 'amount': amount, 'unit': unit}))

    name, price, amount, unit = None, None, None, None
    order += 1

    print(products)

    qv = input('Нажмите enter, чтобы продолжить список, либо введите ok ,чтобы выйти: ')
    if qv.lower() == 'ok':
        break

# Словарь
analytic = {'name': [], 'price': [], 'amount': [], 'unit': set()}

for _, item in products:
    analytic['name'].append(item['name'])
    analytic['price'].append(item['price'])
    analytic['amount'].append(item['amount'])
    analytic['unit'].add(item['unit'])

print(analytic)
