import json

global player1, player2, board

def entrypoint(event, context):
    board = []
    player1 = event.symbol
      if player1.upper() == 'X':
        player1 = 'X'
        player2 = 'O'
    else:
        player1 = 'O'
        player2 = 'X'
    return {
        "statusCode": 200,
        "body": json.dumps('Player1 is {}, Player2 is {}'.format(player1, player2))
    }
