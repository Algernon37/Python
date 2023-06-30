# Хакер Василий получил доступ к классному журналу
# и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, 
# но наоборот: все максимальные – на минимальные.
import random


n = int(input("Введите колличесвто оценок: "))
evaluations = [random.randint(1, 5) for i in range(n)]
max_evaluations = max(evaluations)
min_evaluations = min(evaluations)
print(*evaluations)
print(' ')
for i in range(len(evaluations)):
    if evaluations[i] == max_evaluations:
        evaluations[i] = min_evaluations
print(*evaluations)

# evaluations = [min(evaluations) if i == max(evaluations) else i for i in evaluations]
# print(*evaluations)