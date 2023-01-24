#Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход

from random import randint as R
table = R(50, 101)
print(f'На столе {table} конфет')
rang = input('Бросаем жребий, чей первый ход да/нет? ')
sum_hum, sum_comp = 0, 0
count = 0
if 'да' in rang:
    lot = R(0, 1)
    if lot == 0:
        print(f'Выпало {lot}, Вы ходите первым')
        while table >= 28:
            if count %2 != 1:
                human = int(input('Сколько возьмете конфет? '))
                table -= human
                sum_hum += human
            else:
                comp = R(1, 29)
                print(f'Комп берет {comp} конфет')
                table -= comp
                sum_comp += comp
            count += 1
            print(f'На столе осталось {table} конфет')
    else:
        print(f'Выпало {lot}, первым ходит комп')
        while table >= 28:
            if count %2 != 1:
                comp = R(1, 29)
                print(f'Комп берет {comp} конфет')
                table -= comp
                sum_comp += comp
            else:
                human = int(input('Сколько возьмете конфет? '))
                table -= human
                sum_hum += human
            count += 1
            print(f'На столе осталось {table} конфет')

                