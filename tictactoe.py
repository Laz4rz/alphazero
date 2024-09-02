class TicTacToe:
    def __init__(self):
        self.empty_str = " "
        self.board = [[self.empty_str for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        print('|'.join(self.board[0]))
        for row in self.board[1:]:
            print('-' * 5 * len(self.empty_str))
            print('|'.join(row))

    def make_move(self, row, col):
        if self.board[row][col] == self.empty_str:
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print('Invalid move')        
    
    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != self.empty_str:
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != self.empty_str:
                return self.board[0][i]
            
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != self.empty_str:
            return self.board[0][0]
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != self.empty_str:
            return self.board[0][2]
        
        return None
    
    def is_full(self):
        for row in self.board:
            for cell in row:
                if cell == self.empty_str:
                    return False
        return True
    
    def is_game_over(self):
        return self.check_winner() or self.is_full()
    
    def play(self):
        while not self.is_game_over():
            self.print_board()
            row = int(input('Enter row: '))
            col = int(input('Enter col: '))
            self.make_move(row, col)
        
        self.print_board()
        winner = self.check_winner()
        if winner:
            print(f'{winner} wins!')
        else:
            print('It\'s a tie!')

    def valid_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == self.empty_str]
    
    def make_move_api(self, row, col):
        if self.board[row][col] == self.empty_str:
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            raise ValueError('Invalid move') 

if __name__ == '__main__':
    game = TicTacToe()
    game.play()