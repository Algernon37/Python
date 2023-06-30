# Дан список, состоящий из целых чисел. 
# Напишите программу, которая в данном списке 
# определит количество элементов, 
# у которых два соседних и, 
# при этом, оба соседних элемента меньше данного.

import random


def create_array_1():
    n = int(input("Введите длину списка 1: "))
    number_min_1 = int(input("Введите минимальный предел 1: "))
    number_max_1 = int(input("Введите максимальный предел 1: "))
    list_1 = [random.randint(number_min_1, number_max_1) for i in range(n)]
    return list_1

def Main(array):
    count = 0
    print(*array)
    for i in range(1,len(array)-1):
        if array[i - 1] < array[i] > array[i + 1]:
            count += 1
    return count

print(Main(create_array_1()))
