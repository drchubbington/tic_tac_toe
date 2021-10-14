import random
board = [
    ['-', '-', '-',],
    ['-', '-', '-',],
    ['-', '-', '-']
]
global stored_ai_move
stored_ai_move = None
winner = None

#player is 'x'
def player_move(board):
    row = int(input("Enter a row (1-3): "))-1
    col = int(input("Enter a column (1-3): "))-1
    if board[row][col] == "-":
        board[row][col] = "x"
    else:
        print("Someone has already gone there!")
        player_move()

def print_board(board):
    for j in range(3):
        print(board[j])
    print()

def assess_board(board):
    global winner
    for i in range(3):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][0]=="x":
            return "p1"
        elif board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][0]=="o":
            return "p2"
    if not winner:
        for i in range(3): 
            if board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[0][i]=="x":
                return "p1"
            elif board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[0][i]=="o":
                return "p2"
    if not winner:
        if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0]=="x":
            return "p1"
        elif board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0]=="o":
            return "p2"
        elif board[2][0]==board[1][1] and board[1][1]==board[0][2] and board[2][0]=="x":
            return "p1"
        elif board[2][0]==board[1][1] and board[1][1]==board[0][2] and board[2][0]=="o":
            return "p2"
    if not find_empty_spaces(board):
        return "tie"
    return None

def find_empty_spaces(board):
    spaces = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "-":
                spaces.append([row, col])
    return spaces

def add_move(board, move, maximizing_player):
    board[move[0]][move[1]] = "o" if maximizing_player else "x"
    return board

def minimax(board, alpha, beta, maximizing_player, is_starter):
    state=assess_board(board)
    if state == "p1":
        return -1
    elif state == "p2":
        return 1
    elif state == "tie":
        return 0
    
    global stored_ai_move
    if maximizing_player:
        max_eval=-2
        for move in find_empty_spaces(board):
            eval = minimax(add_move([board[0][:],board[1][:],board[2][:]], move, True), alpha, beta, False, False)
            if is_starter and eval>max_eval:
                stored_ai_move = move
            max_eval=max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta<=alpha:
                break
        return max_eval
    else:
        min_eval=2
        for move in find_empty_spaces(board):
            eval = minimax(add_move([board[0][:],board[1][:],board[2][:]], move, False), alpha, beta, True, False)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta<=alpha:
                break
        return min_eval

#ai is 'o'
def ai_move(board):
    global stored_ai_move
    minimax(board, -2, 2, True, True)
    move = stored_ai_move
    board[move[0]][move[1]] = "o"

def end_game():
    global board
    if assess_board(board) == "p1":
        print("Player wins!")
        quit()
    elif assess_board(board) == "p2":
        print("AI wins!")
        quit()
    elif assess_board(board) == "tie":
        print("It's a tie!")
        quit()
answer = input("Would you like to go first?").lower()
print_board(board)
if answer=="y" or answer=="yes":
    while True:
        player_move(board)
        print_board(board)
        end_game()

        ai_move(board)
        print_board(board)
        end_game()
else:
    while True:
        ai_move(board)
        print_board(board)
        end_game()

        player_move(board)
        print_board(board)
        end_game()
