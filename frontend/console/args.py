"""Provide the classes and functions to handle CLI arguments and options.

This module allows the handle CLI arguments and options.

The module contains the following classes and functions:
- `Args(NamedTuple)` - A class to create a namedtuple to handle arguments for CLI
- `parse_args` - Returns type handled tuple with information about the players and initial Mark.
"""

import argparse
from typing import NamedTuple

from tic_tac_toe.game.players import (
    Player,
    RandomComputerPlayer,
    MinimaxComputerPlayer,
)
from tic_tac_toe.logic.models import Mark

from .players import ConsolePlayer

PLAYER_CLASSES = {
    "human": ConsolePlayer,
    "random": RandomComputerPlayer,
    "minimax": MinimaxComputerPlayer,
}

class Args(NamedTuple):
    """A class that handle arguments for CLI

    Args:
        NamedTuple (_type_): Player1, Player2, starting_mark.

    Attributes:
        player1: Player
            An instance of subclass of the Player class that represents a human or computer.
        player2: Player
            An instance of subclass of the Player class that represents a human or computer.
        renderer: Renderer
            An instance of subclass of the Renderer class that handles UI rendering.
    """
    player1: Player
    player2: Player
    starting_mark: Mark

def parse_args() -> Args:
    """Returns type handled tuple with information about the players and initial Mark.

    Returns:
        Args: tuple[Player, Player, Mark] tuple with players and Mark
    """

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-X",
        dest="player_x",
        choices=PLAYER_CLASSES.keys(),
        default="human",
    )
    parser.add_argument(
        "-O",
        dest="player_o",
        choices=PLAYER_CLASSES.keys(),
        default="minimax",
    )
    parser.add_argument(
        "-s",
        "--starting",
        dest="starting_mark",
        choices=Mark,
        type=Mark,
        default="X",
    )
    args = parser.parse_args()

    player1 = PLAYER_CLASSES[args.player_x](Mark("X"))
    player2 = PLAYER_CLASSES[args.player_o](Mark("O"))

    if args.starting_mark == "O":
        player1, player2 = player2, player1

    return Args(player1, player2, args.starting_mark)
