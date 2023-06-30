# Напишите функцию, 
# которая принимает одно число и проверяет, 
# является ли оно простым

# def simple_number(n):
#     count = 0 
#     for i in range(1,n+1):
#         if n%i == 0:
#             count += 1
#     if count == 2:
#         print("Число простое") 
#     else: 
#         print("Число не простое")    

# n = int(input("Введите число: "))
# simple_number(n)
n = int(input("Введите число: "))

def is_simple(num: int) -> bool:
    if num in [1,2]:
        return True
    elif not num%2:
        return False
    for i in range(3, num//2 + 1, 2):
        if num%i == 0:
            return False
    return True
print(is_simple(n))
