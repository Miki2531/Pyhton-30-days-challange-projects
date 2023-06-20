import random


def display_board(board):
    print(('\n'*100))
    print('  |   |')
    print('' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('  |   |')
    print('------------')
    print('  |   |')
    print('' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('  |   |')
    print('------------')
    print('  |   |')
    print('' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('  |   |')


def play_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player1: Choose X or O: ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def check_won(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))


def choice_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# Indicating wheter space on the board freely available on.


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):

    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose postition (1-9):'))

    return position


def replay():
    choice = input("Play again? Enter Yes or No")

    return choice == 'Yes'


print('Welcome to tic tac toe game')

while True:
    the_board = [' ']*10
    palyer1_marker, player2_marker = play_input()
    turn = choice_first()
    print(turn + ' Will go first')

    play_game = input('Ready to paly? y or n')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            #  show the board
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,  palyer1_marker, position)

            if check_won(the_board, palyer1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!!')
                game = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!!!")
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,  player2_marker, position)

            if check_won(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!!')
                game = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!!!")
                    game_on = False
                else:
                    turn = 'Player 1'
    if not replay():
        break
