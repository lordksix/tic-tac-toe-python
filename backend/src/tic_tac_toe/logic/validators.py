"""Module with methods to validate grid and gamestates"""

from __future__ import annotations
import re
from typing import TYPE_CHECKING
from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.logic.exceptions import InvalidGameState

if TYPE_CHECKING:
    from tic_tac_toe.game.players import Player
    from tic_tac_toe.logic.models import GameState, Grid, Mark

def validate_grid(grid: Grid) -> None:
    """Method that verifies that the grid is compose of 9 elements (X, O, or
    space)

    Args:
        grid (Grid): Grid with 9 elements(X, O or space)

    Raises:
        ValueError: "Must contain 9 cells of: X, O, or space"
    """
    if not re.match(r"^[\sXO]{9}$", grid.cells):
        raise ValueError("Must contain 9 cells of: X, O, or space")

def validate_game_state(game_state: GameState) -> None:
    """Method to verify a correct gamestate

    Args:
        game_state (GameState): GameState
    """
    validate_number_of_marks(game_state.grid)
    validate_starting_mark(game_state.grid, game_state.starting_mark)
    validate_winner(
        game_state.grid, game_state.starting_mark, game_state.winner
    )

def validate_number_of_marks(grid: Grid) -> None:
    """Method to verify the correct quantity of X and O

    Args:
        grid (Grid): Grid with 9 elements(X, O or space)

    Raises:
        InvalidGameState: Custom exception
    """
    if abs(grid.x_count - grid.o_count) > 1:
        raise InvalidGameState("Wrong number of Xs and Os")

def validate_starting_mark(grid: Grid, starting_mark: Mark) -> None:
    """Verifies that the correct Mark was selected

    Args:
        grid (Grid): Grid with 9 elements(X, O or space)
        starting_mark (Mark): Mark X

    Raises:
        InvalidGameState: Custom exception
    """
    if grid.x_count > grid.o_count:
        if starting_mark != "X":
            raise InvalidGameState("Wrong starting mark")
    elif grid.o_count > grid.x_count and starting_mark != "O":
          raise InvalidGameState("Wrong starting mark")

def validate_winner(
    grid: Grid, starting_mark: Mark, winner: Mark | None
) -> None:
    """Method to validate winner

    Args:
        grid (Grid): Grid with 9 elements(X, O or space)
        starting_mark (Mark): Mark X
        winner (Mark | None): Winner if any

    Raises:
        InvalidGameState: Custom exception
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
    """Method that validates the correct instantiation of Players.
    Players must use different marks

    Args:
        player1 (Player): Player consisting in a Mark
        player2 (Player): Player consisting in a Mark

    Raises:
        ValueError: custom exception
    """
    if player1.mark is player2.mark:
        raise ValueError("Players must use different marks")
