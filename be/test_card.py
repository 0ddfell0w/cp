import unittest
from collections import defaultdict
from functools import total_ordering

from card import Card
from deck import Deck
from test.utils import CardCollectionUtils


class CardTest(unittest.TestCase):
  def test_self_equality(self):
    for card in Deck.DefaultDeck():
      self.assertEquals(card, Card(card.rank, card.suit),
        "{} != {} should be equal".format(card, card))

class ValidRoundTest(unittest.TestCase):
  pass


if __name__ == '__main__':
  unittest.main()
