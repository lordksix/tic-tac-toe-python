"""Provide classes for visual and state rendering.

This module allows the creation of UI rendering.

The module contains the following class:
- `Renderer`
"""
import abc

from tic_tac_toe.logic.models import GameState

class Renderer(metaclass=abc.ABCMeta):
    """Abstract class for the creation of visual and state rendering. Extends as metaclass, abc.ABCMeta.

    Methods:
        def render(self, game_state: GameState) -> None:
            Render the current game state.
    """
    @abc.abstractmethod
    def render(self, game_state: GameState) -> None:
        """Render the current game state."""

    def placerholder(self) -> None:
        """Render the current game state."""
