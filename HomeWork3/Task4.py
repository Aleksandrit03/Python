#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10
n = int(input('Введите число: '))
array = list()
while n > 1:
    if n % 2 == 0:
        n = round(n/2)
        array.append(0)
    else: 
        n = n//2
        array.append(1)
array.append(n)
array.reverse()
print('Ваше число в двоичном коде: ')
print(array)