import copy

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def display_board(self):
        for row in self.board:
            print("|".join(row))
            print("-----")
        print()

    def game_over(self):
        return self.is_winner('X') or self.is_winner('O') or self.is_board_full()

    def is_board_full(self):
        return all(all(cell != ' ' for cell in row) for row in self.board)

    def make_move(self, move):
        row, col = move
        self.board[row][col] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def available_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']

    def is_winner(self, player):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):  # Check rows
                return True
            if all(self.board[j][i] == player for j in range(3)):  # Check columns
                return True
        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def minimax(self, depth, maximizing_player):
        if self.is_winner('X'):
            return -10 + depth, None
        elif self.is_winner('O'):
            return 10 - depth, None
        elif self.is_board_full():
            return 0, None

        if maximizing_player:
            max_eval = float('-inf')
            best_move = None
            for move in self.available_moves():
                self.make_move(move)
                eval, _ = self.minimax(depth - 1, False)
                self.board[move[0]][move[1]] = ' '  # Undo the move
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in self.available_moves():
                self.make_move(move)
                eval, _ = self.minimax(depth - 1, True)
                self.board[move[0]][move[1]] = ' '  # Undo the move
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
            return min_eval, best_move

if __name__ == "__main__":
    game = TicTacToe()

    while not game.game_over():
        game.display_board()

        if game.current_player == 'X':
            while True:
                try:
                    move_input = int(input("Player X, enter your move (1-9): "))
                    move = (move_input - 1) // 3, (move_input - 1) % 3
                    if 0 <= move[0] < 3 and 0 <= move[1] < 3 and game.board[move[0]][move[1]] == ' ':
                        game.make_move(move)
                        break  # Exit the input loop if a valid move is made
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 9.")
        else:  # AI's turn
            eval, best_move = game.minimax(depth=3, maximizing_player=True)  # Example depth
            game.make_move(best_move)

    game.display_board()  # Display the final board
    if game.is_winner('X'):
        print("Player X wins!")
    elif game.is_winner('O'):
        print("Computer wins!")
    else:
        print("It's a tie!")
