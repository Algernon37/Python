# Дано натуральное число N и последовательность 
# из N элементов. 
# Требуется вывести эту последовательность 
# в обратном порядке.

n = int(input("Введите число элементов строки: "))
str_1 = list()
for i in range(0,n):
    str_1.append(input("Введите элемент строки: "))

print(*str_1 )

my_string = ' '.join(str_1)

def restart(string):   
    if len(string) == 0:
        return string
    else:
        return restart(string[1:]) + string[0]

print(restart(my_string))