# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

#Пример:
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
flag = True
num = int(input('Введите коэффециент: '))
f = open('mnogochlen.txt','a')
while flag:
    rand = random.randint(0, 100)
    if num == 0:
        if rand == 0:
            f.write('')
        else:
            f.write(f'{rand}')
            num -= 1
    elif num == -1:
        f.write(' = 0\n')
        flag = False
    else:
        if rand == 0:
            f.write('')
        else:
            if num == 1:
                f.write(f'{rand}x + ')
                num -= 1
            else:
                f.write(f'{rand}x^{num} + ')
                num -= 1
f.close()