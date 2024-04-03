n = int(input())
a = n // 100 % 10
b = n // 10 % 10
c = n % 10
if a==b==c:
    print('Одинаковые')
else:
    print('Не одинаковые')
