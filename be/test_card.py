import unittest
from collections import defaultdict

from card import Card, Deck, PokerMove, Rank, Suit

class CardTest(unittest.TestCase):
	def test_self_equality(self):
		for card in Deck.DefaultDeck():
			self.assertEquals(card, card,
				"{} != {} should be equal".format(card, card))


class DefaultDeckTest(unittest.TestCase):

	def test_size(self):
		self.assertEquals(52, len(Deck.DefaultDeck()),
			"52 != {}".format(len(Deck.DefaultDeck())))

	def test_composition(self):
		rankToSuits = defaultdict(set)
		for card in Deck.DefaultDeck():
			rankToSuits[card.rank].add(card.suit)
		lens = sorted(len(unique) for unique in rankToSuits.values())
		self.assertEquals([4]*13, lens,
			"{} != {}".format([4]*13, lens))

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
		self.assertEquals(
			[
				Card(Rank._5, Suit._C),
				Card(Rank._9, Suit._S),
				Card(Rank._2, Suit._D),
				Card(Rank._2, Suit._H),
			],
			sorted([
				Card(Rank._2, Suit._H),
				Card(Rank._9, Suit._S),
				Card(Rank._5, Suit._C),
				Card(Rank._2, Suit._D),
			]))


class PokerMoveTest(unittest.TestCase):

	def test_is_straight(self):
				straight = PokerMove([
					Card(Rank._3, "S"),
					Card(Rank._4, "S"),
					Card(Rank._5, "S"),
					Card(Rank._6, "S"),
					Card(Rank._7, "S"),
				])
				self.assertTrue(straight.is_straight())

	def test_is_flush(self):
				flush = PokerMove([
					Card(Rank._3, "S"),
					Card(Rank._J, "S"),
					Card(Rank._Q, "S"),
					Card(Rank._K, "S"),
					Card(Rank._7, "S"),
				])
				self.assertTrue(flush.is_flush())

	def test_is_straight_flush(self):
				straight_flush = PokerMove([
					Card(Rank._3, "S"),
					Card(Rank._4, "S"),
					Card(Rank._5, "S"),
					Card(Rank._6, "S"),
					Card(Rank._7, "S"),
				])
				self.assertTrue(straight_flush.is_straight_flush())

	def test_is_four_of_a_kind(self):
				foak = PokerMove([
					Card(Rank._3, "S"),
					Card(Rank._3, "H"),
					Card(Rank._3, "C"),
					Card(Rank._3, "D"),
					Card(Rank._7, "S"),
				])
				self.assertTrue(foak.is_four_of_a_kind())

	def test_is_full_house(self):
				full_house = PokerMove([
					Card(Rank._3, "S"),
					Card(Rank._3, "H"),
					Card(Rank._3, "C"),
					Card(Rank._7, "D"),
					Card(Rank._7, "C"),
				])
				self.assertTrue(full_house.is_full_house())

if __name__ == '__main__':
    unittest.main()
