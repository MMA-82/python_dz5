#Создайте программу для игры в 'Крестики-нолики'
welcome = 'Игра крестики-нолики с компьютером:'
print(welcome.upper())
cell = list(range(1,10)) 
def create_cell(cell):
    print('=' * 15)
    for i in range(3):
        print(' |', cell[0+i*3], '|', cell[1+i*3], '|', cell[2+i*3], '| ')
        print('=' * 15)

win_line = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

def motion(move, xo):
    cell[cell.index(move)] = xo

def check_win():
    for item in win_line:
        if cell[item[0]] == cell[item[1]] == cell[item[2]]:
            return cell[item[0]]

def check_move(numO, numX):
    move = ''
    for item in win_line:
        count_o, count_x = 0, 0 
        for i in range(3):
            if cell[item[i]] == 'O':
                count_o += 1
            if cell[item[i]] == 'X':
                count_x += 1
        if count_o == numO and count_x == numX:
            for i in range(3):
                if cell[item[i]] != 'O' and cell[item[i]] != 'X':
                    move = cell[item[i]]
    return move

def comp():        
    move = ''
    move = check_move(2,0)

    if move == '':
        move = check_move(0,2)        
 
    if move == '':
        move = check_move(1,0)  

    if move == '':
        move = check_move(1,1) 
        
    if cell[4] != 'X' and cell[4] != 'O':
        move = 5
    if cell[0] != 'X' and cell[0] != 'O':
        move = 1           
    return move

gameover = False
count = 0 
while not gameover:
    create_cell(cell)
    if count %2 != 1:
        xo = 'X'
        move = int(input('Ваш ход, выбирайте ячейку: '))
    else:
        xo = 'O'
        print(f'Ход компьтера: {comp()}')
        move = comp()
    count+= 1
    motion(move,xo) 
         
    if count >4:
        if check_win():
            create_cell(cell)
            print(f'Победили {check_win()}!!!')
            gameover = True
            #break
      
    if count >7:
        if not check_win():
            create_cell(cell)
            print('Нет больше выигрышных ходов, ничья!!!')
            gameover = True
print('Игра окончена.')

        
 

    






 

    






