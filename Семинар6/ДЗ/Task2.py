# Задача 32: Определить индексы элементов списка, 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
def create_array_1():
    n = int(input("Введите длину списка: "))
    number_min_1 = int(input("Введите минимальный предел : "))
    number_max_1 = int(input("Введите максимальный предел : "))
    list_1 = [random.randint(number_min_1, number_max_1) for i in range(n)]
    print(*list_1)
    return list_1

def Main(array):
    result = list()
    number_min = int(input("Введите минимальный предел поиска : "))
    number_max = int(input("Введите максимальный предел поиска: "))
    for i in range(len(array)):
        if number_min < array[i] < number_max:
            result.append(f"{i} - {array[i]}")                
    return result

print(*Main(create_array_1()))