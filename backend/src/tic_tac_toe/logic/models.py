"""Provide the classes for domain model.

This module allows the creation of intances of Marks, Grids, Move and GameState.

The module contains the following class:
- `Mark` - A class that handles user marks.
- `Grid` - A inmutable Class that handles the grid information.
- `Move` - A inmutable data class that handles move information.
- `GameState` - A inmutable data class that handles game state information.
"""
import enum
import random
import re
from dataclasses import dataclass
from functools import cached_property

from tic_tac_toe.logic.exceptions import InvalidMove, UnknownGameScore
from tic_tac_toe.logic.validators import validate_game_state, validate_grid

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
    """A class that handles user marks. it can be CROSS or X, or NAUGHT or O. Extends enum.StrEnum
        class. It can be CROSS or X, or NAUGHT or O.

    Methods:
        other(self) -> "Mark":
            Returns the opposite MARK
            space).

    Returns:
        (Mark): CROSS or X, or NAUGHT or O
    """
    CROSS = "X"
    NAUGHT = "O"

    @property
    def other(self) -> "Mark":
        """Returns the opposite MARK.

        Returns:
            Mark: can be X or O.
        """
        return Mark.CROSS if self is Mark.NAUGHT else Mark.NAUGHT

@dataclass(frozen=True)
class Grid:
    """An inmutable Class that handles the grid. It is instantiate as a empty grid 9 spaces as
    default. It runs as Post instantiation hook that verifies that grid composition. Allowed
    cell position: 9 elements (X, O, or space).

    Attributes:
        cells: str
            Represents the grid, 9 elements X, O or space.

    Methods:
        x_count(self) -> int:
            Cached getter of total of X.
        o_count(self) -> int:
            Cached getter of total of O
        empty_count(self) -> int:
            Cached getter of total of spaces

    Raises:
        ValueError: Raises ValueError if
    """
    cells: str = " " * 9

    def __post_init__(self) -> None:
        """Post instantiation hook that verifies that the grid is compose of 9 elements (X, O, or
        space)"""
        validate_grid(self)

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
    """An inmutable data class that is strictly a data transfer object (DTO) whose main purpose
    is to carry data. Consists of the mark identifying the player who made a move, a numeric
    zero-based index in the string of cells, and the two states before and after making a move.

    Attributes:
        mark: Mark
            Represent the mark of the player.
        cell_index: int
            Represent the position to play.
        before_state: "GameState"
            Represent the game state before the move.
        after_state: "GameState"
            Represent the game state after the move.
    """
    mark: Mark
    cell_index: int
    before_state: "GameState"
    after_state: "GameState"

@dataclass(frozen=True)
class GameState:
    """An inmutable data Class that is strictly a data transfer object (DTO) whose main purpose
    is to carry data, consisting of the grid of cells and the starting player's mark

    Attributes:
        grid: Grid
            Represents the grid, 9 elements X, O or space
        starting_mark: Mark = Mark("X")
            Represent the starting mark. Default to X

    Methods:
        current_mark(self) -> Mark:
            Cached getter of current mark.
        game_not_started(self) -> bool:
            Cached getter if current state is the initial state.
        game_over(self) -> bool:
            Cached getter to check if the game is ofver by check if there is a winner or
            there is a tie.
        tie(self) -> bool:
            Cached getter to check if there is a tie by checking if
            there is a winner or grid is empty.
        winner(self) -> Mark | None:
            Cached getter that check if there is a winner by checking winning patterns.
        possible_moves(self) -> list[Move]:
            Cached getter of possible moves.
        make_random_move(self) -> Move | None:
            Return possible move based on possible moves.
        make_move_to(self, index: int) -> Move:
            Return the move to make based on index.
        evaluate_score(self, mark: Mark) -> int:
            Returns score based on the result of the move.
    """
    grid: Grid
    starting_mark: Mark = Mark("X")

    def __post_init__(self) -> None:
        """Post instantiation hook that verifies that the gamestate is correct
        """
        validate_game_state(self)

    @cached_property
    def current_mark(self) -> Mark:
        """Cached getter of current mark.

        Returns:
            Mark: Mark of current state.
        """
        if self.grid.x_count == self.grid.o_count:
            return self.starting_mark
        return self.starting_mark.other

    @cached_property
    def game_not_started(self) -> bool:
        """Cached getter if current state is the initial state.

        Returns:
            bool: Rather current turn is the first turn or not
        """
        return self.grid.empty_count == 9

    @cached_property
    def game_over(self) -> bool:
        """Cached getter to check if the game is ofver by check if there is a winner or
        there is a tie.

        Returns:
            bool: Rather the game is over or not.
        """
        return self.winner is not None or self.tie

    @cached_property
    def tie(self) -> bool:
        """Cached getter to check if there is a tie by checking if
        there is a winner or grid is empty.

        Returns:
            bool: Rather the game has a winner or grid is empty
        """
        return self.winner is None and self.grid.empty_count == 0

    @cached_property
    def winner(self) -> Mark | None:
        """Cached getter that check if there is a winner by checking winning patterns.

        Returns:
            Mark | None: Could be X, O or None.
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

    @cached_property
    def possible_moves(self) -> list[Move]:
        """Cached getter of possible moves.

        Returns:
            list[Move]: list of possible moves
        """
        moves = []
        if not self.game_over:
            for match in re.finditer(r"\s", self.grid.cells):
                moves.append(self.make_move_to(match.start()))
        return moves

    def make_random_move(self) -> Move | None:
        """Return possible move based on possible moves.

        Returns:
            Move | None: Snapshot of moves.
        """
        try:
            return random.choice(self.possible_moves)
        except IndexError:
            return None

    def make_move_to(self, index: int) -> Move:
        """Return the move to make based on index.

        Args:
            index (int): Position of the move.

        Raises:
            InvalidMove: Exception when a invalid move is selected

        Returns:
            Move: Snapshot of moves
        """
        if self.grid.cells[index] != " ":
            raise InvalidMove("Cell is not empty")
        return Move(
            mark=self.current_mark,
            cell_index=index,
            before_state=self,
            after_state=GameState(
                Grid(
                    self.grid.cells[:index]
                    + self.current_mark
                    + self.grid.cells[index + 1:]
                ),
                self.starting_mark,
            ),
        )

    def evaluate_score(self, mark: Mark) -> int:
        """Returns score based on the result of the move.

        Args:
            mark (Mark): Class that handles user marks.

        Raises:
            UnknownGameScore: Exception when no score can be calculated.

        Returns:
            int: score for the game.
        """
        if self.game_over:
            if self.tie:
                return 0
            if self.winner is mark:
                return 1
            return -1
        raise UnknownGameScore("Game is not over yet")
