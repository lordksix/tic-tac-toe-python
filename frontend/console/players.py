"""Provide the classes handle human players.

This module allows the handle CLI arguments and options.

The module contains the following classes:
- `ConsolePlayer(Player)` - A class that represents human players.

The module contains the following functions:
- `grid_to_index(grid: str) -> int:` - Return infex of the next move.
"""
import re

from tic_tac_toe.game.players import Player
from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.logic.models import GameState, Move

class ConsolePlayer(Player):
    """A class that represents human players. Extend abstract class for the creation of players.

    Methods:
        get_move(self, game_state: GameState) -> Move | None:
            Return the current player's move based on the human player choice.
    """
    def get_move(self, game_state: GameState) -> Move | None:
        """Return the current player's move based on the human player choice.

        Args:
            game_state (GameState): current GameState, consisting of a current Grid (9 elemets that
                that can be X, O or spaces) and a starting Mark (default X).

        Returns:
            Move | None: return a move class or none.
        """
        while not game_state.game_over:
            try:
                index = grid_to_index(input(f"{self.mark}'s move: ").strip())
            except ValueError:
                print("Please provide coordinates in the form of A1 or 1A")
            else:
                try:
                    return game_state.make_move_to(index)
                except InvalidMove:
                    print("That cell is already occupied.")
        return None

def grid_to_index(grid: str) -> int:
    """Return infex of the next move. Input must be in format A1 or 1A.
    Letters can be A, B or C, and number 1, 2, or 3.

    Args:
        grid (str): String with the position option from human input

    Raises:
        ValueError: Exception when a value of the index is outside bounds.

    Returns:
        int: index of move
    """
    if re.match(r"[abcABC][123]", grid):
        col, row = grid
    elif re.match(r"[123][abcABC]", grid):
        row, col = grid
    else:
        raise ValueError("Invalid grid coordinates")
    return 3 * (int(row) - 1) + (ord(col.upper()) - ord("A"))
