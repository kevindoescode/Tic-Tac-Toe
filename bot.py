import random
def bot_move(board, player_symbol, difficulty):
    if player_symbol == 0:
        bot_symbol = 1
    else:
        bot_symbol = 0
    if difficulty == 0:
        board_values = list(board.keys())
        random.shuffle(board_values)
        for i in board_values:
            if board[i] == None:
                board[i] = bot_symbol
                break
    if difficulty == 1:
        move_executed = False
        board_positions = []
        board_keys = list(board.keys())
        board_values = list(board.values())
        for i in range(9):
            if board_values[i] == bot_symbol:
                position_yes = True
            elif board_values[i] == player_symbol:
                position_yes = False
            else:
                position_yes = None
            board_positions.append(position_yes)
        if True:
            move_possible = 0
            move_impossible = False
            for i in range(0,3):
                if board_positions[i] == True:
                    move_possible += 1
                if board_positions[i] == False:
                    move_impossible = True
            if move_possible == 2 and move_impossible == False:
                for i in range(0,3):
                    if board_values[i] == None:
                        board[board_keys[i]] = bot_symbol
                        move_executed = True
        if True:
            move_possible = 0
            move_impossible = False
            for i in range(3,6):
                if board_positions[i] == True:
                    move_possible += 1
                if board_positions[i] == False:
                    move_impossible = True
            if move_possible == 2 and move_impossible == False:
                for i in range(3,6):
                    if board_values[i] == None:
                        board[board_keys[i]] = bot_symbol
                        move_executed = True
        if True:
            move_possible = 0
            move_impossible = False
            for i in range(6,9):
                if board_positions[i] == True:
                    move_possible += 1
                if board_positions[i] == False:
                    move_impossible = True
            if move_possible == 2 and move_impossible == False:
                for i in range(6,9):
                    if board_values[i] == None:
                        board[board_keys[i]] = bot_symbol
                        move_executed = True
        if True:
            move_possible = 0
            move_impossible = False
            for i in [0,3,6]:
                if board_positions[i] == True:
                    move_possible += 1
                if board_positions[i] == False:
                    move_impossible = True
            if move_possible == 2 and move_impossible == False:
                for i in [0,3,6]:
                    if board_values[i] == None:
                        board[board_keys[i]] = bot_symbol
                        move_executed = True
        if True:
            move_possible = 0
            move_impossible = False
            for i in [1,4,7]:
                if board_positions[i] == True:
                    move_possible += 1
                if board_positions[i] == False:
                    move_impossible = True
            if move_possible == 2 and move_impossible == False:
                for i in [1,4,7]:
                    if board_values[i] == None:
                        board[board_keys[i]] = bot_symbol
                        move_executed = True
        if True:
            move_possible = 0
            move_impossible = False
            for i in [2,6,8]:
                if board_positions[i] == True:
                    move_possible += 1
                if board_positions[i] == False:
                    move_impossible = True
            if move_possible == 2 and move_impossible == False:
                for i in [2,6,8]:
                    if board_values[i] == None:
                        board[board_keys[i]] = bot_symbol
                        move_executed = True
        if True:
            move_possible = 0
            move_impossible = False
            for i in [0,4,8]:
                if board_positions[i] == True:
                    move_possible += 1
                if board_positions[i] == False:
                    move_impossible = True
            if move_possible == 2 and move_impossible == False:
                for i in [0,4,8]:
                    if board_values[i] == None:
                        board[board_keys[i]] = bot_symbol
                        move_executed = True
        if True:
            move_possible = 0
            move_impossible = False
            for i in [2,4,6]:
                if board_positions[i] == True:
                    move_possible += 1
                if board_positions[i] == False:
                    move_impossible = True
            if move_possible == 2 and move_impossible == False:
                for i in [2,4,6]:
                    if board_values[i] == None:
                        board[board_keys[i]] = bot_symbol
                        move_executed = True

        if move_executed == False:
            random.shuffle(board_keys)
            for i in board_keys:
                if board[i] == None:
                    board[i] = bot_symbol
                    break
    return board
