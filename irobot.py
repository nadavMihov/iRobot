import os
from statistics import mean


BOARD_SIZE = 5
MESSAGE = ("Welcome to iRobot!\n"
           "Avaliable commands:\n"
           "left\n"
           "right\n"
           "up\n"
           "down\n"
           "<num> - go num steps in current direction\n"
           "on - will wash places he visits\n"
           "off - will not wash places he visits\n"
           "R - puts robot in reverse mode, make stuff dirty again\n"
           "quit - quit the program\n"
           "Instructions: ")
DIRECTIONS = ["up", "down", "right", "left"]
MODES = ["on", "off", "R"]
board: list[list[str]] = []
current_mode = 1
current_direction = "right"
current_position = (0, 0)


def create_board() -> None:
    """
    Creates a board of size BOARD_SIZE
    """
    global board
    for i in range(BOARD_SIZE):
        board += [[]]
        for j in range(BOARD_SIZE):
            board[i] += ['.']


def print_board() -> None:
    """
    Prints the board
    """
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            print(board[i][j], end=' ')
        print("")


def paint(position: tuple[int, int]) -> None:
    """
    Paints a certain position on the floor according to the mode
    """
    if current_mode == 0:
        return
    elif current_mode == 1:
        board[position[0]][position[1]] = 'X'
    else:
        board[position[0]][position[1]] = '.'


def change_mode(mode: str) -> None:
    """
    changes the mode of the robot
    """
    global current_mode
    if mode == "on":
        current_mode = 1
    elif mode == "off":
        current_mode = 0
    elif mode == "R":
        current_mode = 2


def move(num: int) -> None:
    """
    Move the robot num places in the current direction and paint the floor
    """
    global current_position
    new_position = current_position
    if current_direction == "left":
        new_position = (current_position[0], max(0, current_position[1] - num))
        for i in range(new_position[1], current_position[1]):
            paint((current_position[0], i))
    elif current_direction == "right":
        new_position = (current_position[0], min(BOARD_SIZE - 1, current_position[1] + num))
        for i in range(current_position[1] + 1, new_position[1] + 1):
            paint((current_position[0], i))
    elif current_direction == "up":
        new_position = (max(0, current_position[0] - num), current_position[1])
        for i in range(new_position[0], current_position[0]):
            paint((i, current_position[1]))
    elif current_direction == "down":
        new_position = (min(BOARD_SIZE - 1, current_position[0] + num), current_position[1])
        for i in range(current_position[0] + 1, new_position[0] + 1):
            paint((i, current_position[1]))
    current_position = new_position


def parse_commands(commands: str) -> bool:
    """
    parses the commands and moves the robot accordinly

    :return True if quit
    """
    global current_direction
    sep_commands = commands.split(" ")
    for command in sep_commands:
        if command == "quit":
            return True
        elif command in DIRECTIONS:
            current_direction = command
        elif command.isdecimal():
            move(int(command))
        elif command in MODES:
            change_mode(command)
        else:
            print(f"Skipping unknown command {command}")
    return False


def main() -> None:
    create_board()
    play = True
    while play:
        commands = input(MESSAGE)
        play = not parse_commands(commands)
        print_board()


if __name__ == "__main__":
    main()
