nums = [4, 78, 11, 2, 65, 1]

''' 
    .sort() - Функция, сортирующая массив. Функция изменяет массив, в котором вызывается.
    Параметры функции:
        reverse - изменяет направление сортировки. (True, False - по умолчанию)
'''
nums.sort(reverse=True)
print(nums)

'''
    sorted() - Функция, сортирующая массив. Функция не изменяет исходный массив.
    Параметры функции такие же, как и у sort()
'''

nums = sorted(nums, reverse=False)
print(nums)
