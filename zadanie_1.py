#Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход

from random import randint as R
table = R(50, 100)
sum_h, sum_c = 0, 0
print('Бросаем жребий')
lot = R(0,1)
if lot == 0:
    print(f'Выпало {lot}, Ваш ход!!!')
    count = 0
    while table > 0:
        if count %2 != 1:
            human = int(input(f'На столе {table} конфет, сколько возьмете? '))
            if human >0 and human <= table and human <= 28:
                table-= human
                sum_h+= human
            else:
                print('Некорректный ввод. Максимум можете взять 28 конфет за раз!')
                human = int(input(f'На столе {table} конфет, сколько возьмете? '))
                if human >0 and human <= table and human <= 28:
                    table-= human
                    sum_h+= human
        else:
            if table > 28:
                comp = R(1, 28)
                print(f'Комп берет {comp} конфет')
                table-= comp
                sum_c+= comp
            else:
                comp = table
                print(f'Комп забирает все оставшиеся {table} конфет')
                table-= comp
                sum_c+= comp
        count+= 1
    if count %2 != 0:
        sum_h+= sum_c
        print(f'Вы победили и забрали все {sum_h} конфет')
    else:
        sum_c+= sum_h
        print(f'Комп выиграл и забрал все {sum_c} конфет')
else:
    print(f'Выпало {lot}, ход компа!!!')
    count = 0
    while table > 0:
        if count %2 != 1:
            if table > 28:
                comp = R(1, 28)
                print(f'На столе {table} конфет. Комп берет {comp} конфет')
                table-= comp
                sum_c+= comp
            else:
                comp = table
                print(f'Комп забирает оставшиеся {table} конфет')
                table-= comp
                sum_c+= comp
        else:
            human = int(input(f'На столе {table} конфет, сколько возьмете? '))
            if human >0 and human <= table and human <= 28:
                table-= human
                sum_h+= human
            else:
                print('Некорректный ввод. Максимум можете взять 28 конфет за раз!')
                human = int(input(f'На столе {table} конфет, сколько возьмете? '))
                if human >0 and human <= table and human <= 28:
                    table-= human
                    sum_h+= human
        count+= 1
    if count %2 != 0:
        sum_c+= sum_h
        print(f'Комп выиграл и забрал все {sum_c} конфет')
    else:
        sum_h+= sum_c
        print(f'Вы победили и забрали все {sum_h} конфет')
print('Игра окончена, приходите еще!!!')
                