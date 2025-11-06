from typing import Dict
from typing import Callable


def fit(num: int, maximum: int, minimun: int = 0) -> int:
    """
    makes a number fit inside a given range
    """
    num = max(num, minimun)
    num = min(num, maximum)
    return num


class Robot:
    """
    class for controlling the robot on a given board
    """

    DIRECTIONS = ["up", "down", "left", "right"]
    MODES = ["off", "on", "R"]
    MODE_ON = 1
    MODE_OFF = 0
    MODE_R = 2
    MODE_ON_SYMBOL = 'X'
    MODE_R_SYMBOL = '.'

    _commands: Dict[str, str] = {"left": "",
                                 "right": "",
                                 "up": "",
                                 "down": "",
                                 "<num>": "go num steps in current direction",
                                 "on": "will wash places he visits",
                                 "off": "will not wash places he visits",
                                 "R": "puts robot in reverse mode, make stuff dirty again"}

    def __init__(self) -> None:
        """
        initiates robot
        """
        self._current_mode = self.MODE_ON
        self._current_direction = [0, 1]
        self._current_position = [0, 0]

    def print_commands(self) -> None:
        """
        prints all commands that this robot supports
        """
        print("Avaliable commands:")
        i = 1
        for key in self._commands.keys():
            print(f"{i}. {key}", end="")
            i += 1
            if self._commands[key] != "":
                print(f" - {self._commands[key]}", end="")
            print()

    def paint(self, position: tuple[int, int], board: list[list[str]]) -> list[list[str]]:
        """
        Paints a certain position on the floor according to the mode
        """
        if self._current_mode == self.MODE_OFF:
            return board
        elif self._current_mode == self.MODE_ON:
            board[position[0]][position[1]] = self.MODE_ON_SYMBOL
        else:
            board[position[0]][position[1]] = self.MODE_R_SYMBOL
        return board

    def move(self, num: int, board: list[list[str]]) -> list[list[str]]:
        """
        Move the robot num places in the current direction and paint the floor
        """
        new_position = self._current_position.copy()
        new_position[0] = fit(new_position[0] + num * self._current_direction[0], len(board) - 1)
        new_position[1] = fit(new_position[1] + num * self._current_direction[1], len(board) - 1)

        for i in range(new_position[0], self._current_position[0], -self._current_direction[0] | 1):
            board = self.paint((i, self._current_position[1]), board)

        for i in range(new_position[1], self._current_position[1], -self._current_direction[1] | 1):
            board = self.paint((self._current_position[0], i), board)

        self._current_position = new_position
        return board

    def parse_commands(self, commands: str, board: list[list[str]]) -> list[list[str]]:
        """
        parses the commands and moves the robot accordinly
        """
        sep_commands = commands.split(" ")
        for command in sep_commands:
            if command in self.DIRECTIONS:
                direction = self.DIRECTIONS.index(command)
                self._current_direction = [0, 0]
                self._current_direction[(direction & 2) // 2] = (direction & 1) * 2 - 1
            elif command.isdecimal():
                self.move(int(command), board)
            elif command in self.MODES:
                self._current_mode = self.MODES.index(command)
            else:
                print(f"Skipping unknown command {command}")
        return board
