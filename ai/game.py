class Board:

    player_1 = "X"
    player_2 = "O"

    def __init__(self):
        self.board = [str(i) for i in range(9)]
    
    def move(self, idx, player):
        if self.board[idx].isdigit():
            self.board[idx] = player
        else:
            print(f"This block is occupied. ")
    
    def undo(self, idx):
        if not self.board[idx].isdigit():
            self.board[idx] = str(idx)
    
    def check(self):
        win_conditions = [
            (0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)
        ]
        for a,b,c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] and not self.board[a].isdigit():
                return self.board[a]
        return None
    
    def get_available_moves(self):
        return [x for x in range(len(self.board)) if self.board[x].isdigit()]
    
    def print(self):
        for i in range(0,9,3):
            print(f"{self.board[i]}|{self.board[i+1]}|{self.board[i+2]}")
            if i<6:
                print("---+---+---")
    