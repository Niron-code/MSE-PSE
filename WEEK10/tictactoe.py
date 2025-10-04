"""
Tic-Tac-Toe Game Implementation
A console-based Tic-Tac-Toe game where a human player plays against a computer.

TicTacToe.main()
├── new_board()                    # Initialize empty 3x3 board
├── get_o_or_x()                   # Get human symbol choice
├── play_game()                    # Main game loop
│   ├── display()                  # Show board state
│   ├── game_over()                # Check win/draw conditions
│   │   └── won_game()             # Check victory patterns
│   │       └── empty_squares()    # Find available moves
│   ├── play_one_turn()            # Execute single turn
│   │   ├── make_human_move()      # Handle human input
│   │   └── make_computer_move()   # AI strategy
│   │       ├── empty_squares()    # Available positions
│   │       └── random_in_range()  # Random selection
│   └── other_player()             # Switch between X/O
└── print_result()                 # Display final outcome
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

            if self.game_over(board):
                break

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

                if row < 0 or row > 2 or col < 0 or col > 2:
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

        opponent = self.other_player(symbol)

        # 1. Check for winning move
        for row, col in self.empty_squares(board):
            board[row][col] = symbol
            if self.won_game(board, symbol):
                print(f"Computer chooses ({row}, {col})")
                return
            board[row][col] = " "  # Undo move

        # 2. Block opponent's winning move
        for row, col in self.empty_squares(board):
            board[row][col] = opponent
            if self.won_game(board, opponent):
                board[row][col] = symbol
                print(f"Computer chooses ({row}, {col})")
                return
            board[row][col] = " "  # Undo move

        # 3. Take center if available
        if board[1][1] == " ":
            board[1][1] = symbol
            print("Computer chooses (1, 1)")
            return

        # 4. Take a corner if available
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        if available_corners := [(r, c) for r, c in corners if board[r][c] == " "]:
            row, col = available_corners[0]
            board[row][col] = symbol
            print(f"Computer chooses ({row}, {col})")
            return

        # 5. Take any remaining square randomly
        if empties := self.empty_squares(board):
            index = self.random_in_range(rng, 0, len(empties) - 1)
            row, col = empties[index]
            board[row][col] = symbol
            print(f"Computer chooses ({row}, {col})")


    def empty_squares(self, board: List[List[str]]) -> List[Tuple[int, int]]:
        """Return a list of coordinates for all empty squares on the board."""
        return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]

    def random_in_range(self, rng: Random, start: int, end: int) -> int:
        """Generate a random integer in the inclusive range [start, end]."""
        return rng.randint(start, end)


    def won_game(self, board: List[List[str]], symbol: str) -> bool:
        """Check if the specified symbol has won the game."""
        # Check rows
        for row in range(3):
            if all(board[row][col] == symbol for col in range(3)):
                return True

        # Check columns
        for col in range(3):
            if all(board[row][col] == symbol for row in range(3)):
                return True

        # Check diagonals
        # Main diagonal (top-left to bottom-right)
        if all(board[i][i] == symbol for i in range(3)):
            return True

        # Anti-diagonal (top-right to bottom-left)
        return all((board[i][2-i] == symbol for i in range(3)))

    def game_over(self, board: List[List[str]]) -> bool:
        """Check if the game is over (someone won or board is full)."""
        return (self.won_game(board, "X") or self.won_game(board, "O") or
                len(self.empty_squares(board)) == 0)

    def other_player(self, s: str) -> str:
        """Return the opposite player symbol."""
        return "O" if s == "X" else "X"


# Module-level functions to maintain the original interface
def main() -> None:
    """Orchestrate game setup and execution."""
    game = TicTacToe()
    game.main()


def new_board() -> List[List[str]]:
    """Create and return a new empty 3x3 Tic-Tac-Toe board."""
    game = TicTacToe()
    return game.new_board()


def get_o_or_x() -> str:
    """Prompt the human player to choose their symbol (X or O)."""
    game = TicTacToe()
    return game.get_o_or_x()


def play_game(board: List[List[str]], human: str) -> str:
    """Main game loop that alternates between players until the game is over."""
    game = TicTacToe()
    return game.play_game(board, human)


def print_result(winner: str) -> None:
    """Print the final game result."""
    game = TicTacToe()
    game.print_result(winner)


def display(board: List[List[str]]) -> None:
    """Display the current state of the board with row and column indices."""
    game = TicTacToe()
    game.display(board)


def play_one_turn(board: List[List[str]], current: str, human: str) -> None:
    """Execute one turn for the current player (human or computer)."""
    game = TicTacToe()
    game.play_one_turn(board, current, human)


def make_human_move(board: List[List[str]], symbol: str) -> None:
    """Handle human player input and make their move."""
    game = TicTacToe()
    game.make_human_move(board, symbol)


def make_computer_move(board: List[List[str]], symbol: str,
                      rng: Optional[Random] = None) -> None:
    """Make a move for the computer using a strategic algorithm."""
    game = TicTacToe()
    game.make_computer_move(board, symbol, rng)


def empty_squares(board: List[List[str]]) -> List[Tuple[int, int]]:
    """Return a list of coordinates for all empty squares on the board."""
    game = TicTacToe()
    return game.empty_squares(board)


def random_in_range(rng: Random, start: int, end: int) -> int:
    """Generate a random integer in the inclusive range [start, end]."""
    game = TicTacToe()
    return game.random_in_range(rng, start, end)


def won_game(board: List[List[str]], symbol: str) -> bool:
    """Check if the specified symbol has won the game."""
    game = TicTacToe()
    return game.won_game(board, symbol)


def game_over(board: List[List[str]]) -> bool:
    """Check if the game is over (someone won or board is full)."""
    game = TicTacToe()
    return game.game_over(board)


def other_player(s: str) -> str:
    """Return the opposite player symbol."""
    game = TicTacToe()
    return game.other_player(s)


if __name__ == "__main__":
    main()
