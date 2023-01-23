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

def check_line(sum_O, sum_X):
    move = ''
    for item in win_line:
        o = 0
        x = 0
        for j in range(3):
            if cell[item[j]] == 'O':
                o += 1
            if cell[item[j]] == 'X':
                x += 1
        if o == sum_O and x == sum_X:
            for j in range(3):
                if cell[item[j]] != 'O' and cell[item[j]] != 'X':
                    move = cell[item[j]]
    return move

def comp():        
    move = ''
    move = check_line(2,0)
    
    if move == '':
        move = check_line(0,2)        
 
    if move == '':
        move = check_line(1,0)           
    
    if move == '':
        if cell[4] != 'X' and cell[4] != 'O':
            move = 5           
 
    if move == '':
        if cell[0] != 'X' and cell[0] != 'O':
            move = 1           
    return move

game_over = False
count = 0 
while not game_over:
    create_cell(cell)
    if count %2 != 1:
        xo = 'X'
        move = int(input('Ваш ход, выбирайте ячейку: '))
    else:
        print('Ход компьтера:')
        xo = 'O'
        move = comp()
    count+= 1
    motion(move,xo) 
         
    if count >4:
        win = check_win()
        if win:
            create_cell(cell)
            print(f'Победили {win}!!!')
            game_over = True
            break
    if count ==9:
        create_cell(cell)
        print('Ничья!!!')
        game_over = True
        
 

    






