import random
board = [
    ['-', '-', '-',],
    ['-', '-', '-',],
    ['-', '-', '-']
]
game_is_won = False

#player is x
def player_move():
    print_board()
    row = int(input("Enter a row (1-3): "))-1
    col = int(input("Enter a column (1-3): "))-1
    if board[row][col] == "-":
         board[row][col] = "x"
    else:
        print("Someone has already gone there!")
        player_move()

#ai is o
def ai_move():
    print("not yet")

def print_board():
    for j in range(3):
        print(board[j])


def assess_board(game_is_won):
    for i in range(3):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][0]=="x":
            print("Player wins!")
            game_is_won = True
        elif board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][0]=="o":
            print("AI wins!")
            game_is_won = True
    if not game_is_won:
        for i in range(3): 
            if board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[0][i]=="x":
                print("Player wins!")
                game_is_won = True
            elif board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[0][i]=="o":
                print("AI wins!")
                game_is_won = True

    if not game_is_won:
        if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0]=="x":
            print("Player wins!")
            game_is_won = True
        elif board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0]=="o":
            print("AI wins!")
            game_is_won = True
        elif board[2][0]==board[1][1] and board[1][1]==board[0][2] and board[2][0]=="x":
            print("Player wins!")
            game_is_won = True
            print("hi")
        elif board[2][0]==board[1][1] and board[1][1]==board[0][2] and board[2][0]=="o":
            print("AI wins!")
            game_is_won = True
    if game_is_won:
        quit()
    
while not game_is_won:
    player_move()
    print_board()
    assess_board(game_is_won)
    ai_move()
    assess_board(game_is_won)



