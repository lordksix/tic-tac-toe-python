This part of the project documentation focuses on a
**problem-oriented** approach. You'll tackle common
tasks that you might have, with the help of the code
provided in this project.

## How is it structured?

Download the code from this GitHub repository and place
the `tic-tac-toe-python/` folder in the same directory as your
Python script:

    tic-tac-toe/
    │
    ├── docs/
    │   │
    │   |── explanation.md
    │   |── index.md
    │   |── tutorials.md
    │   ├── how-to-guides.md
    |   └── reference.md
    │
    └── src/
        ├── frontends/
        │   |
        |   └── console/
        |   │    ├── __init__.py
        |   │    └── __main__.py
        |   │    ├── arg.py
        |   │    └── cli.py
        |   │    ├── players.py
        |   │    └── renderers.py
        |   |
        |   ├── __init__.py
        |   └── play.py
        │
        ├── backend/
        │   │
        │   ├── game/
        │   │   ├── __init__.py
        │   │   ├── engine.py
        │   │   ├── players.py
        │   │   └── renderers.py
        │   │
        │   ├── logic/
        │   │   ├── __init__.py
        │   │   ├── exceptions.py
        │   │   ├── models.py
        │   │   └── validators.py
        │   │
        │   └── __init__.py
        │
        └── pyproject.toml

You can run the script `play.py`, to run the most basic and
default version of the game:

```sh
  tictactoe -X human -O minimax
```

Where -X mean the player that uses the X mark, options: human, random, minimax
Where -O mean the player that uses the O mark, options: human, random, minimax
