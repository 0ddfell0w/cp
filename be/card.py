# coding: utf-8
'''
Dump of relevant classes for representing card collections (e.g. moves, hands, decks).
'''
import random
import bisect
from collections import Counter


class Suit(object):

	_D = DIAMONDS = 1
	_C = CLUBS = 2
	_H = HEARTS = 3
	_S = SPADES = 4

	VALID_SUITS = (DIAMONDS, CLUBS, HEARTS, SPADES)


class Rank(object):
	_3 = THREE = 3
	_4 = FOUR = 4
	_5 = FIVE = 5
	_6 = SIX = 6
	_7 = SEVEN = 7
	_8 = EIGHT = 8
	_9 = NINE = 9
	_10 = TEN = 10
	_J = JACK = 11
	_Q = QUEEN = 12
	_K = KING = 13
	_A = ACE = 14
	_2 = TWO = 15

	VALID_RANKS = (
		THREE,
		FOUR,
		FIVE,
		SIX,
		SEVEN,
		EIGHT,
		NINE,
		TEN,
		JACK,
		QUEEN,
		KING,
		ACE,
		TWO,
	)


class Card(object):

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def __repr__(self):
		return "{}{}".format(self.rankString(), self.suitString())

	def __repr__(self):
		return "{}{}".format(self.rankString(), self.suitString())

	def rankString(self):
		if self.rank > 10:
			rankString = "JQKA2"[self.rank - 11]
		else:
			rankString = str(self.rank)
		return rankString

	def suitString(self):
		# TODO(Zack): Replace with unicode characters
		if self.suit == Suit.DIAMONDS:
			return "♦"
		elif self.suit == Suit.CLUBS:
			return "♣"
		elif self.suit == Suit.HEARTS:
			return "♥"
		elif self.suit == Suit.SPADES:
			return "♠"

	def __cmp__(self, other):
		if not isinstance(other, Card):
			raise TypeError("Cannot compare Card with {}".format(type(other)))
		if self.rank > other.rank:
			ret = 1
		elif self.rank < other.rank:
			ret = -1
		else:
			if self.suit > other.suit:
				ret = 1
			elif self.suit < other.suit:
				ret = -1
			else:
				ret = 0
		return ret

class CardCollection(object):
	def __init__(self, cards):
		self.cards = cards

	def __len__(self):
		return len(self.cards)

	def __repr__(self):
		return "<{} ({}) {}>".format(
			type(self).__name__, len(self), self.cards)

	def __iter__(self):
		return iter(self.cards)

	def __contains__(self, x):
		return x in self.cards

	def shuffle(self):
		'''Shuffle cards in place'''
		self.cards = random.sample(self.cards, len(self.cards))

	def by_rank(self):
		return sorted(self.cards)

	def remove_lowest_cards(self, n):
		if not n:
			return
		card_to_score = {card: idx
			for idx, card in enumerate(sorted(self.cards))}
		self.cards = [card for card in self.cards if card_to_score[card] >= n]


class Deck(CardCollection):

	@staticmethod
	def DefaultDeck():
		'''Get a 52 card deck in sorted order'''
		return Deck([Card(rank, suit)
		for rank in Rank.VALID_RANKS
		for suit in Suit.VALID_SUITS])


	def get_hands(self, num_hands, remove_cards=True):
		'''get num_hands-many hands from the deck'''
		if remove_cards:
			self.remove_lowest_cards(len(self.cards) % num_hands)
		hands = [Hand([]) for _ in range(num_hands)]
		for idx, card in enumerate(self.cards):
			hand = hands[idx % num_hands]
			bisect.insort_left(hand.cards, card)
		return hands


class Hand(CardCollection):
	pass


class Move(CardCollection):
	def __init__(self, cards):
		if not (0 <= len(cards) <= 5):
			raise ValueError(
				"Moves must have between 0 and 5 cards, inclusive")
		super(Move, self).__init__(cards)


	def __cmp__(self, other):
		if len(self.cards) != len(other.cards):
			return -1
		# TODO(Danna): finish this


class PokerMove(Move):

	def __init__(self, cards):
		if len(cards) != 5:
			raise ValueError("Poker hands must consist of five cards.")
		return super(PokerMove, self).__init__(cards)

	def is_valid(self):
		if len(self.cards) < 5:
			return False
		return any(check() for check in [
			self.is_straight,
			self.is_flush,
			self.is_four_of_kind,
			self.is_full_house,
		])

	def is_straight(self):
		ranks = sorted([card.rank for card in self.cards])
		return all(x == y for x, y in enumerate(ranks, ranks[0]))


	def is_flush(self):
		pass


	def is_four_of_kind(self):
		pass


	def is_full_house(self):
		pass


# TODO(Zack): Wiki says that Kind moves can't be 4 cards, 4 of a kinds must include a 5th card
class KindMoves(Move):
	def is_valid(self):
		num_unique_ranks = len({c.rank for c in self.cards})
		return num_unique_ranks == 1
