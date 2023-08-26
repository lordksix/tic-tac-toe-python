"""Provide functions to validate grid and gamestates

This module allows more validate different game states and the UI grid.

Examples:

    >>> from tic_tac_toe.logic.models import Grid
    >>> # Create an empty grid
    >>> Grid()
    Grid(cells='         ')

    >>> # Create a grid of a particular cell combination
    >>> Grid("XXOXO O  ")
    Grid(cells='XXOXO O  ')

    >>> # Don't create a grid with too few cells
    >>> Grid("XO")
    Traceback (most recent call last):
    ...
    ValueError: Must contain 9 cells of: X, O, or space

The module contains the following functions:
- `validate_grid(grid: Grid)` - Verify that the grid is compose of 9 elements (X, O, or
    space).
- `validate_game_state(game_state: GameState)` - Verify a correct gamestate, raises exceptions
    if is not.
- `validate_number_of_marks(grid: Grid) ` - Verify the correct quantity of X and O. Differente
    between Xs and Os must not exceed 1.
- `validate_starting_mark(grid: Grid, starting_mark: Mark)` - Verify that the correct starting
    mark is selected.
- `validate_winner(
    grid: Grid, starting_mark: Mark, winner: Mark | None
    ) ` - Validate winner by verifying total of Xs and Os.
- `validate_players(player1: Player, player2: Player)` - Validate the correct instantiation of
    Players.
"""

from __future__ import annotations
import re
from typing import TYPE_CHECKING
from tic_tac_toe.logic.exceptions import InvalidGameState

if TYPE_CHECKING:
    from tic_tac_toe.game.players import Player
    from tic_tac_toe.logic.models import GameState, Grid, Mark

def validate_grid(grid: Grid) -> None:
    """Verify that the grid is compose of 9 elements (X, O, or
    space). Raises ValueError it the composition is incorrect

    Args:
        grid (Grid): Grid with 9 elements(X, O or space)

    Raises:
        ValueError: "Must contain 9 cells of: X, O, or space"
    """
    if not re.match(r"^[\sXO]{9}$", grid.cells):
        raise ValueError("Must contain 9 cells of: X, O, or space")

def validate_game_state(game_state: GameState) -> None:
    """Verify a correct gamestate, raises exceptions if is not.

    Args:
        game_state (GameState): current GameState, consisting of a current Grid (9 elemets that
            that can be X, O or spaces) and a starting Mark (default X)
    """
    validate_number_of_marks(game_state.grid)
    validate_starting_mark(game_state.grid, game_state.starting_mark)
    validate_winner(
        game_state.grid, game_state.starting_mark, game_state.winner
    )

def validate_number_of_marks(grid: Grid) -> None:
    """Verify the correct quantity of X and O. Differente between Xs and Os
    must not exceed 1.

    Args:
        grid (Grid): Grid with 9 elements(X, O or space).

    Raises:
        InvalidGameState: Exception that represent a invalidad game state.
    """
    if abs(grid.x_count - grid.o_count) > 1:
        raise InvalidGameState("Wrong number of Xs and Os")

def validate_starting_mark(grid: Grid, starting_mark: Mark) -> None:
    """Verifies that the correct starting mark is selected,

    Args:
        grid (Grid): Grid with 9 elements(X, O or space)
        starting_mark (Mark): Mark X

    Raises:
        InvalidGameState: Exception that represent a invalidad game state.
    """
    if grid.x_count > grid.o_count:
        if starting_mark != "X":
            raise InvalidGameState("Wrong starting mark")
    elif grid.o_count > grid.x_count and starting_mark != "O":
        raise InvalidGameState("Wrong starting mark")

def validate_winner(
    grid: Grid, starting_mark: Mark, winner: Mark | None
) -> None:
    """Validate winner by verifying total of Xs and Os.

    Args:
        grid (Grid): Grid with 9 elements(X, O or space)
        starting_mark (Mark): Mark that represents the winner

    Raises:
        InvalidGameState: Exception that represent a invalidad game state.
    """
    if winner == "X":
        if starting_mark == "X":
            if grid.x_count <= grid.o_count:
                raise InvalidGameState("Wrong number of Xs")
        else:
            if grid.x_count != grid.o_count:
                raise InvalidGameState("Wrong number of Xs")
    elif winner == "O":
        if starting_mark == "O":
            if grid.o_count <= grid.x_count:
                raise InvalidGameState("Wrong number of Os")
        else:
            if grid.o_count != grid.x_count:
                raise InvalidGameState("Wrong number of Os")

def validate_players(player1: Player, player2: Player) -> None:
    """Validates the correct instantiation of Players. Players must use different marks

    Args:
        player1 (Player): An instance of subclass of the Player class that
            represents a human or computer
        player2 (Player): An instance of subclass of the Player class that
            represents a human or computer

    Raises:
        ValueError: Exception that represent a invalidad game state.
    """
    if player1.mark is player2.mark:
        raise ValueError("Players must use different marks")
