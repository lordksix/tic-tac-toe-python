"""Module to handle CLI start game
"""

from tic_tac_toe.game.engine import TicTacToe

from .args import parse_args
from .renderers import ConsoleRenderer

def main() -> None:
    """Public method to start game from CLI
    """
    player1, player2, starting_mark = parse_args()
    TicTacToe(player1, player2, ConsoleRenderer()).play(starting_mark)
