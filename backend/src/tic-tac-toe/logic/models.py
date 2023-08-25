"""Module that with Mark and Grid classes"""
import enum
import re
from dataclasses import dataclass
from functools import cached_property

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
    """Class that handles an inmutable grid. It is instantiate as a empty grid 9 spaces as
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
