import unittest

from ..kind_move import KindMove
from .utils import CustomAssertions


class KindMoveTest(unittest.TestCase, CustomAssertions):

  def test_one_of_a_kind(self):
    self.assert_in_order_from_string(KindMove, ["3C", "4C"])

  def test_two_of_a_kind(self):
    self.assert_in_order_from_string(KindMove, ["3C 3H", "4C 4H"])

  def test_three_of_a_kind(self):
    self.assert_in_order_from_string(KindMove, ["3C 3H 3S", "4C 4H 4S"])

  def test_four_of_a_kind_invalid(self):
    self.assertInvalidKindMove("4D 4C 4H 4S")

  def test_four_of_a_kind_valid_poker_move_invalid_kind_move(self):
    self.assertInvalidKindMove("3D 3C 3H 3S 5C")

  def assertInvalidKindMove(self, move_string):
    self.assertFalse(KindMove.from_string(move_string).is_valid())


if __name__ == '__main__':
  unittest.main()
