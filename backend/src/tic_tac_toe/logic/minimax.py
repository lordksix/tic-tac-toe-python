"""MOdule that handle computer AI
"""

from functools import partial

from tic_tac_toe.logic.models import GameState, Mark, Move

def find_best_move(game_state: GameState) -> Move | None:
    """Method to find best

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
    """Method to select next move base on minimax algorith

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
