import json

class responseBody(object):
    def __init__(self, player1, player2, board):
        self.board = board
        self.player1 = player1
        self.player2 = player2