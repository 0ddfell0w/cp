import unittest

from card import PokerMove


class PokerMoveTest(unittest.TestCase):

  def test_is_straight(self):
    straight = PokerMove.from_string("3S 4S 5S 6S 7S")
    self.assertTrue(straight.is_straight())

  def test_is_flush(self):
    flush = PokerMove.from_string("3S JS QS KS 7S")
    self.assertTrue(flush.is_flush())

  def test_is_straight_flush(self):
    straight_flush = PokerMove.from_string("3S 4S 5S 6S 7S")
    self.assertTrue(straight_flush.is_straight_flush())

  def test_is_four_of_a_kind(self):
    four_of_a_kind = PokerMove.from_string("3S 3H 3C 3D 7S")
    self.assertTrue(four_of_a_kind.is_four_of_a_kind())

  def test_is_full_house(self):
    full_house = PokerMove.from_string("3s 3h 3c 7d 7c")
    self.assertTrue(full_house.is_full_house())


if __name__ == '__main__':
  unittest.main()
