from __future__ import absolute_import, unicode_literals

import unittest

from ..card import Card, Rank, Suit
from ..deck import Deck
from ..hand import Hand


class DeckTest(unittest.TestCase):

  def test_self_equality(self):
    self.assertEqual(Deck([]), Deck([]),
                     "{} != {}".format(Deck([]), Deck([])))


class DefaultDeckTest(unittest.TestCase):

  def test_size(self):
    self.assertEqual(52, len(Deck.get_default_deck()),
                     "52 != {}".format(len(Deck.get_default_deck())))

  def test_composition(self):
    expected_deck = Deck.from_string(
      ('3D 3C 3H 3S 4D 4C 4H 4S 5D 5C 5H 5S 6D 6C 6H 6S 7D 7C 7H 7S'
       ' 8D 8C 8H 8S 9D 9C 9H 9S 10D 10C 10H 10S JD JC JH JS'
       ' QD QC QH QS KD KC KH KS AD AC AH AS 2D 2C 2H 2S'))
    self.assertEqual(expected_deck, Deck.get_default_deck(),
                     "{} != {}".format("Default deck", Deck.get_default_deck()))

  def test_order_suits(self):
    for r in Rank.VALID_RANKS:
      self.assertLess(Card(r, Suit._D), Card(r, Suit._C))
      self.assertLess(Card(r, Suit._C), Card(r, Suit._H))
      self.assertLess(Card(r, Suit._H), Card(r, Suit._S))

  def test_order_ranks(self):
    for s in Suit.VALID_SUITS:
      self.assertTrue(
        Card(Rank._3, s) < Card(Rank._4, s) < Card(Rank._5, s) <
        Card(Rank._6, s) < Card(Rank._7, s) < Card(Rank._8, s) <
        Card(Rank._9, s) < Card(Rank._10, s) < Card(Rank._J, s) <
        Card(Rank._Q, s) < Card(Rank._K, s) < Card(Rank._A, s) <
        Card(Rank._2, s))

  def test_sorting(self):
    self.assertEqual(Hand.from_string("5C 9S 2D 2H").cards,
                     Hand.from_string("2H 9S 5C 2D").sorted().cards)

  def test_get_hands_3_players_3D_excluded(self):
    d = Deck.get_default_deck().get_hands(3)
    hands = d.get_hands(3)
    diff = list(set(d.cards) - set(card for hand in hands for card in hand))
    self.assertEqual(diff[0], Card.from_string("3D"))

  def test_get_hands_shuffled_3_players_3D_excluded(self):
    d = Deck.get_default_deck()
    d.shuffle()
    hands = d.get_hands(3)
    diff = list(set(d.cards) - set(card for hand in hands for card in hand))
    self.assertEqual(diff[0], Card.from_string("3D"))


if __name__ == '__main__':
  unittest.main()
