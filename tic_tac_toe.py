board = [
    ['-', '-', '-',],
    ['-', '-', '-',],
    ['-', '-', '-']
]
global stored_ai_move
stored_ai_move = None

#player is 'x'
#asks the player for a row and column, then plays a piece there if valid
def player_move(board):
    row = int(input("Enter a row (1-3): "))-1
    col = int(input("Enter a column (1-3): "))-1
    if board[row][col] == "-":
        board[row][col] = "x"
    else:
        print("Someone has already gone there!")
        player_move()

#prints the board array passed as a parameter
def print_board(board):
    for j in range(3):
        print(board[j])
    print()

#returns the winner of the passed board as a string, or None if not a winning state
#NOTE: this method doesn't end the game—it just returns the winner
def assess_board(board):
    #checking for rows
    for i in range(3):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][0]=="x":
            return "p1"
        elif board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][0]=="o":
            return "p2"
    #checking for columns
    for i in range(3): 
        if board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[0][i]=="x":
            return "p1"
        elif board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[0][i]=="o":
            return "p2"
    #checking tl-br diagonal
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0]=="x":
        return "p1"
    elif board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0]=="o":
        return "p2"
    #checkng tr-bl diagonal
    elif board[2][0]==board[1][1] and board[1][1]==board[0][2] and board[2][0]=="x":
        return "p1"
    elif board[2][0]==board[1][1] and board[1][1]==board[0][2] and board[2][0]=="o":
        return "p2"
    #if the board is full and not a winning state, it's a tie
    if not find_empty_spaces(board):
        return "tie"
    #otherwise, the game would continue from this state
    return None

#returns a list of the indices in the passed board that are "empty" (represented by "-")
def find_empty_spaces(board):
    spaces = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "-":
                spaces.append([row, col])
    return spaces

#adds a move to the passed board and returns it
def add_move(board, move, maximizing_player):
    board[move[0]][move[1]] = "o" if maximizing_player else "x"
    return board

#solves the complete game, assuming best play from the opponent
#ai is 'o' and maximizes. player is 'x' and minimizes.
#alpha stores the best move for the maximizer (the ai), whereas beta stores the best move for the minimizer (the player)
#maximizing_player determines whether we are trying to maximize or minimize in the current iteration. Alternates between layers of the tree
#is_starter is only true if it's the first call of the algorithm (using the present game board state)
def minimax(board, alpha, beta, maximizing_player, is_starter):
    #if game is over, return static evaluation
    state=assess_board(board)
    if state == "p1":
        return -1
    elif state == "p2":
        return 1
    elif state == "tie":
        return 0
    
    global stored_ai_move

    #go down the tree until a game-ending state, then pass the best move up the tree by returning it
    if maximizing_player:
        max_eval=-2
        for move in find_empty_spaces(board):
            #use recursion to go down the tree. Note that maximizing_player=False, so we will minimize next iteration.
            eval = minimax(add_move([board[0][:],board[1][:],board[2][:]], move, True), alpha, beta, False, False)
            #if we're evaluating the original board and we find a good move, we update it here
            if is_starter and eval>max_eval:
                stored_ai_move = move
            max_eval=max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta<=alpha:
                #true if there was a better move earlier in the tree. This means we can clip.
                break
        return max_eval
    else:
        min_eval=2
        for move in find_empty_spaces(board):
            #use recursion to go down the tree. Note that maximizing_player=True, so we will maximize next iteration.
            eval = minimax(add_move([board[0][:],board[1][:],board[2][:]], move, False), alpha, beta, True, False)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta<=alpha:
                #true if there was a better move earlier in the tree. This means we can clip.
                break
        return min_eval

#ai is 'o'
#runs minimax() and plays the ai's best move onto the game board
def ai_move(board):
    global stored_ai_move
    minimax(board, -2, 2, True, True)
    move = stored_ai_move
    board[move[0]][move[1]] = "o"

#if the game board is in a winning state, end the game and terminate
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

#to see the AI going both first and second, the player can choose whether to go first
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
