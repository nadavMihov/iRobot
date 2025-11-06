import os
from statistics import mean
from robot import Robot


BOARD_SIZE = 5
WELCOME_MESSAGE = "Welcome to iRobot!"
PROMPT_MESSAGE = "Instructions: "


def create_board() -> list[list[str]]:
    """
    Creates a board of size BOARD_SIZE
    """
    board: list[list[str]] = []
    for i in range(BOARD_SIZE):
        board += [[]]
        for j in range(BOARD_SIZE):
            board[i] += ['.']
    return board


def print_board(board: list[list[str]]) -> None:
    """
    Prints the board
    """
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            print(board[i][j], end=' ')
        print("")


def main() -> None:
    board = create_board()
    r = Robot()
    print(WELCOME_MESSAGE)
    r.print_commands()
    commands = input(PROMPT_MESSAGE)
    board = r.parse_commands(commands, board)
    print_board(board)


if __name__ == "__main__":
    main()
