import unittest

from ..card import Card
from ..deck import Deck


class CardTest(unittest.TestCase):
  def test_self_equality(self):
    for card in Deck.get_default_deck():
      self.assertEqual(card, Card(card.rank, card.suit),
                       "{} != {} should be equal".format(card, card))


class ValidRoundTest(unittest.TestCase):
  pass


if __name__ == '__main__':
  unittest.main()
