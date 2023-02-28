#Заполните один кортеж десятью случайными целыми числами от 0 до 5
# включительно. Так же заполните второй кортеж числами от-5 до 0.
# Для заполнения кортежей числами напишите одну функцию. Объедините
# два кортежа с помощью оператора +, создав тем самым третий кортеж.
# С помощью метода кортежа count() определите
# в нем количество нулей. Выведите на экран третий кортеж
# и количество нулей в нем.

import random

def fill_tuple(max, min):
    list_for_tuple = list()
    for i in range(10):
        list_for_tuple.append(random.randint(min,max))
    return list_for_tuple

tuple1 = tuple(fill_tuple(5, 0))
tuple2 = tuple(fill_tuple(0, -5))

print('tuple1: ', tuple1)
print('tuple2: ', tuple2)

tuple_union = tuple1 + tuple2
print('tuple_union: ', tuple_union)
print('Count of Zero: ', tuple_union.count(0))
