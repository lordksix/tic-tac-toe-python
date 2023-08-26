"""Provide the classes to instantiate players, human or computer.

This module allows the creation of different categories of players.

Typical usage example:

    player1 = RandomComputerPlayer(Mark("X"))
    player2 = MinimaxComputerPlayer(Mark("O"))

The module contains the following class:
- `Player` - ABC
- `ComputerPlayer` - ABC. Extension of class Player.
- `RandomComputerPlayer` - Extension of class ComputerPlayer.
- `MinimaxComputerPlayer` - ABC. Extension of class ComputerPlayer.
"""
import abc
import time

from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.logic.minimax import find_best_move
from tic_tac_toe.logic.models import GameState, Mark, Move

class Player(metaclass=abc.ABCMeta):
    """Abstract class for the creation of players. Extends as metaclass, abc.ABCMeta.

    Attributes:
        mark: Mark
            An instance of Mark class that handles user marks.

    Methods:
        make_move(self, game_state: GameState) -> GameState:
            Handles the current player move.
        get_move(self, game_state: GameState) -> Move | None:
            Determines current player base on the current game state. Abstract method.
    """
    def __init__(self, mark: Mark) -> None:
        """Initializes the instance based on mark provided.
        Args:
            mark (Mark): An instance class that handles user marks.
        """
        self.mark = mark

    def make_move(self, game_state: GameState) -> GameState:
        """Handles the current player move which depends on the get_move method
        implemented in each subclass if it's the given player's turn and whether the move exists.

        Args:
            game_state (GameState): current GameState, consisting of a current Grid (9 elemets that
                that can be X, O or spaces) and a starting Mark (default X).

        Raises:
            InvalidMove: Exception when a invalid move is selected
        Returns:
            GameState: current GameState, consisting of a current Grid (9 elemets that
            that can be X, O or spaces) and a starting Mark (default X).
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
    """Abstract class for the creation of computer players. Extends as metaclass, abc.ABCMeta.
        Extends Player abstract class An instance of subclass of the Player class that represents
        a human or computer.

    Attributes:
        mark: Mark
            An instance of Mark class that handles user marks

    Methods:
        get_move(self, game_state: GameState) -> Move | None:
            Return the current computer player's move in the given game state
        get_computer_move(self, game_state: GameState) -> Move | None:
            Determines current player base on the current game state. Abstract method
    """
    def __init__(self, mark: Mark, delay_seconds: float = 0.25) -> None:
        """
        Args:
            mark (Mark): An instance class that handles user marks
            delay_seconds (float, optional): Represents the delay time for the computer
                to player. Defaults to 0.25.
        """
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
    """Class for the creation of computer players with random moves. Extends ComputerPlayer
    abstract class.

    Methods:
        get_computer_move(self, game_state: GameState) -> Move | None:
            Return the current computer player's random move in the given game state.
    """
    def get_computer_move(self, game_state: GameState) -> Move | None:
        """Return the current computer player's random move in the given game state.

        Args:
            game_state (GameState): current GameState, consisting of a current Grid (9 elemets that
                that can be X, O or spaces) and a starting Mark (default X).

        Returns:
            Move | None: return a move class or none
        """
        return game_state.make_random_move()

class MinimaxComputerPlayer(ComputerPlayer):
    """A class for the creation of computer players with move based on minimax algorithm.
    Extends ComputerPlayer, an abstract class for the creation of computer players.

    Methods:
        get_computer_move(self, game_state: GameState) -> Move | None:
            Return the current computer player's move in the given game state.
    """
    def get_computer_move(self, game_state: GameState) -> Move | None:
        """Return the current computer player's move in the given game state using
        minimax algorithm.

        Args:
            game_state (GameState): current GameState, consisting of a current Grid (9 elemets that
                that can be X, O or spaces) and a starting Mark (default X).

        Returns:
            Move | None: return a move class or none.
        """
        if game_state.game_not_started:
            return game_state.make_random_move()
        return find_best_move(game_state)
