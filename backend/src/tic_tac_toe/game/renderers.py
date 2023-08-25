"""Module that handles classes for visual and state rendering
"""
import abc

from tic_tac_toe.logic.models import GameState

class Renderer(metaclass=abc.ABCMeta):
    """Abstract class for the creation of visual and state rendering

    Args:
        metaclass (_type_, optional): Setting class as ABC. Defaults to abc.ABCMeta.
    """
    @abc.abstractmethod
    def render(self, game_state: GameState) -> None:
        """Render the current game state."""

    @abc.abstractmethod
    def placerholder(self, game_state: GameState) -> None:
        """Render the current game state."""
