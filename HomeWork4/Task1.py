#Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, 
#сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)
n = int(input('Введите число: '))
pi = float(open('ChisloPI.txt'))
#c = round(, n)
print(pi)
exit()
data = []
with open("ChisloPI.txt") as n:
    for line in n:
        print()