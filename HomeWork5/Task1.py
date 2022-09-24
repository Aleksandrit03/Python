#Создайте программу для игры с конфетами человек против человека.

#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""
# Смысл игры в том чтобы за 2 хода(по 1 ходу каждого игрока) было взято 29 конфет(ЕСЛИ ПЕРВЫЙ ХОД ВТОРОГО)
from random import randint as rand
candy = 400
random_number = rand(0, 1)
count = 0
if random_number == 0:
    count = 1
else:
    count = 2
def Bot(candy):
    if candy // 28 > 1:
        candy = rand(10, 28)
    elif 0 < candy < 29:
        candy = candy
    elif candy < 100:
        candy = rand(5, 12)
    else:
        candy = candy % 28
    return candy
def Game(candy, count):
    if count % 2 == 0:
        print('Ходит бот')
        candy = Bot(candy)
        return  candy
    else:
        print('Ходит первый игрок')
        flag = False
        while not flag:
            count = int(input('Сколько конфет хотите взять: '))
            if count > 28 or count < 0:
                print('Подумайте еще')
            else:
                flag = True
        return count

while candy != 0:
    tamp = Game(candy, count)
    print(f'{tamp} конфет взяли')
    candy = candy - tamp
    print(f'{candy} конфет осталось')
    if candy == 0:
        if count % 2 == 0:
            print('Победил бот')
        else:
            print('Победил игрок')
    count += 1