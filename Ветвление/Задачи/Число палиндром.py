n = int(input())
a = n // 100
b = n // 10 % 10
c = n % 10
if a == b == c or a == c:
    print('Это число - палиндром')
else:
    print('Это число - не палиндром')

