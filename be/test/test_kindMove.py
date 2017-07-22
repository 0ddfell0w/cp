import unittest

from kind_move import KindMove
from test.utils import CardCollectionUtils as cc_utils


class KindMoveTest(unittest.TestCase):

  def assertInvalidKindMove(self, move_string):
    self.assertFalse(KindMove.from_string(move_string).is_valid())

  def testOneOfAKind(self):
    cc_utils.assert_in_order_from_string(KindMove, ["3C", "4C"])

  def testTwoOfAKind(self):
    cc_utils.assert_in_order_from_string(KindMove, ["3C 3H", "4C 4H"])

  def testThreeOfAKind(self):
    cc_utils.assert_in_order_from_string(KindMove, ["3C 3H 3S", "4C 4H 4S"])

  def testFourOfAKind_invalid(self):
    self.assertInvalidKindMove("4D 4C 4H 4S")

  def testFourOfAKind_validPokerMoveInvalidKindMove(self):
    self.assertInvalidKindMove("3D 3C 3H 3S 5C")

if __name__ == '__main__':
  unittest.main()
