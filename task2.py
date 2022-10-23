# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
def f(x):
    return random.randint(0, 101)

k = int(input('Укажите степень многочлена: '))

index = [f(i) for i in range(k + 1)]

deg = ['x^' + str(i) for i in range(1, k + 1)]
deg.reverse()

print(index) #для наглядности и проверки

res = ''
for i in range(k):
    if index[i] == 0:
        continue
    else:
        if i < k - 1:
            res += str(index[i]) + '*' + str(deg[i]) + ' + '
        elif i == k - 1 and index[i + 1] != 0:
            res += str(index[i]) + '*x + ' + str(index[i + 1]) + ' = 0'
        else:
            res += str(index[i]) + '*x' + ' = 0'

with open('file.txt', 'a') as data:
    data.write(res)
