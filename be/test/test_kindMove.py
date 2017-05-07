import unittest

from card import KindMove
from test.utils import CardCollectionUtils as cc_utils


class KindMoveTest(unittest.TestCase):

  def testOneOfAKind(self):
    cc_utils.assert_in_order_from_string(KindMove, ["3C", "4C"])

  def testTwoOfAKind(self):
    cc_utils.assert_in_order_from_string(KindMove, ["3C 3H", "4C 4H"])

  def testThreeOfAKind(self):
    cc_utils.assert_in_order_from_string(KindMove, ["3C 3H 3S", "4C 4H 4S"])

  def testFourOfAKind_invalid(self):
    with self.assertRaises(ValueError):
      cc_utils.assert_in_order_from_string(
        KindMove, ["3D 3C 3H 3S", "4D 4C 4H 4S"])

  def testFourOfAKind_validPokerMoveInvalidKindMove(self):
    with self.assertRaises(ValueError):
      cc_utils.assert_in_order_from_string(
        KindMove, ["3D 3C 3H 3S 5C", "4D 4C 4H 4S 5D"])

if __name__ == '__main__':
  unittest.main()
