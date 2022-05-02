#tictactoe

# setup
from random import gammavariate


p1name = input("what is player ones name?: ")
p2name = input("what is player twos name?: ")
name = p1name
print(f"{p1name} will be x and {p2name} will be o.")

# starting board
board = [[1,2,3], [4,5,6], [7,8,9]]

def print_board():
    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(" - - - - ")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(" - - - - ")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")

print_board()

player_symbol = 'x'
player_turn = 1

def player_turn(name, symbol):
    turn = int(input(f"{name}, pick a number to place ur {symbol}: "))
    if turn == 1:
        board[0][0] = symbol
    elif turn == 2:
        board[0][1] = symbol
    elif turn == 3:
        board[0][2] = symbol
    elif turn == 4:
        board[1][0] = symbol
    elif turn == 5:
        board[1][1] = symbol
    elif turn == 6:
        board[1][2] = symbol
    elif turn == 7:
        board[2][0] = symbol
    elif turn == 8:
        board[2][1] = symbol
    elif turn == 9:
        board[2][2] = symbol 
    else:
        print("invalid number")

def check_for_win():
    global winner 
    #check 4 row win
    for row in range(len(board)):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            print(f"{name} has won")
            return True
    #check 4 collim win
    for column in range(len(board)):
        column_values = []
        for row in range(len(board)):
            column_values.append(board[row][column]) 
        if column_values[0] == column_values[1] and column_values[1] and column_values[1] == column_values[2]:
            return True
            
            
    #chec 4 digonal when
    if board[0][0] != '1':
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return True
turns = 0
winner = False
while turns < 9 and not winner:
    #playerturn
    player_turn(name, player_symbol)
    turns += 1
    

    if name == p1name:
        name = p2name
        player_symbol = 'o'
    else:
        name = p1name
        player_symbol = 'x'

    


    

#update board

    print_board()