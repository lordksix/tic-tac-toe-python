"""Module that handles the game and logic
"""
from dataclasses import dataclass
from typing import Callable, TypeAlias

from tic_tac_toe.game.players import Player
from tic_tac_toe.game.renderers import Renderer
from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.logic.models import GameState, Grid, Mark
from tic_tac_toe.logic.validators import validate_players

ErrorHandler: TypeAlias = Callable[[Exception], None]

@dataclass(frozen=True)
class TicTacToe:
    """Application engine
    """
    player1: Player
    player2: Player
    renderer: Renderer
    error_handler: ErrorHandler | None = None

    def __post_init__(self):
        """Post instantiation hook that verifies that the player instantiation was corrected
        """
        validate_players(self.player1, self.player2)

    def play(self, starting_mark: Mark = Mark("X")) -> None:
        """Method that starts and handles the game until the game is over

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
        """Method that determines current player base on the current game state

        Args:
            game_state (GameState): current GameState, consisting of a current Grid (9 elemets that
            that can be X, O or spaces) and a starting Mark (default X)

        Returns:
            Player: The player that has to play current turn
        """
        if game_state.current_mark is self.player1.mark:
            return self.player1
        else:
            return self.player2
