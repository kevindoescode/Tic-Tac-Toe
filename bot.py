import random
def bot_move(board, player_symbol, difficulty):
    if difficulty == 0:
        if player_symbol == 0:
            bot_symbol = 1
        else:
            bot_symbol = 1
        board_values = list(board.keys())
        random.shuffle(board_values)
        for i in board_values:
            if board[i] == None:
                board[i] = bot_symbol
                break

    return board
