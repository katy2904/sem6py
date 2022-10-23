# Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.

import random

def player_draw(pl_1, pl_2):
    pl_1_1, pl_1_2, pl_2_1, pl_2_2 = 0, 0, 0, 0
    while (pl_1_1 + pl_1_2) == (pl_2_1 + pl_2_2):
        print(f'{pl_1} бросает:')
        pl_1_1, pl_1_2 = random.randint(1, 6), random.randint(1, 6)
        print(f'выпало {pl_1_1} и {pl_1_2}. Сумма {pl_1_1 + pl_1_2}')

        print(f'{pl_2} бросает:')
        pl_2_1, pl_2_2 = random.randint(1, 6), random.randint(1, 6)
        print(f'выпало {pl_2_1} и {pl_2_2}. Сумма {pl_2_1 + pl_2_2}')

        if (pl_1_1 + pl_1_2) == (pl_2_1 + pl_2_2):
            print('Ничья! Кидаем еще раз!')

    if (pl_1_1 + pl_1_2) > (pl_2_1 + pl_2_2):
        return pl_1
    elif (pl_1_1 + pl_1_2) < (pl_2_1 + pl_2_2):
        return pl_2

def print_field(area):
    for el in area:
        print(el)

def replacing_the_value_X(area, n):
    for el in area:
        for i in range(len(el)):
            if el[i] == n:
                el[i] = 'X'

def replacing_the_value_O(area, n):
    for el in area:
        for i in range(len(el)):
            if el[i] == n:
                el[i] = 'O'

def check(area):
    if (area[0] == ['X', 'X', 'X'] or area[1] == ['X', 'X', 'X'] or area[2] == ['X', 'X', 'X'] or
       area[0][0] == area[1][0] == area[2][0] == 'X' or
       area[0][1] == area[1][1] == area[2][1] == 'X' or
       area[0][2] == area[1][2] == area[2][2] == 'X'):
        print(f'Поздравляю, выйграл игрок {p1}')
        return True
    elif (area[0] == ['O', 'O', 'O'] or area[1] == ['O', 'O', 'O'] or area[2] == ['O', 'O', 'O'] or
         area[0][0] == area[1][0] == area[2][0] == 'O' or
         area[0][1] == area[1][1] == area[2][1] == 'O' or
         area[0][2] == area[1][2] == area[2][2] == 'O'):
        print(f'Поздравляю, выйграл игрок {p2}')
        return True

field = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print('Давай поиграем! Крестики-нолики, поле 3х3')
player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя второго игрока: ')

print('А теперь жеребьевка! Бросаем кубики!')

p1 = player_draw(player1, player2)
print(f'Первый ход делает {p1}')
if p1 == player1:
      p2 = player2
else:
      p2 = player1

print('Перед вами игровое поле')
print_field(field)
print('Чтобы сделать ход, просто укажите номер позиции, на которую хотите поставить X или O')

while True:
    x = int(input(f'{p1}, твой ход: '))
    replacing_the_value_X(field, x)
    print_field(field)
    if check(field) == True:
        break
    o = int(input(f'{p2}, твой ход: '))
    replacing_the_value_O(field, o)
    print_field(field)
    if check(field) == True:
        break
