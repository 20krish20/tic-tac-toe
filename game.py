class TicTacToe:
    def __init__(self):
        self.board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]
                    ]
        
    def check_win(self, board, current_player):
        win_scenarios = [
                [[0,0], [1,1], [2,2]],
                [[0,2], [1,1], [2,0]],
                [[0,0], [0,1], [0,2]],
                [[1,0], [1,1], [1,2]],
                [[2,0], [2,1], [2,2]],
                [[0,0], [1,0], [2,0]],
                [[0,1], [1,1], [2,1]],
                [[0,2], [1,2], [2,2]]
            ]

        for scen in win_scenarios:
            if board[scen[0][0]][scen[0][1]] == board[scen[1][0]][scen[1][1]] == board[scen[2][0]][scen[2][1]] == current_player:
                return f"Player {1 + current_player} WINS!!"


    
    def tic_tac_toe(self):
        current_player = 0

        for i in range(0, 9):

            while True:
                r, c = map(int, input("Row, Columns (0/1/2): ").split(","))
                if r not in [0,1,2] or c not in [0,1,2]:
                    print("Row and columns must be integers in 0,1,2. Fill again!")
                    continue
                elif self.board[r][c] is not None:
                    print("Place already filled, select a new place!")
                    continue
                break

            self.board[r][c] = current_player

            result = self.check_win(self.board, current_player)
            if result:
                return result

            current_player = 1 - current_player

        return "Draw!!"



if __name__ == "__main__":
    game = TicTacToe()
    print(game.tic_tac_toe())