def sum(x,y):  # Функция сложения 
    return x + y
f = sum # Можно присвоить функцию какому то аргументу

def mult(x,y): # Функция умножения
    return x * y

g = mult
def calc(op, a, b): # Функция с помощью которой мы можем передать функцию как аргумент (ор).
    print(op(a,b))  # Значения "а" и "b" не должны быть идентичны тем что в функциях

calc(mult, 4, 5)
calc(sum, 4, 5)
calc(g, 4, 5)
calc(f, 4, 5)

                                  # ЛЯМБДА
summ = lambda x, y: x + y # Первую функцию можно переписать так
print(summ(4, 6))
calc(summ, 4, 7)
calc(lambda x, y: x + y, 4, 11)

                                  # СПИСОК
spisok = [i for i in range(1, 21) if i%2 == 0]
print(spisok)

data = list(map(int,input().split())) # Преобразование вводимых значений в лист
print(data)
                                  # СПИСОК КОРТЕЖЕЙ
def mult(x): 
    return x**2
spisok = [(i, mult(i)) for i in range(1, 21) if i%2 == 0]
print(spisok)
#                                    Функция filter - фильтрует данные
data = [x for x in range(10)]
result = list(filter(lambda x:not x % 2, data))
print(result)