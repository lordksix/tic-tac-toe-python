"""Module that with Mark and Grid classes"""
import enum
import re
from dataclasses import dataclass
from functools import cached_property

WINNING_PATTERNS = (
    "???......",
    "...???...",
    "......???",
    "?..?..?..",
    ".?..?..?.",
    "..?..?..?",
    "?...?...?",
    "..?.?.?..",
)

class Mark(enum.StrEnum):
    """Class that handles user marks

    Args:
        enum (_type_): CROSS or X, or NAUGHT or O

    Returns:
        _type_: CROSS or X, or NAUGHT or O
    """
    CROSS = "X"
    NAUGHT = "O"

    @property
    def other(self) -> "Mark":
        """Method that returns the opposite MARK

        Returns:
            Mark: can be X or O
        """
        return Mark.CROSS if self is Mark.NAUGHT else Mark.NAUGHT

@dataclass(frozen=True)
class Grid:
    """Inmutable Class that handles the grid. It is instantiate as a empty grid 9 spaces as
    default. It runs as Post instantiation hook that verifies that grid composition. Allowed
    cell position: 9 elements (X, O, or space)

    Raises:
        ValueError: Raises ValueError if
    """
    cells: str = " " * 9

    def __post_init__(self) -> None:
        """Post instantiation hook that verifies that the grid is compose of 9 elements (X, O, or
        space)"""
        if not re.match(r"^[\sXO]{9}$", self.cells):
            raise ValueError("Must contain 9 cells of: X, O, or space")

    @cached_property
    def x_count(self) -> int:
        """Cached getter of total of X

        Returns:
            int: Total of X
        """
        return self.cells.count("X")

    @cached_property
    def o_count(self) -> int:
        """Cached getter of total of O

        Returns:
            int: Total of Y
        """
        return self.cells.count("O")

    @cached_property
    def empty_count(self) -> int:
        """Cached getter of total of spaces

        Returns:
            int: Total of spaces
        """
        return self.cells.count(" ")

@dataclass(frozen=True)
class Move:
    """Inmutable data Class that is strictly a data transfer object (DTO) whose main purpose is to
    carry data. Consists of the mark identifying the player who made a move, a numeric zero-based
    index in the string of cells, and the two states before and after making a move.
    """
    mark: Mark
    cell_index: int
    before_state: "GameState"
    after_state: "GameState"

@dataclass(frozen=True)
class GameState:
    """Inmutable data Class that is strictly a data transfer object (DTO) whose main purpose is to
    carry data, consisting of the grid of cells and the starting player’s mark
    """
    grid: Grid
    starting_mark: Mark = Mark("X")

    @cached_property
    def current_mark(self) -> Mark:
        """Cached getter of current mark

        Returns:
            Mark: Mark of current state
        """
        if self.grid.x_count == self.grid.o_count:
            return self.starting_mark
        else:
            return self.starting_mark.other

    @cached_property
    def game_not_started(self) -> bool:
        """Cached getter if current state is the initial state

        Returns:
            bool: Rather current turn is the first turn or not
        """
        return self.grid.empty_count == 9

    @cached_property
    def game_over(self) -> bool:
        """Cached getter to check if the game is ofver by check if there is a winner or
        there is a tie

        Returns:
            bool: Rather the game is over or not
        """
        return self.winner is not None or self.tie

    @cached_property
    def tie(self) -> bool:
        """Cached getter to check if there is a tie by checking if
        there is a winner or grid is empty

        Returns:
            bool: Rather the game has a winner or grid is empty
        """
        return self.winner is None and self.grid.empty_count == 0

    @cached_property
    def winner(self) -> Mark | None:
        """Chaced getter that check if there is a winner by checking winning patterns

        Returns:
            Mark | None: Could be X, O or None
        """
        for pattern in WINNING_PATTERNS:
            for mark in Mark:
                if re.match(pattern.replace("?", mark), self.grid.cells):
                    return mark
        return None

    @cached_property
    def winning_cells(self) -> list[int]:
        """Chaced getter with information of position of marks in winning cell

        Returns:
            list[int]: List of positions of marks in winning cell
        """
        for pattern in WINNING_PATTERNS:
            for mark in Mark:
                if re.match(pattern.replace("?", mark), self.grid.cells):
                    return [
                        match.start()
                        for match in re.finditer(r"\?", pattern)
                    ]
        return []
