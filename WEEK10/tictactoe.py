"""
Tic-Tac-Toe Game Implementation
A console-based Tic-Tac-Toe game where a human player plays against a computer.

TicTacToe.main()                          # Entry point & orchestrator
├── new_board()                           # Initialize empty 3x3 board
├── get_o_or_x()                          # Get human symbol choice
├── other_player()                        # Switch between X/O symbols
├── play_game()                           # Main game loop
│   ├── display()                         # Show board state
│   ├── game_over()                       # Check win/draw conditions
│   │   ├── won_game()                    # Check victory patterns
│   │   └── empty_squares()               # Find available moves
│   ├── play_one_turn()                   # Execute single turn
│   │   ├── make_human_move()             # Handle human input
│   │   └── make_computer_move()          # AI strategy
│   │       ├── try_move() [nested]       # Test move helper
│   │       │   ├── empty_squares()       # Available positions
│   │       │   └── won_game()            # Victory check
│   │       ├── other_player()            # Get opponent symbol
│   │       └── empty_squares()           # Random move selection
│   └── other_player()                    # Switch players
└── print_result()                        # Display final outcome
"""

from random import Random
from typing import List, Tuple, Optional


class TicTacToe:
    """Tic-Tac-Toe game class that manages the game state and logic."""

    def __init__(self) -> None:
        """Initialize a new game instance."""
        self.board: List[List[str]] = []
        self.human_symbol: str = ""
        self.computer_symbol: str = ""

    def main(self) -> None:
        """Orchestrate game setup and execution."""
        self.board = self.new_board()
        self.human_symbol = self.get_o_or_x()
        self.computer_symbol = self.other_player(self.human_symbol)
        winner = self.play_game(self.board, self.human_symbol)
        self.print_result(winner)


    def new_board(self) -> List[List[str]]:
        """Create and return a new empty 3x3 Tic-Tac-Toe board."""
        return [[" " for _ in range(3)] for _ in range(3)]

    def get_o_or_x(self) -> str:
        """Prompt the human player to choose their symbol (X or O)."""
        while True:
            choice = input("Do you want to be X or O? ").strip().upper()
            if choice in ["X", "O"]:
                return choice
            print("Please enter X or O.")

    def play_game(self, board: List[List[str]], human: str) -> str:
        """Main game loop that alternates between players until the game is over."""
        current_player = "X"  # X always goes first

        self.display(board)

        while not self.game_over(board):
            self.play_one_turn(board, current_player, human)
            self.display(board)
            current_player = self.other_player(current_player)

        # Determine winner
        if self.won_game(board, "X"):
            return "X"
        return "O" if self.won_game(board, "O") else "DRAW"

    def print_result(self, winner: str) -> None:
        """Print the final game result."""
        if winner == "DRAW":
            print("It's a draw!")
        else:
            print(f"Player {winner} wins!")


    def display(self, board: List[List[str]]) -> None:
        """Display the current state of the board with row and column indices."""
        print("  0 1 2")
        for i in range(3):
            row_display = f"{i} {board[i][0]}|{board[i][1]}|{board[i][2]}"
            print(row_display)
            if i < 2:
                print("  -----")
        print()

    def play_one_turn(self, board: List[List[str]], current: str, human: str) -> None:
        """Execute one turn for the current player (human or computer)."""
        if current == human:
            self.make_human_move(board, current)
        else:
            self.make_computer_move(board, current)


    def make_human_move(self, board: List[List[str]], symbol: str) -> None:
        """Handle human player input and make their move."""
        while True:
            try:
                move_input = input("Enter your move (row col): ").strip()
                parts = move_input.split()

                if len(parts) != 2:
                    print("Please enter two numbers separated by a space.")
                    continue

                row, col = int(parts[0]), int(parts[1])

                if not (0 <= row <= 2 and 0 <= col <= 2):
                    print("Row and column must be between 0 and 2.")
                    continue

                if board[row][col] != " ":
                    print("That square is already occupied.")
                    continue

                board[row][col] = symbol
                break

            except ValueError:
                print("Please enter valid numbers.")


    def make_computer_move(self, board: List[List[str]], symbol: str,
                          rng: Optional[Random] = None) -> None:
        """Make a move for the computer using a strategic algorithm."""
        if rng is None:
            rng = Random(0)

        # Helper function to try a move
        def try_move(test_symbol: str) -> Optional[Tuple[int, int]]:
            for row, col in self.empty_squares(board):
                board[row][col] = test_symbol
                if self.won_game(board, test_symbol):
                    board[row][col] = " "  # Undo
                    return (row, col)
                board[row][col] = " "  # Undo
            return None

        # 1. Try to win
        if move := try_move(symbol):
            row, col = move
        # 2. Block opponent
        elif move := try_move(self.other_player(symbol)):
            row, col = move
        # 3. Take center
        elif board[1][1] == " ":
            row, col = 1, 1
        # 4. Take corner
        elif corners := [(r, c) for r, c in [(0,0), (0,2), (2,0), (2,2)] if board[r][c] == " "]:
            row, col = corners[0]
        # 5. Take any remaining square
        else:
            row, col = rng.choice(self.empty_squares(board))

        board[row][col] = symbol
        print(f"Computer chooses ({row}, {col})")

    def empty_squares(self, board: List[List[str]]) -> List[Tuple[int, int]]:
        """Return a list of coordinates for all empty squares on the board."""
        return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]


    def won_game(self, board: List[List[str]], symbol: str) -> bool:
        """Check if the specified symbol has won the game."""
        # Check rows and columns
        for i in range(3):
            if (all(board[i][j] == symbol for j in range(3)) or  # row
                all(board[j][i] == symbol for j in range(3))):   # column
                return True

        # Check diagonals
        return (all(board[i][i] == symbol for i in range(3)) or        # main diagonal
                all(board[i][2-i] == symbol for i in range(3)))        # anti-diagonal

    def game_over(self, board: List[List[str]]) -> bool:
        """Check if the game is over (someone won or board is full)."""
        return (self.won_game(board, "X") or self.won_game(board, "O") or
                len(self.empty_squares(board)) == 0)

    def other_player(self, s: str) -> str:
        """Return the opposite player symbol."""
        return "O" if s == "X" else "X"


# Simplified entry point
def main() -> None:
    """Orchestrate game setup and execution."""
    game = TicTacToe()
    game.main()


if __name__ == "__main__":
    main()
