#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.

#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

spisok = [1.1, 1.2, 3.1, 5, 10.01]
for i in range(5):
    spisok[i] = round(spisok[i] % 1, 2)
item = 0
spisok.remove(item)
print(spisok)
razniza = max(spisok) - min(spisok)
print(razniza)