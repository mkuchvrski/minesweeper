import random
# play the game

class Board:
    def __init__(itself, dim_size, num_bombs):

        self.dim_size = dim_size
        self.num_bombs = num_bombs

        #let's create the board 

        self.board = self.make_new_board()
        self.assign_values_to_board()

        #initalize a set to keep track of which locations we've uncovered

        self.dug = set() #if we dig at 0, 0, then self.dug = {(0,0)}

    


    def make_new_board(self):
        # construct a new board based on the dim size and num bombs
        # we should construct the list of lists here (or whatever representation you prefer,
        # but since we have a 2-D board, list of lists is most natural)

        #generate a new board

        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        #plant the bombs

        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 -1)
            row = loc //self.dim_size 
            col = loc % self.dim_size

            if board[row][col] == '*':
                #this means we've actually planted a bomb there already so keep going
                continue

            board[row][col] = '*' #plant the bomb
            bombs_planted += 1
        
        return board

    def assign_values_to_board(self):

        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r,c)
    
    def get_num_neighboring_bombs(self, row, col):
        #finished here 1:37


def play(dim_size=10, num_bombs=10):
    #Step 1: create the board and plant the bombs
    #Step 2: show the user the board and ask for where they want to dig
    #Step 3a: if location is a bomb, show game over message
    #Step 3b: if location is not a bomb, fig recursively until each squeare is at least next to a bomb
    #Step 4: repeat steps 2 and 3a/b unitel there are no more places to fig -> VICTORY
    pass



