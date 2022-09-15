#Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, 
#сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)
n = int(input('Введите число: '))
#c = round(, n)
data = []
with open("ChisloPI.txt") as n:
    for line in n:
        data.append([float(x) for x in line.split()])