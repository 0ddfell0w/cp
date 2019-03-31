import unittest

from ..poker_move import PokerMove
from .utils import CustomAssertions

INVALID = "3S 4S 5S 6S 2H"
STRAIGHT = "3S 4C 5D 6S 7H"
FLUSH = "3S JS QS KS 7S"
FULL_HOUSE = "3S 3H 3C 7D 7C"
FOUR_OF_A_KIND = "3S 3H 3C 3D 7S"
STRAIGHT_FLUSH = "7H 6H 5H 4H 3H"


class PokerMoveTest(unittest.TestCase, CustomAssertions):

  def test_is_straight(self):
    self.assertTrue(PokerMove.from_string(STRAIGHT).is_straight())

  def test_is_flush(self):
    self.assertTrue(PokerMove.from_string(FLUSH).is_flush())

  def test_is_straight_flush(self):
    self.assertTrue(PokerMove.from_string(STRAIGHT_FLUSH).is_straight_flush())

  def test_is_four_of_a_kind(self):
    self.assertTrue(PokerMove.from_string(FOUR_OF_A_KIND).is_four_of_a_kind())

  def test_is_full_house(self):
    self.assertTrue(PokerMove.from_string(FULL_HOUSE).is_full_house())

  # Ordering
  def testMoveStrengthOrdering(self):
    self.assert_in_order_from_string(PokerMove, [
      INVALID,
      STRAIGHT,
      FLUSH,
      FULL_HOUSE,
      FOUR_OF_A_KIND,
      STRAIGHT_FLUSH,
    ])

  # Intra-move-strength ordering
  def test_straight_ordering_highest_card_wins(self):
    self.assert_in_order_from_string(PokerMove, ["3S 4C 5D 6S 7H", "3S 4C 5D 6S 7S"])

  def test_straight_ordering_second_highest_card_wins(self):
    self.assert_in_order_from_string(PokerMove, ["3S 4C 5D 6C 7H", "3S 4C 5D 6S 7H"])

  def test_straight_ordering_with_two(self):
    self.assert_in_order_from_string(PokerMove, ["9S 10D JC QD KS", "JC QD KS AD 2H"])

  def test_straight_ordering_with_two_suit_wins(self):
    self.assert_in_order_from_string(PokerMove, ["JC QD KS AD 2D", "JC QD KS AD 2H"])

  def test_flush(self):
    self.assertTrue(PokerMove.from_string(FLUSH).is_flush())

  def test_straight_flush(self):
    self.assertTrue(PokerMove.from_string(STRAIGHT_FLUSH).is_straight_flush())

  def test_four_of_a_kind(self):
    self.assertTrue(PokerMove.from_string(FOUR_OF_A_KIND).is_four_of_a_kind())

  def test_full_house(self):
    self.assertTrue(PokerMove.from_string(FULL_HOUSE).is_full_house())


if __name__ == '__main__':
  unittest.main()
