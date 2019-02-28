from random import choice

class Game:
    """
    Represents one game of pig.  Parameters are a list of players and a list of dice.
    Can play one round of pig and detect if there are any winners afterwards.
    """

    def __init__(self, players, dice):
        self.player_scores = {}
        for player in players:
            self.player_scores[player] = 0
        self.dice = dice
        self.turn_score = 0

    def play_a_round(self):
        for player in self.player_scores:
            self.turn_score = 0
            while player.choose_to_roll(self):
                roll_total = 0
                for die in dice:
                    roll = die.roll()
                    roll_total += roll
                self.turn_score += roll_total
                print(f"{player}, you rolled {roll_total}.  Your turn score is {self.turn_score}.  Your total score before this turn was {self.player_scores[player]}.")



class Player:
    """
    Represents a player.  A player can have a strategy (in which case it is a computer) or not.
    In any case, a player should have the ability to choose to roll the dice.
    """

    def __init__(self, strategy=None):
        self.strategy = strategy

    def choose_to_roll(self, game):
        if game.turn_score < 30:
            return True
        return False


class Strategy:
    """
    Represents a strategy that a computer player can have.  This strategy should be able to look at a game state
    and determine whether or not to roll the dice without user input.
    """

    def __init__(self, hold_at = 20):
        self.hold_at = hold_at


class Die:
    """
    Represents a die.  Can specify how many sides the die has and what happens when you cast the die.
    """

    def __init__(self, sides = [1,2,3,4,5,6]):
        self.sides = sides

    def roll(self):
        return choice(self.sides)


if __name__ == "__main__":
    player1 = Player()
    player2 = Player(strategy=Strategy())
    players = [player1, player2]
    dice = [Die(sides=range(1, 7))]
    game = Game(players, dice)

    game.play_a_round()
