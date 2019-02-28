import pytest
from pig import Player, Game, Strategy, Die


player1 = Player()
player2 = Player(strategy=Strategy())
players = [player1, player2]
dice = [Die(sides=range(1, 7))]
game = Game(players, dice)


def test_initiate_game():
    for player in game.player_scores:
        assert game.player_scores[player] == 0

def test_choose_to_roll():
    assert player2.choose_to_roll(game)

