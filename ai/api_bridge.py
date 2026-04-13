import sys
import json
from minimax import minimax
from game import Board

input_data = json.loads(sys.argv[1])

python_board = [str(i) if val is None else val for i, val in enumerate(input_data)]

temp_board = Board()
temp_board.board = python_board

score, move = minimax(temp_board, "O", 0)

print(move)