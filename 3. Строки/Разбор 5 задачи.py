s = input()

# replace(<что ищем>, <чем заменяем>, <сколько раз>)
# count(<что ищем>) - функция находит кол-во символов в строке
# Вычитаем 1, чтобы удалить не все символы, а на 1 меньше, чем есть
s = s.replace(s[-1], '', s.count(s[-1]) - 1)
print(s)
