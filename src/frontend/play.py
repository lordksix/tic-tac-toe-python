"""Provide script to start game
"""

from frontend.console.players import ConsolePlayer
from frontend.console.renderers import ConsoleRenderer

from backend.game.engine import TicTacToe
from backend.game.players import RandomComputerPlayer
from backend.logic.models import Mark

player1 = ConsolePlayer(Mark("X"))
player2 = RandomComputerPlayer(Mark("O"))

TicTacToe(player1, player2, ConsoleRenderer()).play()
