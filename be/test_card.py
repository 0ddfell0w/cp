import unittest
from collections import defaultdict

from card import Card, Deck, KindMove, PokerMove, Rank, Suit


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
				straight = PokerMove.from_string("3S 4S 5S 6S 7S")
				self.assertTrue(straight.is_straight())

	def test_is_flush(self):
				flush = PokerMove.from_string("3S JS QS KS 7S")
				self.assertTrue(flush.is_flush())

	def test_is_straight_flush(self):
				straight_flush = PokerMove.from_string("3S 4S 5S 6S 7S")
				self.assertTrue(straight_flush.is_straight_flush())

	def test_is_four_of_a_kind(self):
				four_of_a_kind = PokerMove.from_string("3S 3H 3C 3D 7S")
				self.assertTrue(four_of_a_kind.is_four_of_a_kind())

	def test_is_full_house(self):
				full_house = PokerMove.from_string("3s 3h 3c 7d 7c")
				self.assertTrue(full_house.is_full_house())


class KindMoveTest(unittest.TestCase):

	def test_kind_moves(self):
		for card in Deck.DefaultDeck():
			self.assertTrue(KindMove([card]).is_valid())

	def test_2_of_kind(self):
		for rank in Rank.VALID_RANKS:
			self.assertTrue(all((
				KindMove([Card(rank, Suit._D), Card(rank, Suit._H)]).is_valid(),
				KindMove([Card(rank, Suit._H), Card(rank, Suit._C)]).is_valid(),
				KindMove([Card(rank, Suit._C), Card(rank, Suit._S)]).is_valid(),
				KindMove([Card(rank, Suit._S), Card(rank, Suit._H)]).is_valid(),
			)))

	def test_2_of_kind(self):
		for rank in Rank.VALID_RANKS:
			self.assertTrue(all((
				KindMove([Card(rank, Suit._D), Card(rank, Suit._H)]).is_valid(),
				KindMove([Card(rank, Suit._H), Card(rank, Suit._C)]).is_valid(),
				KindMove([Card(rank, Suit._C), Card(rank, Suit._S)]).is_valid(),
				KindMove([Card(rank, Suit._S), Card(rank, Suit._H)]).is_valid(),
			)))


if __name__ == '__main__':
    unittest.main()
