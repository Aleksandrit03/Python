# a - дозапись текста в файл
# w - перезапись файла(удаление старого и создание нового)
# r - чтение файлов
#colors = ['red', 'green', 'blue']
#data = open('file.txt', 'w')
# data.writelines(colors) # разделителей не будет, но можно добавить
#data.writelines('Line3') 
#data.close()
# Возможно вот так вот еще
#with open('file.txt', 'w') as data:
#    data.write('Line 1\n')
#    data.write('Line 2\n')

# Чтение файлов 
#path = 'file.txt'
#data = open(path, 'r')
#for line in data:
#    print(line)
#data.close()

#exit()

#                  ФУНКЦИИ И МОДУЛИ
# Можно использовать функцию написанную в другом файле через
# import hello as h, где hello - название файла,
# as(или) изменить название на более удобное(на h) 
#def new_string(symbol, count): # count можно зафиксировать значение(symbol, count = 3)
#    return symbol * count

#print(new_string('!', 5)) # Правильное написание, выдаст это (!!!!!)
#print(new_string('!')) # Не правильное написание, будет ошибка
#                               КОРТЕЖИ () - неизменяемый список
a = (3, 4) # кортеж из пары чисел
print(a)
print(a[0]) # Возможно указать какой элемент необходимо вывести на экран
print(a[-1])
# a[0] = 12 Присвоение  кортежах не работает, 
# Если хочешь кортеж из одного числа не забудь поставить запятую a = (3,)

# Можно использовать for для перебора
for item in a:
    print(item)


#                                    СЛОВАРИ
dictionary = {}
dictionary = \
    {
        'up': 'вверх',
        'down': 'вниз'
    }
print(dictionary) # Можно распечатать словарь
print(dictionary['up']) # Можно и так

# Печать всех ключей
for k in dictionary.keys():
    print(k)

# Печать значений
for k in dictionary.values():
    print(k)