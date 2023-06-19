def display_board(board):

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


test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
# print(display_board(test_board))


def pass_marker():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player1: Choose X or O: ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


pl1, pl2 = pass_marker()
print(pl1, pl2)


def place_marker(board, marker, position):
    board[position] = marker


place_marker(test_board, '&', 7)
print(display_board(test_board))


def check_won(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))


print(check_won(test_board, 'X'))
