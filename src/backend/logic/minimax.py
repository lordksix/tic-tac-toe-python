"""Provide functions with basic AI for computer moves.

This module allows more complexity to the computer moves using different
kind of algorithms.

Examples:

    >>> from tic_tac_toe.logic.minimax import minimax
    >>> from tic_tac_toe.logic.models import GameState, Grid, Mark
    >>> def preview(cells):
            print(cells[:3], cells[3:6], cells[6:], sep='\\n')
    >>> game_state = GameState(Grid("XXO O X O"), starting_mark=Mark('X'))
    >>> for move in game_state.possible_moves:
            print("Score:", minimax(move, maximizer=Mark('X')))
            preview(move.after_state.grid.cells)
            print('-' * 10)

The module contains the following functions:
- `find_best_move(game_state: GameState)` - Return the best move available.
- `minimax(
    move: Move, maximizer: Mark, choose_highest_score: bool = False
    )` - Return 1, 0 or -1 base in the result of the next move.
"""

from functools import partial

from backend.logic.models import GameState, Mark, Move

def find_best_move(game_state: GameState) -> Move | None:
    """Return the best move available.

    Args:
        game_state (GameState): current GameState, consisting of a current Grid (9 elemets that
            that can be X, O or spaces) and a starting Mark (default X)

    Returns:
        Move | None: Inmutable data Class that is strictly a data transfer object (DTO) whose main
    purpose is to carry data. Consists of the mark identifying the player who made a move, a numeric
    zero-based index in the string of cells, and the two states before and after making a move.
    """
    maximizer: Mark = game_state.current_mark
    bound_minimax = partial(minimax, maximizer=maximizer)
    return max(game_state.possible_moves, key=bound_minimax)

def minimax(
    move: Move, maximizer: Mark, choose_highest_score: bool = False
) -> int:
    """Return 1, 0 or -1 base in the result of the next move.

    Args:
        move (Move): Inmutable data Class that is strictly a data transfer object (DTO) whose
            main purpose is to carry data. Consists of the mark identifying the player who made a
            move, a numeric zero-based index in the string of cells, and the two states before
            and after making a move.
        maximizer (Mark): Mark for the player
        choose_highest_score (bool, optional): Defaults to False.

    Returns:
        int: returns 1, 0 or -1
    """
    if move.after_state.game_over:
        return move.after_state.evaluate_score(maximizer)
    return (max if choose_highest_score else min)(
        minimax(next_move, maximizer, not choose_highest_score)
        for next_move in move.after_state.possible_moves
    )
