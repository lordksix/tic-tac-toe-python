"""Provide functions to handle CLI start game.

This module allows the handle CLI start game

Examples:
    >>> python -m console -X human -O human

The module contains the following classes and functions:
- `main` - Handle start game from CLI
"""

from tic_tac_toe.game.engine import TicTacToe

from .args import parse_args
from .renderers import ConsoleRenderer

def main() -> None:
    """Handle start game from CLI
    """
    player1, player2, starting_mark = parse_args()
    TicTacToe(player1, player2, ConsoleRenderer()).play(starting_mark)
