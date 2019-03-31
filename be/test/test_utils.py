import unittest
from functools import total_ordering

from .utils import CustomAssertions


class TestCustomAssertions(unittest.TestCase, CustomAssertions):
  @total_ordering
  class MockClass:

    def __init__(self, value): self.value = value

    def __repr__(self): return str(self.value)

    def __lt__(self, other): return self.value < other.value

    @staticmethod
    def from_string(value):
      return value

  def testassert_in_order_from_string(self):
    mocks = [self.MockClass(value) for value in [5, 6, 7]]
    self.assert_in_order_from_string(self.MockClass, mocks)

  def testassert_in_order_from_string_NotInOrder(self):
    mocks = [self.MockClass(value) for value in [8, 6, 7]]
    with self.assertRaises(AssertionError):
      self.assert_in_order_from_string(self.MockClass, mocks)


if __name__ == '__main__':
  unittest.main()
