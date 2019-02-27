# Game

**Responsibilities**
- Controls the flow of the game
- Keeps track of the state of the game (player totals, etc)
- Reports to the player the state of the game

**Collaborators**
- Player
- Strategy


# Player

**Responsibilities**
- Chooses to roll or to hold (If it has a Strategy, use that to decide to roll, otherwise takes user input)
- Keeps track of the current point total for the turn only (total points are managed by the Game class)
- Takes a turn (and reports point results for that turn)

**Collaborators**
- Game
- Strategy


# Strategy

**Responsibilities**
- Using a set of initial parameters and arguments that it gets from the Player and the state of the Game, decides to roll or to hold

**Collaborators**
- Player
- Game
