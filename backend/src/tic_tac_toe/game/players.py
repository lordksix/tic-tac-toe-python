import abc
import random
import time

from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.logic.models import GameState, Mark, Move

class Player(metaclass=abc.ABCMeta):
    """Abstract class for the creation of players

    Args:
        metaclass (_type_, optional): Setting class as ABC. Defaults to abc.ABCMeta.
    """
    def __init__(self, mark: Mark) -> None:
        self.mark = mark

    def make_move(self, game_state: GameState) -> GameState:
        """Public method that handles player move which depends on the get_move method
        implemented in each subclass if it's the given player's turn and whether the move exists

        Args:
            game_state (GameState): current GameState, consisting of a current Grid (9 elemets that
            that can be X, O or spaces) and a starting Mark (default X).

        Raises:
            InvalidMove: custom exception
        Returns:
            GameState: current GameState, consisting of a current Grid (9 elemets that
            that can be X, O or spaces) and a starting Mark (default X)
        """
        if self.mark is game_state.current_mark:
            if move := self.get_move(game_state):
                return move.after_state
            raise InvalidMove("No more possible moves")
        raise InvalidMove("It's the other player's turn")

    @abc.abstractmethod
    def get_move(self, game_state: GameState) -> Move | None:
        """Return the current player's move in the given game state."""

class ComputerPlayer(Player, metaclass=abc.ABCMeta):
    """Abstract class for the creation of computer players

    Args:
        Player (_type_): Abstract class for the creation of players
        metaclass (_type_, optional): Setting class as ABC. Defaults to abc.ABCMeta.
    """
    def __init__(self, mark: Mark, delay_seconds: float = 0.25) -> None:
        super().__init__(mark)
        self.delay_seconds = delay_seconds

    def get_move(self, game_state: GameState) -> Move | None:
        """Return the current computer player's move in the given game state

        Args:
            game_state (GameState): current GameState, consisting of a current Grid (9 elemets that
            that can be X, O or spaces) and a starting Mark (default X).

        Returns:
            Move | None: return a move class or none
        """
        time.sleep(self.delay_seconds)
        return self.get_computer_move(game_state)

    @abc.abstractmethod
    def get_computer_move(self, game_state: GameState) -> Move | None:
        """Return the computer's move in the given game state."""

class RandomComputerPlayer(ComputerPlayer):
    """Class for the creation of computer players

    Args:
        ComputerPlayer (_type_): Abstract class for the creation of computer players
    """
    def get_computer_move(self, game_state: GameState) -> Move | None:
        """Return the current computer player's move in the given game state.

        Args:
            game_state (GameState): current GameState, consisting of a current Grid (9 elemets that
            that can be X, O or spaces) and a starting Mark (default X).

        Returns:
            Move | None: return a move class or none
        """
        try:
            return random.choice(game_state.possible_moves)
        except IndexError:
            return None
