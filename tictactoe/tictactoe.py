global player1, player2

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

# test_board = ['#','A','e','X','O','X','O','X','O','X','a']
# display_board(test_board)

def player_input():
    global player1, player2
    player1 = input('Player1, please choose your symbol X or O: ')
    while player1.upper() != 'X' and player1.upper() != 'O':
        print('Invalid symbol!')
        player1 = input('Player1, please choose your symbol X or O: ')

    if player1.upper() == 'X':
        player1 = 'X'
        player2 = 'O'
    else:
        player1 = 'O'
        player2 = 'X'
    print('Player1 is {}, Player2 is {}'.format(player1, player2))


def place_marker(b, marker, position):
    if len(b) <= position:
        while len(b) <= position:
            b.append(' ')
        b.append(marker)
    else:
        b[position] = marker
    return b

def win_check(board, mark):
    index = 0
    indexSet = set([])
    for item in board:
        if item == mark:
            indexSet.add(index)
        index = index + 1
    for item in indexSet:
        if item == 1:
            return (2 in indexSet and 3 in indexSet) or \
                   (5 in indexSet and 9 in indexSet) or \
                   (4 in indexSet and 7 in indexSet)
        elif item == 2:
            return 5 in indexSet and 8 in indexSet
        elif item == 3:
            return (6 in indexSet and 9 in indexSet) or \
                   (5 in indexSet and 7 in indexSet)
        elif item == 4:
            return 6 in indexSet and 5 in indexSet
        elif item == 7:
            return 8 in indexSet and 9 in indexSet
        else:
            break
    return False

import random


def choose_first():
    if random.randint(0, 1) == 0:
        print('Player1 goes first using {}'.format(player1))
        return 'player1'
    else:
        print('Player2 goes first using {}'.format(player2))
        return 'player2'


def space_check(board, position):
    formatedBoard = format_board(board)
    return formatedBoard[position] == ' '


def full_board_check(board):
    formatedBoard = format_board(board)
    formatedBoard[0] = '#'
    for item in formatedBoard:
        if item == ' ':
            return False
    return True


def player_choice(board):
    index = 1
    availableSpace = []
    while index <= 9:
        if space_check(board, index):
            availableSpace.append(index)
        index = index + 1
    return availableSpace


def replay():
    choice = input('Do you want to replay? (Yes/No)')
    return choice[0].lower == 'y'


def place_token(board, token, p):
    avialablespots = player_choice(board)
    choice = input('{} can put your token {} in: {}'.format(p, token, avialablespots))
    # todo: check the input is valid
    b = place_marker(board, token, int(choice))
    b = display_board(b)
    return b


print('Welcome to Tic Tac Toe!')
isReplay = True
while isReplay:
    # Set the game up here
    player_input()
    print('The game is started!')
    game_on = True
    player = choose_first()
    board = display_board(['#'])

    while game_on:
        if player == 'player1':
            board = place_token(board, player1, player)
            if win_check(board, player1):
                print('Player1 win the game!')
                game_on = False
            else:
                if full_board_check(board):
                    game_on = False
                    print('Game tie')
                else:
                    player = 'player2'
        else:
            board = place_token(board, player2, player)
            if win_check(board, player2):
                print('Player2 win the game!')
                game_on = False
            else:
                if full_board_check(board):
                    game_on = False
                    print('Game tie')
                else:
                    player = 'player1'

    isReplay = replay()

print('Game is over, have a nice day')
