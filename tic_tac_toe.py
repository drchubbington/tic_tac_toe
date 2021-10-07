import random
board = [
    ['-', '-', '-',],
    ['-', '-', '-',],
    ['-', '-', '-']
]

winner = None

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

def print_board():
    for j in range(3):
        print(board[j])

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
    return None

def end_game():
    global board
    if assess_board(board) == "p1":
        print("Player wins!")
        quit()
    elif assess_board(board) == "p2":
        print("AI wins!")
        quit()
    

class Node():
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, data):
        self.children.append(Node(data))

    def get_child(self, ind):
        return self.children[ind]

def postorder(root):
    if root:
        for child in root.children:
            postorder(child)
        print(root.data)

def minimax(root, alpha, beta, maximizing_player):
    if assess_board(root.data):
        #game is over, return static value
        return 0

    if maximizing_player:
        max_eval=-9999
        for child in root.children:
            maxEval = max(max_eval, minimax(child, alpha, beta, False))

    else:
        pass


#ai is oa
def ai_move():
    pass



while not winner:
    player_move()
    print_board()
    end_game()
    ai_move()
    end_game()
