"""Module with classes and methods to handle UI
"""

import textwrap
from typing import Iterable

from tic_tac_toe.game.renderers import Renderer
from tic_tac_toe.logic.models import GameState

class ConsoleRenderer(Renderer):
    """Class to handler render of the console

    Args:
        Renderer (_type_): Abstract class for the creation of visual and state rendering
    """
    def render(self, game_state: GameState) -> None:
        """Method that renders a new UI depending on game state

        Args:
            game_state (GameState): current GameState, consisting of a current Grid (9 elemets that
            that can be X, O or spaces) and a starting Mark (default X).
        """
        clear_screen()
        if game_state.winner:
            print_blinking(game_state.grid.cells, game_state.winning_cells)
            print(f"{game_state.winner} wins \N{party popper}")
        else:
            print_solid(game_state.grid.cells)
            if game_state.tie:
                print("No one wins this time \N{neutral face}")

    def placeholder2(self) -> None:
        """This is a placeholder
        """
def clear_screen() -> None:
    """Method to clear console, like command reset on modern Linux systems
    """
    print("\033c", end="")

def blink(text: str) -> str:
    """Method to clear console, like command reset on modern Linux systems. [5m slow blink
    and [0m reset
    """
    return f"\033[5m{text}\033[0m"

def print_blinking(cells: Iterable[str], positions: Iterable[int]) -> None:
    """Method to add blinking ANSI code to positions in cells

    Args:
        cells (Iterable[str]): Lits of all cells
        positions (Iterable[int]): List of positions
    """
    mutable_cells = list(cells)
    for position in positions:
        mutable_cells[position] = blink(mutable_cells[position])
    print_solid(mutable_cells)

def print_solid(cells: Iterable[str]) -> None:
    """Method to render game UI. It uses textwrap and format to replace on the correct position

    Args:
        cells (Iterable[str]): _description_
    """

    print(
        textwrap.dedent(
            """\
             A   B   C
           ------------
        1 ┆  {0} │ {1} │ {2}
          ┆ ───┼───┼───
        2 ┆  {3} │ {4} │ {5}
          ┆ ───┼───┼───
        3 ┆  {6} │ {7} │ {8}
    """
        ).format(*cells)
    )