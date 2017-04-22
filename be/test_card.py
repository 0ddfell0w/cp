import unittest

from card import Card, Deck, Rank, Suit

class DeckTest(unittest.TestCase):

	def test_self_equality(self):
		for card in Deck.DefaultDeck():
			self.assertEquals(card, card,
				"{} != {} should be equal".format(card, card))

	def test_order_suits(self):
		for r in Rank.VALID_RANKS:
			self.assertLess(Card(r, Suit._D), Card(r, Suit._C))
			self.assertLess(Card(r, Suit._C), Card(r, Suit._H))
			self.assertLess(Card(r, Suit._H), Card(r, Suit._S))

	def test_order_ranks(self):
		for s in Suit.VALID_SUITS:
			self.assertTrue(
				Card(Rank._3, s) <
				Card(Rank._4, s) <
				Card(Rank._5, s) <
				Card(Rank._6, s) <
				Card(Rank._7, s) <
				Card(Rank._8, s) <
				Card(Rank._9, s) <
				Card(Rank._10, s) <
				Card(Rank._J, s) <
				Card(Rank._Q, s) <
				Card(Rank._K, s) <
				Card(Rank._A, s) <
				Card(Rank._2, s)
			)

class HandTest(unittest.TestCase):
	def testSorting(self):
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

if __name__ == '__main__':
    unittest.main()
