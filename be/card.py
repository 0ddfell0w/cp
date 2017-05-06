# coding: utf-8
'''
Dump of relevant classes for representing card collections (e.g. moves, hands, decks).
'''
import bisect
import random
from collections import Counter, defaultdict
from functools import total_ordering

class Suit(object):

  _D = DIAMONDS = 1
  _C = CLUBS = 2
  _H = HEARTS = 3
  _S = SPADES = 4

  VALID_SUITS = (DIAMONDS, CLUBS, HEARTS, SPADES)

  @staticmethod
  def from_string(string):
    return {
      "♦": Suit.DIAMONDS,
      "♣": Suit.CLUBS,
      "♥": Suit.HEARTS,
      "♠": Suit.SPADES,
      "D": Suit.DIAMONDS,
      "C": Suit.CLUBS,
      "H": Suit.HEARTS,
      "S": Suit.SPADES,
      "DIAMONDS": Suit.DIAMONDS,
      "CLUBS": Suit.CLUBS,
      "HEARTS": Suit.HEARTS,
      "SPADES": Suit.SPADES,
    }.get(str(string).upper())


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

  VALID_RANKS = (_3, _4, _5, _6, _7, _8, _9, _10, _J, _Q, _K, _A, _2)

  @staticmethod
  def from_string(string):
    return {
      "3": Rank.THREE,
      "4": Rank.FOUR,
      "5": Rank.FIVE,
      "6": Rank.SIX,
      "7": Rank.SEVEN,
      "8": Rank.EIGHT,
      "9": Rank.NINE,
      "10": Rank.TEN,
      "J": Rank.JACK,
      "Q": Rank.QUEEN,
      "K": Rank.KING,
      "A": Rank.ACE,
      "2": Rank.TWO,
    }.get(str(string).upper())

@total_ordering
class Card(object):

  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit

  @staticmethod
  def from_string(string):
    rankString, suitString = string[:-1], string[-1:]
    return Card(Rank.from_string(rankString), Suit.from_string(suitString))

  def _is_valid_operand(self, other):
      return (hasattr(other, "suit") and
              hasattr(other, "rank"))

  def __eq__(self, other):
      if not self._is_valid_operand(other):
          return NotImplemented
      return ((self.rank, self.suit) == (other.rank, other.suit))

  def __lt__(self, other):
      if not self._is_valid_operand(other):
          return NotImplemented
      return ((self.rank, self.suit) <
              (other.rank, other.suit))

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

  @classmethod
  def from_string(cls, string, delimiter=None):
    return cls([Card.from_string(sub) for sub in string.split(delimiter)])

  def shuffle(self):
    '''Shuffle cards in place'''
    self.cards = random.sample(self.cards, len(self.cards))

  def shuffled(self):
    self.shuffle()
    return self

  def sort(self):
    '''Sort cards in place'''
    self.cards.sort()

  def sorted(self):
    self.sort()
    return self

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
  def get_moves_of_len(length):
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
      self.is_four_of_a_kind,
      self.is_full_house,
    ])

  def is_straight(self):
    ranks = sorted([card.rank for card in self.cards])
    return all(x == y for x, y in enumerate(ranks, ranks[0]))

  def is_flush(self):
    suits = {card.suit for card in self.cards}
    return len(suits) == 1

  def is_straight_flush(self):
    return self.is_straight() and self.is_flush()

  def is_four_of_a_kind(self):
    rankToSuits = defaultdict(set)
    for card in self.cards:
      rankToSuits[card.rank].add(card.suit)
    lens = sorted(len(unique_suits) for unique_suits in rankToSuits.values())
    return lens == [1, 4]

  def is_full_house(self):
    rankToSuits = defaultdict(set)
    for card in self.cards:
      rankToSuits[card.rank].add(card.suit)
    lens = sorted(len(unique_suits) for unique_suits in rankToSuits.values())
    return lens == [2, 3]


@total_ordering
class KindMove(Move):

  def __init__(self, cards):
    if len(cards) not in [1, 2, 3]:
      raise ValueError("KindMoves must consist of 1, 2 or 3 cards.")
    num_unique_ranks = len({c.rank for c in cards})
    if num_unique_ranks != 1:
      raise ValueError("KindMoves must have one unique rank.")
    return super(KindMove, self).__init__(cards)

  def __le__(self, other):
    return (len(self.cards) == len(other.cards) and
      max(other.cards) >= max(self.cards))

  def __ge__(self, other):
    return (len(self.cards) == len(other.cards) and
      max(other.cards) <= max(self.cards))

  def __gt__(self, other):
    return (len(self.cards) == len(other.cards) and
      max(other.cards) < max(self.cards))

  def __lt__(self, other):
    return (len(self.cards) == len(other.cards) and
      max(other.cards) > max(self.cards))

  def __eq__(self, other):
    if len(self.cards) != len(other.cards):
      raise ValueError("Cannot compare different length KindMoves")
    return max(other.cards) == max(self.cards)

kms = sorted(map(KindMove.from_string,
        [
        "2c 2h 2s",
        "3c 3h 3s",
        "7h 7s 7c",
        ]))
