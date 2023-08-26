"""Provide custom exceptions for the game.

This module allows the raise of custom exceptions.

The module contains the following custom exceptions:
- `InvalidGameState`
- `InvalidMove`
- `UnknownGameScore`
"""

class InvalidGameState(Exception):
    """Raised when the game state is invalid."""

class InvalidMove(Exception):
    """Raised when the move is invalid."""

class UnknownGameScore(Exception):
    """Raised when the game score is unknown."""
