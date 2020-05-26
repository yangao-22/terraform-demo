
def format_board(rawboard):
    newboard = []
    for item in rawboard:
        if item == 'X' or item == 'O':
            newboard.append(item)
        else:
            newboard.append(' ')

    while len(newboard) < 10:
        newboard.append(' ')
    newboard[0] = '#'
    return newboard

def display_board(board):
    newboard = format_board(board)

    print(' {} | {} | {} '.format(newboard[9], newboard[8], newboard[7]))
    print('--------------')
    print(' {} | {} | {} '.format(newboard[6], newboard[5], newboard[4]))
    print('--------------')
    print(' {} | {} | {} '.format(newboard[3], newboard[2], newboard[1]))
    return newboard

def json_board(board):
    str = ' {} | {} | {} \n'.format(board[9], board[8], board[7])
    str += '-------------- \n'
    str += ' {} | {} | {} \n'.format(board[6], board[5], board[4])
    str += '--------------\n'
    str += ' {} | {} | {} \n'.format(board[3], board[2], board[1])
    return str