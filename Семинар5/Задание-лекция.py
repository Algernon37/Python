# def sum_numbers(n, y = "hello"):
#     sum=0
#     print(y)
#     for i in range(1,n+1):
#         sum += i
#     return sum
#     print('stop')

# a = sum_numbers(5, "папа")
# print(a)

# def sum_str(*args):
#     res = 0 
#     for i in args:
#         res += i 
#     return res

# print(sum_str(1,8,9))

# import modul1

# print(modul1.max1(5,9))

# from modul1 import max1

# print(max1(5,9))

# def f(n):
#     if n in [1,2]:
#         return 1
#     return f(n-1) + f(n-2)

# list_1 = []
# for i in range(1,10):
#     list_1.append(f(i))
# print(list_1)

# быстрая сортировка:

# def x(array):
#     if len(array) <=1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     bigger = [i for i in array[1:] if i > pivot]
#     return x(less) + [pivot] + x(bigger)
# print(x([15,1235,13,6,3,134,3145,6]))

# сортировка слиянием:

def sort(nums):
    if len(nums)>1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        sort(left)
        sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i +=1
            else:
                nums[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            nums[k] = left[j]
            j += 1
            k += 1

list_1 = [1,2,4,6,7,34,7,2,245,2457,1,6,7,4]
sort(list_1)
print(list_1)