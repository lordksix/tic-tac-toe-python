"""Script that handles initiation of game using CLI

    $ python -m console [options] [id] [id ...]

    Available options are:

        -X              Choose player with mark X
        -O              Choose player with mark O
        -S, --starting  Choose starting mark

    Available arguments are:
        - 'human':      Argument for a human player
        - 'random':     Argument for a random computer player
        - 'minimax':    Argument for a minimax computer player
        - 'X':          Starting mark 'X'
        - 'O':          Starting mark 'O'
"""

from .console.cli import main

if __name__ == "__main__":
    main()
