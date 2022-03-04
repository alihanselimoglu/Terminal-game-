import os
import sys
import platform
import time
game_size = [14, 7]
"""
┌───┬───┬───┐
│ X │ X │ X │
├───┼───┼───┤
│ X │ X │ X │
├───┼───┼───┤
│ X │ X │ X │
└───┴───┴───┘

"""
box_drawings = [
    "┌───┬───┬───┐",
    "├───┼───┼───┤",
    "└───┴───┴───┘",
]


def clean():
    clean_command = "clear" if platform.system() == "Linux" else "cls"
    os.system(clean_command)

def getSize():
    return os.get_terminal_size()

def startingPoint(size):
    x = int((size.columns - game_size[0]) / 2)
    y = int((size.lines - game_size[1]) / 2)
    #print(size.lines, y)
    return [x, y]


def drawBoard(board, offset):
    for _ in range(offset[1]):
        print(" ")

    
    for i in range(game_size[1]):
        print(" "*offset[0], sep="", end="")
        if i == 0:
            print(box_drawings[0])
        elif i in [2, 4]:
            print(box_drawings[1])
        elif i == 6:
            print(box_drawings[2])

        else:

            n = int(1.5*i - 1.5)
            theLine = f"│ {board[n]} │ {board[n+1]} │ {board[n+2]} │"
            print(theLine)


    for _ in range(offset[1]):
        print(" ")

def is_winning(board):

    for i in range(0, 9, 3):
        if board[i] == board[i+1] and board[i+1] == board[i+2] and board[i] != " ":
            return board[i]

    for i in range(3):
        if board[i] == board[i+3] and board[i+3] == board[i+6] and board[i] != " ":
            return board[i]

    if board[0] == board[4] and board[4] == board[8] and board[4] != " ":
        return board[4]

    if board[2] == board[4] and board[4] == board[6] and board[4] != " ":
        return board[4]

    return False

def main():
    #clean()
    size = getSize()
    board = [" " for i in range(9)]
    drawBoard(board, startingPoint(size))
    #drawBoard(board, startingPoint(size))
    current_user = ["X", "O"]
    counter = 0
    while True:
        
        try:
            user_input = input()
            if user_input == "q":
                sys.exit()

            user_input = int(user_input) -1

            if user_input not in range(10):
                raise ValueError

        except ValueError:
            drawBoard(board, startingPoint(size))
            continue

        if board[user_input] in current_user:
            drawBoard(board, startingPoint(size))
            continue

        counter += 1
        board[user_input] = current_user[counter % 2]
        drawBoard(board, startingPoint(size))

        result = is_winning(board)
        if result:
            print(f"{result} wins!")
            sys.exit()


        if " " not in board:
            print("Tie!")
            sys.exit()

        

if __name__ == "__main__":
    main()
