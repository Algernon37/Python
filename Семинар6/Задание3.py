# Дан список чисел. 
# Посчитайте, сколько в нем пар элементов, 
# равных друг другу. Считается, что любые два элемента,
# равные друг другу образуют одну пару, 
# которую необходимо посчитать.


import random


def create_array_1():
    n = int(input("Введите длину списка 1: "))
    number_min_1 = int(input("Введите минимальный предел 1: "))
    number_max_1 = int(input("Введите максимальный предел 1: "))
    list_1 = [random.randint(number_min_1, number_max_1) for i in range(n)]
    return list_1

def Main(array):
    print(*array)
    count = 0
    used_indexes = []
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j] and i not in used_indexes and j not in used_indexes:
                count += 1
                used_indexes.append(i)
                used_indexes.append(j)
    return count

print(Main(create_array_1()))

# my_list = [random.randint(1, 10) for i in range(30)]

# repeats = sum([my_list.count(i)//2 for i in set(my_list)])

# print(repeats)