Snakes On A Plane
==================
A remake of the classic cell phone snake game, coded initially on a plane.

This project is primarily for development practice with different GUI and
build systems in different languages. The goal is to remake the game in
different ways to learn new tools while still maintaining the same core
functionality & assets.

# Core Requirements
## Game
### Basics
* A game map must be presented in a grid.
* Each map tile may contain an item, snake piece, or an environment piece.
* A player is represented by a snake.
* A snake may move up, down, left, or right.
* A snake moves in time intervals.
* Within each move time interval of a snake, its player may alter the direction.
* Snake pieces are connected in a chain, with the head piece as 0 and each
subsequent piece 1...N with N being the end of the chain.
* A snake moves from piece 0 to N, each replacing the spot of the previous one.
* When a snake's length increases, the head will move and its previous position
shall be occupied with a new snake piece.
* When a snake's length decreases, the tail end snake piece shall be removed.
* When a player's snake's head enters a non-empty space, it interacts with
what the space is occupied with.
* When a player's snake dies, the player loses.
* When a snake head hits a snake piece, it dies.
* When a snake head hits an environment piece, it dies.
* When a snake head hits an item piece, the item is collected and its action is
preformed.
* An item may increase/decrease the snake's player's score.
* An item may increase/decrease the length of the snake.
* An item may shorten/lengthen the move time interval of the snake.
* When an item is used up, it is removed.
* An item may be placed at random into an empty grid position.
* There must always be a positive item for a snake to collect on the grid if
there is a space for it to go.
* When there is no more spaces for an item to be placed, the game is over.
* A player's score may be added to the scoreboard with a given name.
* A scoreboard may be saved to a file.
* A scoreboard may be loaded from a file.
* The saving and loading of the scoreboard should be done automatically.
* The scoreboard should be only be loaded into memory when it is needed.
* A user may clear the scoreboard data using the application.
* A user may not alter recorded scores in a scoreboard.
* Scores in a scoreboard are ranked from highest to lowest.


## GUI
* Must have a start screen
* Must have a game screen
* Must have a settings screen
* Must have a win screen
* Must have a game over screen
* Must have a quit
* Must have a scoreboard screen
* Must allow a user to exit game and return to start screen

## Build Actions
* **clean-build** - deletes build files
* **clean-data** - deletes game data files
* **clean-exe** - deletes files created via publish
* **clean** - clean-build + clean-data
* **build** - builds all necessary components to run game
* **run** - starts game from build files in the correct environment
* **start** - build + run
* **test** - preforms unit tests
* **publish** - Copies all files necessary for running the game into a
standalone folder with an executable that can be used to play the game.

## Additions
* Portal tiles that work like edges in PacMan
* Multiple tile graphics for each tile type
* Extra items
* Multi-player (1-screen)
* Multi-player (Networked)
* Different wall configurations (cannot have dead-ends)

# Python Version
* **Status:** In Development
* **GUI:** PyQt5
* **Build System:**: ?
* **Interpreter:** v3.5

## Development setup
```bash
$ cd python
$ virtualenv -p /usr/bin/python3.5 venv
$ source venv/bin/activate
$ pip install --update pip
$ pip install -r requirements.txt
```

## TODO
* Create core game mechanics
* Implement GUI
* Implement Gradle as a build system

## Notes
* [using virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)


# Java Version
* **Status:** TODO
* **GUI:** ?
* **Build System:**: ?

# Android Version
* **Status:** TODO
* **GUI:** ?
* **Build System:**: ?

# C++ Version
* **Status:** TODO
* **GUI:** ?
* **Build System:**: ?

# C# Version
* **Status:** TODO
* **GUI:** ?
* **Build System:**: ?