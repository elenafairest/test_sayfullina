import statistics


def total_revenue(purchases):
    return sum([p['price'] * p['quantity'] for p in purchases])


def items_by_category(purchases):
    d = {}
    for p in purchases:
        lst = d.setdefault(p['category'], [])
        lst.append(p['item'])
    return d


def expensive_purchases(purchases, min_price):
    return [p for p in purchases if p['price'] >= min_price]


def average_price_by_category(purchases):
    d = {}
    for p in purchases:
        lst = d.setdefault(p['category'], [])
        lst.append(p['price'])

    for k in d.keys():
        d[k] = statistics.mean(d[k])

    return d

def most_frequent_category(purchases):
    d = {}
    for p in purchases:
        v = d.setdefault(p['category'], 0)
        d[p['category']] = v + p['quantity']

    return sorted(list(d.keys()), key=lambda k: d[k], reverse=True)[0]


purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]
print(f'Общая выручка: {total_revenue(purchases)}')
print(f'Товары по категориям: {items_by_category(purchases)}')
min_price = 1.0
print(f'Покупки дороже {min_price}: {expensive_purchases(purchases, min_price)}')
print(f'Средняя цена по категориям: {average_price_by_category(purchases)}')
print(f'Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}')