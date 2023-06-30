# Напишите функцию same_by(characteristic, objects),
# которая 
# проверяет, все ли объекты имеют одинаковое значение 
# некоторой характеристики, и возвращают True, 
# если это так. 
# Если значение характеристики для разных объектов 
# отличается - то False. Для пустого набора объектов, 
# функция 
# должна возвращать True. Аргумент characteristic - это 
# функция, которая принимает объект и вычисляет его 
# характеристику.



def same_by(characteristic, objects):
    set_1 = set(map(characteristic, objects))
    return len(set_1) > 1

my_list = []   
print(same_by(lambda objects: objects % 2, my_list))


