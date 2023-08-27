"""Provide the class that handles the game.

This module allows the game to run. It is the game engine.

Examples:

    >>> player1 = RandomComputerPlayer(Mark("X"))
    >>> player2 = RandomComputerPlayer(Mark("O"))
    >>> TicTacToe(player1, player2, ConsoleRenderer()).play()

The module contains the following class:
- `TicTacToe`

"""
from dataclasses import dataclass
from typing import Callable, TypeAlias

from backend.logic.exceptions import InvalidMove
from backend.logic.models import GameState, Grid, Mark
from backend.logic.validators import validate_players

from .players import Player
from .renderers import Renderer

ErrorHandler: TypeAlias = Callable[[Exception], None]


@dataclass(frozen=True)
class TicTacToe:
    """A class used to represebt the game engine.

    Attributes:
        player1: Player
            An instance of subclass of the Player class that represents a human or computer.
        player2: Player
            An instance of subclass of the Player class that represents a human or computer.
        renderer: Renderer
            An instance of subclass of the Renderer class that handles UI rendering.
        error_handler: ErrorHandler | None = None
            A placehholder for a callback function that handles InvalidMove exceptions.

    Methods:
        play(self, starting_mark: Mark = Mark("X")) -> None:
            Handles the flow of the game. The engine itself
        def get_current_player(self, game_state: GameState) -> Player:
            Determines current player base on the current game state
    """

    player1: Player
    player2: Player
    renderer: Renderer
    error_handler: ErrorHandler | None = None

    def __post_init__(self):
        """Post instantiation hook that verifies that the player instantiation was corrected"""
        validate_players(self.player1, self.player2)

    def play(self, starting_mark: Mark = Mark("X")) -> None:
        """Starts and handles the game until the game is over

        Args:
            starting_mark (Mark, optional): Initial Mark. Defaults to Mark("X").
        """
        game_state = GameState(Grid(), starting_mark)
        while True:
            self.renderer.render(game_state)
            if game_state.game_over:
                break
            player = self.get_current_player(game_state)
            try:
                game_state = player.make_move(game_state)
            except InvalidMove as ex:
                if self.error_handler:
                    self.error_handler(ex)

    def get_current_player(self, game_state: GameState) -> Player:
        """Determines current player base on the current game state

        Args:
            game_state (GameState): current GameState, consisting of a current Grid (9 elemets that
                that can be X, O or spaces) and a starting Mark (default X).

        Returns:
            Player: The player that has to play current turn
        """
        if game_state.current_mark is self.player1.mark:
            return self.player1
        return self.player2
