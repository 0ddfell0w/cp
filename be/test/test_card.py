import unittest

from card import Card, Deck


class CardTest(unittest.TestCase):
  def test_self_equality(self):
    for card in Deck.DefaultDeck():
      self.assertEquals(card, Card(card.rank, card.suit),
        "{} != {} should be equal".format(card, card))

if __name__ == '__main__':
  unittest.main()
