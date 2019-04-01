import unittest

from ..round import Round
from ..player_move import PlayerMove
from ..card_collection import CardCollection
from ..player import Player
from .utils import CustomAssertions


class RoundTest(unittest.TestCase, CustomAssertions):

  # Valid first move
  def test_append_first_move_kind_move(self):
    player1 = Player("1", CardCollection.from_string("2S 2H 2C 2D 10S 10H 10C 10D"))
    rnd = Round.new([player1])
    rnd.append(PlayerMove.from_string(player1, "2S"))

  def test_append_first_move_poker_move(self):
    player1 = Player("1", CardCollection.from_string("2S 2H 2C 2D 10S 10H 10C 10D"))
    rnd = Round.new([player1])
    rnd.append(PlayerMove.from_string(player1, "2S 10S 10H 10C 10D"))

  # Invalid first move
  def test_append_first_move_kind_move_invalid_card(self):
    player1 = Player("1", CardCollection.from_string("2S 2H 2C 2D"))
    rnd = Round.new([player1])
    with self.assertRaises(ValueError) as e:
      rnd.append(PlayerMove.from_string(player1, "KH"))
    self.assertIn("does not have", str(e.exception))
    self.assertIn("KH", str(e.exception))

  def test_append_first_move_poker_move_invalid_card(self):
    player1 = Player("1", CardCollection.from_string("2S 2H 2C 2D 10S 10H 10C 10D"))
    rnd = Round.new([player1])
    with self.assertRaises(ValueError) as e:
      rnd.append(PlayerMove.from_string(player1, "3S 10S 10H 10C 10D"))
    self.assertIn("does not have", str(e.exception))
    self.assertIn("3S", str(e.exception))

  # Valid subsequent moves

  # Invalid subsequent moves
  def test_append_move_kind_move_invalid_card(self):
    player1 = Player("1", CardCollection.from_string("7H 7C 7D"))
    player2 = Player("2", CardCollection.from_string("8H 8C 8D"))
    rnd = Round(
      [player1, player2],
      [
        PlayerMove.from_string(player1, "7D")
      ])
    with self.assertRaises(ValueError) as e:
      rnd.append(PlayerMove.from_string(player2, "9H"))
    self.assertIn("does not have", str(e.exception))
    self.assertIn("9H", str(e.exception))

  def test_append_move_poker_move_invalid_card(self):
    player1 = Player("1", CardCollection.from_string("2S 2H 2C 2D 10S 10H 10C 10D"))
    player2 = Player("2", CardCollection.from_string("9S 9H 9C 9D JS JH JC JD"))
    rnd = Round(
      [player1, player2],
      [
        PlayerMove.from_string(player1, "10H 10C 10D 2H 2D")
      ])
    with self.assertRaises(ValueError) as e:
      rnd.append(PlayerMove.from_string(player2, "QH JS JH JC JD"))
    self.assertIn("does not have", str(e.exception))
    self.assertIn("QH", str(e.exception))

  # next, try to append a move of the wrong type.
  def test_append_move_kind_move_after_poker_move(self):
    player1 = Player("1", CardCollection.from_string("2S 2H 2C 2D 10S 10H 10C 10D 9H"))
    player2 = Player("2", CardCollection.from_string("9S 9H 9C 9D JS JH JC JD"))
    rnd = Round(
      [player1, player2],
      [
        PlayerMove.from_string(player1, "10D 10S 10H 10C 9H")
      ])
    with self.assertRaises(ValueError) as e:
      rnd.append(PlayerMove.from_string(player2, "JS JH JC"))
    self.assertIn("Expected PokerMove", str(e.exception))

  def test_append_move_poker_move_after_kind_move(self):
    player1 = Player("1", CardCollection.from_string("9S 9H 9C 9D JS JH JC JD"))
    player2 = Player("2", CardCollection.from_string("2S 2H 2C 2D 10S 10H 10C 10D"))
    rnd = Round(
      [player1, player2],
      [
        PlayerMove.from_string(player1, "JH JC JD")
      ])
    with self.assertRaises(ValueError) as e:
      rnd.append(PlayerMove.from_string(player2, "10H 10C 10D 2H 2D"))
    self.assertIn("Expected KindMove", str(e.exception))
