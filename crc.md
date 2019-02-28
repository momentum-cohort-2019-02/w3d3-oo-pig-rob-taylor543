# Game

**Responsibilities**
- Keeps track of the state of the game (dice list, player totals, turn totals, etc)
- Reports to the player the state of the game when asked

**Collaborators**
- Player
- Strategy
- Die


# Player

**Responsibilities**
- Chooses to roll or to hold (If it has a Strategy, use that and the Game state to decide to roll, otherwise takes user input)

**Collaborators**
- Game
- Strategy


# Strategy

**Responsibilities**
- Using a set of initial parameters and arguments that it gets from the Player and the state of the Game, decides to roll or to hold

**Collaborators**
- Player
- Game


# Die

**Responsibilities**
- Keep track of how many sides or what the sides have on them
- Be able to roll itself and return one of the sides as an integer

**Collaborators**
- Game
- Player