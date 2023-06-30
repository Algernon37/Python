# 39. Даны два списка чисел. 
# Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), 
# которых нет во втором массиве


import random
def create_array_1():
    n = int(input("Введите длину списка 1: "))
    number_min_1 = int(input("Введите минимальный предел 1: "))
    number_max_1 = int(input("Введите максимальный предел 1: "))
    list_1 = [random.randint(number_min_1, number_max_1) for i in range(n)]
    return list_1

def create_array_2():
    m = int(input("Введите длину списка 2: "))
    number_min_2 = int(input("Введите минимальный предел 2: "))
    number_max_2 = int(input("Введите максимальный предел 2: "))
    list_2 = [random.randint(number_min_2, number_max_2) for i in range(m)]  
    return list_2

def main(array1,array2):
    print(*array1)
    print(*array2)
    print(" ")
    for i in array2:
        if i in array1:
            array1.remove(i)
    return array1

print(*main(create_array_1(),create_array_2()))




