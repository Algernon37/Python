# def f(x):
#     return (x*x)

# a = f 
# print(a(5))
# print(f(5))

# def calk1(a,b):
#     return(a+b)

# def calk2(a,b):
#     return(a*b)

# def math(op, x, y):
#     print(op(x,y))
    
# math(lambda a,b: a + b,5,45)

# Анонимные, lambda-функции
# Теперь, чтобы вызвать функцию суммы, достаточно просто вызвать sum.
# Также можно пропустить шаг создания переменной sum и сразу вызвать lambda:
# calc(lambda a,b: a + b, 4, 5) = 9

# Итак:

# Сначала мы избавились от классического описания функций.
# Затем научились описывать лябдыб присваивая результат какой-то переменной.
# После избавились от этой переменнойб пробрасывая всю лябду в качестве функции.

# import random

# def create_array_1():
#     n = int(input("Введите длину списка 1: "))
#     number_min_1 = int(input("Введите минимальный предел 1: "))
#     number_max_1 = int(input("Введите максимальный предел 1: "))
#     list_1 = [random.randint(number_min_1, number_max_1) for i in range(n)]
#     return list_1

# list_2 = []

# def Main(array1,array2):
#     for i in range(len(array1)):
#         if array1[i] % 2 == 0: 
#             array2.append((array1[i], array1[i] ** 2))
#     return array2     
    
    
# print(Main(create_array_1(),list_2)) - моё решение

#___________________________________________

# data = [1,2,3,5,8,15,23,38]
# res = list()

# for i in data:
#     if i % 2 == 0:
#          res.append((i,i**2))
# print(res) - что сделал лектор


# def where(f,col):
#     return[x for x in col if f(x)]

# data = [1,2,3,5,8,15,23,38]
# res = map(int,data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)



# Lambda-функции в Python - это анонимные (безымянные) функции, 
# которые могут быть определены и использованы на месте,
# где требуется функция. 
# Они являются компактным способом определения небольших функций одной строкой кода.
# #___________________________________________

# # list_1 = [x for x in range (1,20)]
# # print(list_1)

# # list_1 = list(map(lambda x: x + 10, list_1))
# # print(list_1)

# # Задача: Дан набор чисел в качестве строки. Как превратить list строк в list чисел?

# data = '15 345 6 1 6 856 12346'

# data = list(map(int, data.split()))
# print(data)

# # Функция map в Python используется для применения 
# заданной функции к каждому элементу итерируемого объекта 
# # (например, списка) и возвращает итератор, содержащий 
# # результаты применения этой функции.
# map(function, iterable)
# где:

# function - функция, которую нужно применить к каждому элементу итерируемого объекта.
# iterable - итерируемый объект, к которому будет применена функция.

# #___________________________________________

# data = [15,12,4326,456789,13,4,1245,43535]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# data = [1,2,3,5,8,15,23,38]
# res = map(int,data)
# res = filter(lambda x: x % 2 == 0, res)
# print(res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# Функция filter в Python используется для фильтрации элементов итерируемого объекта 
# (например, списка) на основе заданного условия. 
# Она создает итератор, содержащий только те элементы, 
# для которых условие истинно.

# Синтаксис функции filter выглядит следующим образом:

# python
# Copy code
# filter(function, iterable)
# где:

# function - функция, которая принимает один аргумент 
# (элемент итерируемого объекта) и возвращает True или False в зависимости от условия.
# iterable - итерируемый объект, который будет фильтроваться.


# #___________________________________________

# Функция zip в Python используется для объединения элементов 
# нескольких итерируемых объектов (например, списков) в один итератор, 
# который возвращает кортежи из соответствующих элементов этих объектов.

# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 35]
# countries = ['USA', 'Canada', 'UK']

# # Объединение списков
# data = zip(names, ages, countries)

# # Вывод результатов
# for item in data:
#     print(item)
    
# ('Alice', 25, 'USA')
# ('Bob', 30, 'Canada')
# ('Charlie', 35, 'UK')

# #___________________________________________


# # Функция enumerate в Python используется для перебора элементов последовательности 
# # (например, списка) вместе с их индексами. 
# # Она возвращает итератор, 
# # который генерирует пары из индекса элемента и самого элемента.
# fruits = ['apple', 'banana', 'orange']

# # Перебор элементов списка с индексами
# for index, fruit in enumerate(fruits):
#     print(index, fruit)

# 0 apple
# 1 banana
# 2 orange