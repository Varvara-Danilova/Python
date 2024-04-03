print('Ведите точку')
x = int(input())
print('Введите начало отрезка и конец отрезка поочерёдно')
a = int(input())
b = int(input())
if x>a and x<b:
    print('Принадлежит')
else:
    print('Не принадлежит')