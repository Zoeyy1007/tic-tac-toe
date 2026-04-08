import game

def minimax(board, currPlayer, depth):
    available_moves = board.get_available_moves()

    # score check 
    if board.check() == "X":
        return (10-depth, None)
    elif board.check() == "O":
        return (-10+depth, None)
    if not board.get_available_moves():
        return (0, None)

    best_move = None
    
    if currPlayer == "X":
        next_player = "O"
        best_score = float('-inf')
        for idx in available_moves:
            board.move(idx, currPlayer)
            score, _ = minimax(board, next_player, depth+1)
            board.undo(idx)
            if score > best_score:
                best_score = score
                best_move = idx
        return (best_score, idx)
    else:
        next_player = "X"
        best_score = float('inf')
        for idx in available_moves:
            board.move(idx, currPlayer)
            score, _ = minimax(board, next_player, depth+1)
            board.undo(idx)
            if score < best_score:
                best_score = score
                best_move = idx
        return (best_score, best_move)


# player_1 = "X"
# player_2 = "O"
# player_1 goal state is 10
# player_2 goal state is -10