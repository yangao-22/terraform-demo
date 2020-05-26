import json
import responseObj

global player1, player2, board

def entrypoint(event, context):
    if event["type"] == "symbol":
        set_symbol(event["symbol"] )

def set_symbol(symbol):
    player1 = symbol
    if player1.upper() == 'X':
        player1 = 'X'
        player2 = 'O'
    else:
        player1 = 'O'
        player2 = 'X'

    response = responseObj.responseBody(player1, player2, [])
    return {
        "statusCode": 200,
        "body": response.__dict__
    } 