class ConnectTwo:
    def __init__(self):
        self.board = [" " for _ in range(4)]
        self.player = "X"

    def valid_moves(self):
        return [i for i in range(4) if self.board[i] == " "]
    
    def make_move(self, move):
        self.board[move] = self.player
        self.player = "X" if self.player == "O" else "O"

    def is_game_over(self):
        for x1, x2 in zip(self.board, self.board[1:]):
            if x1 == x2 and x1 != " ":
                return True
        if self.is_full():
            return True
        return False
    
    def is_full(self):
        return all(cell != " " for cell in self.board)
    
    def check_winner(self):
        for x1, x2 in zip(self.board, self.board[1:]):
            if x1 == x2 and x1 != " ":
                return x1
        return None
        
    def play(self):
        while not self.is_game_over():
            print(self)
            move = int(input('Enter move: '))
            self.make_move(move)
        print(self)
        print(f'{self.check_winner()} wins!')

    def print_board(self):
        print('|'.join(self.board))

    def __str__(self):
        return '|'.join(self.board)
    
    def __repr__(self):
        return str(self)

if __name__ == '__main__':
    game = ConnectTwo()
    game.play()
