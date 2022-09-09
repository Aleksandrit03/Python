# Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно

n = int(input('Введите число: '))
print(n)
result = 0
k = 0
while k < n:
    k = k + 1
    result = result + k
print(result)