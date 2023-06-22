# Обычный генератор
nums = [i for i in range(10)]
# Генератор с действием над переменной
nums = [i ** 2 for i in range(10)]
# Генератор с условием
nums = [i ** 2 for i in range(10) if i % 2 == 0]
print(nums)