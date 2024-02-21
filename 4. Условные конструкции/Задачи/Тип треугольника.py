a = int(input())
b = int(input())
c = int(input())
if (a+b) < c or (a+c) < b or (b+c) < a:
    print('impossible')
elif (a**2 + b**2) == c**2:
    print('rectangular')
elif (a**2 + b**2) < c**2:
    print('obtuse')
elif (a**2 + b**2) > c**2:
    print('acute')



