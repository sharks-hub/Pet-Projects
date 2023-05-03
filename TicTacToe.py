import random

# Define the board as a list of squares
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Define the winning combinations
winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

# Define the player symbols and who goes first
player_symbol = ""
computer_symbol = ""
player_turn = False

# Define a function to draw the board
def draw_board():
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")

# Define a function to check for a winner
def check_winner():
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]]:
            return board[combination[0]]
    return ""

# Define a function to get the player's move
def get_player_move():
    while True:
        try:
            move = int(input("Enter the number of the square you want to place your tile: "))
            if move < 1 or move > 9:
                print("Invalid square, please try again.")
            elif board[move-1] in ["X", "O"]:
                print("This square is already taken, please try again.")
            else:
                return move-1
        except ValueError:
            print("Invalid input, please try again.")

# Define a function to get the computer's move
def get_computer_move():
    available_squares = [i for i in range(9) if board[i] not in ["X", "O"]]
    return random.choice(available_squares)

# Define the main game loop
def play_game():
    global player_turn
    global player_symbol
    global computer_symbol

    # Prompt the player to choose a side
    print("Welcome to Tic Tac Toe!")
    while player_symbol not in ["X", "O"]:
        player_symbol = input("Choose your side (X/O): ").upper()

    # Determine who goes first by flipping a coin
    coin = random.randint(0, 1)
    if coin == 0:
        print("You go first!")
        player_turn = True
    else:
        print("The computer goes first.")
        player_turn = False

    # Assign symbols to the player and the computer
    if player_symbol == "X":
        computer_symbol = "O"
    else:
        computer_symbol = "X"

    # Draw the initial board
    draw_board()

    # Start the game loop
    while True:
        # Get the player's move
        if player_turn:
            print("Your turn.")
            move = get_player_move()
            board[move] = player_symbol
        # Get the computer's move
        else:
            print("The computer's turn.")
            move = get_computer_move()
            board[move] = computer_symbol
        # Draw the updated board
        draw_board()

        # Check for a winner or a tie
        winner = check_winner()
        if winner != "":
            if winner == player_symbol:
                print("Congratulations, you won!")
            else:
                print("Sorry, you lost.")
            break
        elif all(square in ["X", "O"] for square in board):
            print("Tie game.")
            break

        # Switch turns
        player_turn = not player_turn

    print("Game over.")

# Start the game
play_game()
