import random

# Global variables

winner = None
player = ' X '
board = [' - ' for x in range(9)]
win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                    [0, 3, 6], [1, 4, 7], [2, 5, 8],
                    [0, 4, 8], [2, 4, 6]]

semi_positions = [[0, 1, 2], [0, 2, 1], [1, 2, 0],
                  [3, 4, 5], [3, 5, 4], [4, 5, 3],
                  [6, 7, 8], [6, 8, 7], [7, 8, 6],
                  [0, 3, 6], [0, 6, 3], [3, 6, 0],
                  [1, 4, 7], [1, 7, 4], [4, 7, 1],
                  [2, 5, 8], [2, 8, 5], [5, 8, 2],
                  [0, 4, 8], [0, 8, 4], [4, 8, 0],
                  [2, 4, 6], [2, 6, 4], [4, 6, 2]]


# display the game board


def display_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])


# validate and play the turn of the current player

def play_a_turn():
    print(player + "'s turn")
    move = input("Where do you want to make a move? (1-9): ")

    while move not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Invalid input")
        move = input("Where do you want to make a move? (1-9): ")

    move = int(move) - 1

    while True:
        if board[move] == " X " or board[move] == " O ":
            print("invalid move, try again")
            print(player + "'s turn")
            move = input("Where do you want to make a move? (1-9): ")
            move = int(move) - 1
            continue
        else:
            board[move] = player
            break


# AI for the computer to play a turn

def computers_turn():
    possiblemoves = [iterat for iterat, mov in enumerate(board) if mov == ' - ']

    semis = []
    for i, h, r in semi_positions:
        if board[i] == ' O ' and board[h] == ' O ':
            if board[r] == ' - ':
                semis.append(r)
        elif board[i] == ' X ' and board[h] == ' X ':
            if board[r] == ' - ':
                semis.append(r)
    if len(semis) > 0:
        move = semis[(random.randrange(len(semis)))]
        board[move] = player

    else:

        corner_moves = []
        for i in possiblemoves:
            if i in [0, 2, 6, 8]:
                corner_moves.append(i)
        if len(corner_moves) > 0:
            move = corner_moves[(random.randrange(len(corner_moves)))]
            board[move] = player
        else:
            edge_moves = []
            for i in possiblemoves:
                if i in [1, 3, 5, 7]:
                    edge_moves.append(i)
            if len(edge_moves) > 0:
                move = edge_moves[(random.randrange(len(edge_moves)))]
                board[move] = player


# change the player


def change_player():
    global player
    if player == " X ":
        player = " O "
    elif player == " O ":
        player = " X "


# check if there is a winner or a tie

def check_for_win():
    global winner

    for i, h, r in win_combinations:
        if board[i] == board[h] == board[r] != " - ":
            winner = board[i]

    if winner == " X " or winner == " O ":
        display_board()
        print(winner + "won!")
        stop_game()
    else:
        check_for_tie()


def check_for_tie():
    global winner
    if ' - ' not in board:
        winner = " "
        display_board()
        print("it's a tie")
        stop_game()


def stop_game():
    global winner, player
    while True:
        playagain = input("Play again? (y/n) ")
        if playagain.lower() == "y":
            for i in range(len(board)):
                board[i] = ' - '
            break
        elif playagain.lower() == "n":
            exit()
        elif playagain not in ("y", "n"):
            continue
    winner = None
    player = ' X '
    play_the_game()


# run the entire game


def play_the_game():
    global winner
    players_1or2 = input("1 Player or 2 Players? (1/2) ")
    while players_1or2 not in ("1", "2"):
        players_1or2 = input("try again")
    while winner is None:
        display_board()
        play_a_turn()
        check_for_win()
        change_player()
        if int(players_1or2) == 1:
            computers_turn()
            check_for_win()
            change_player()


play_the_game()
