#!/usr/bin/python3

"""
Tic-Tac-Toe Game

Two players take turns placing 'X' and 'O' on a 3x3 board. The first player to get
three in a row (horizontally, vertically, or diagonally) wins. If the board is
full and no player has three in a row, the game ends in a tie.
"""

def print_board(board):
    """
    Prints the current state of the Tic-Tac-Toe board.

    Parameters:
        board (list of list of str): The 3x3 game board.

    Behavior:
        Displays the board with 'X', 'O', or blank spaces.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)  # Separator for better readability

def check_winner(board):
    """
    Checks if there is a winner on the board.

    Parameters:
        board (list of list of str): The 3x3 game board.

    Returns:
        bool: True if a player has won, False otherwise.

    Behavior:
        Checks all rows, columns, and both diagonals for three identical non-blank symbols.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """
    Runs the main game loop for Tic-Tac-Toe.

    Behavior:
        Initializes an empty 3x3 board.
        Alternates turns between player 'X' and player 'O'.
        Prompts users for valid row and column input.
        Updates the board with each move.
        Checks for a winner or tie after each move.
        Ends the game with a message announcing the winner or tie.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Input validation loop
        while True:
            try:
                row = int(input(f"Enter row (0-2) for player {player}: "))
                col = int(input(f"Enter column (0-2) for player {player}: "))
                if row not in range(3) or col not in range(3):
                    print("Invalid input! Row and column must be 0, 1, or 2.")
                elif board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter integers only.")

        board[row][col] = player

        # Check for winner
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

        # Check for tie
        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("It's a tie!")
            break

# Run the game
tic_tac_toe()
