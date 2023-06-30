# Планеты вращаются вокруг звезд по эллиптическим орбитам. 
# Назовем самой далекой планетой ту, орбита которой имеет 
# самую большую площадь. Напишите функцию 
# find_farthest_orbit(list_of_orbits), которая среди списка орбит 
# планет найдет ту, по которой вращается самая далекая 
# планета. Круговые орбиты не учитывайте: вы знаете, что у 
# вашей звезды таких планет нет, зато искусственные спутники 
# были были запущены на круговые орбиты. Результатом 
# функции должен быть кортеж, содержащий длины полуосей 
# эллипса орбиты самой далекой планеты. Каждая орбита 
# представляет из себя кортеж из пары чисел - полуосей ее 
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, 
# где a и b - длины полуосей эллипса. При решении задачи 
# используйте списочные выражения. Подсказка: проще всего 
# будет найти эллипс в два шага: сначала вычислить самую 
# большую площадь эллипса, а затем найти и сам эллипс, 
# имеющий такую площад

import random


# a = [random.randint(1, 10) for i in range(10)]
# b = [random.randint(1, 10) for i in range(10)]
# res = list(zip(a,b))

# def Main(a,b):
#     if a != b:
#         return((a,b))

# res = list(filter(Main(), res))
# print(res)

from math import pi

def find_farthest_orbit(list_of_orbits: list) -> tuple:
    dict_ ={round(pi * orbit[0] / 2 * orbit[1] / 2, 2): orbit for orbit in
        filter(lambda orbit: orbit[0] != orbit[1], list_of_orbits)}
    return dict_

a = [random.randint(1, 10) for i in range(10)]
b = [random.randint(1, 10) for i in range(10)]
orbits = list(zip(a,b))

dict_p = find_farthest_orbit(orbits)
print(max(dict_p), dict_p[max(dict_p)])