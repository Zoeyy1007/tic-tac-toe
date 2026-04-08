import minimax
import game

def main():
    my_board = game.Board()
    print(f"You are X, the computer is playing O")
    while my_board.get_available_moves():
        my_board.print()
        user_move = int(input("Now is your move. "))

        if my_board.check():
            break

        my_board.move(user_move,"X")
        ai_score, ai_move = minimax.minimax(my_board, "O", 0)
        my_board.move(ai_move, "O")
        print(f"After AI move, current board is: ")
        my_board.print()

        if my_board.check():
            break

main()