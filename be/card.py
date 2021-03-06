# coding: utf-8
"""
Dump of relevant classes for representing card collections (e.g. moves, hands, decks).
"""
from __future__ import absolute_import, unicode_literals

from functools import total_ordering


class Suit:
  _D = DIAMONDS = 1
  _C = CLUBS = 2
  _H = HEARTS = 3
  _S = SPADES = 4

  VALID_SUITS = (DIAMONDS, CLUBS, HEARTS, SPADES)

  @staticmethod
  def from_string(string):
    return {
      "D": Suit.DIAMONDS,
      "C": Suit.CLUBS,
      "H": Suit.HEARTS,
      "S": Suit.SPADES,
      "♦": Suit.DIAMONDS,
      "♣": Suit.CLUBS,
      "♥": Suit.HEARTS,
      "♠": Suit.SPADES,
      "DIAMONDS": Suit.DIAMONDS,
      "CLUBS": Suit.CLUBS,
      "HEARTS": Suit.HEARTS,
      "SPADES": Suit.SPADES,
    }.get(str(string).upper())


class Rank:
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
class Card:

  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit

  @staticmethod
  def from_string(string):
    rank_string, suit_string = string[:-1], string[-1:]
    return Card(Rank.from_string(rank_string), Suit.from_string(suit_string))

  @staticmethod
  def _is_valid_operand(other):
    return (hasattr(other, "suit") and
            hasattr(other, "rank"))

  def __eq__(self, other):
    if not self._is_valid_operand(other):
      return NotImplemented
    return (self.rank, self.suit) == (other.rank, other.suit)

  def __hash__(self):
    return hash((self.rank, self.suit))

  def __lt__(self, other):
    if not self._is_valid_operand(other):
      return NotImplemented
    return ((self.rank, self.suit) <
            (other.rank, other.suit))

  def __repr__(self):
    return "{}{}".format(self.rank_string(), self.suit_string())

  def rank_string(self):
    if self.rank > 10:
      rank_string = "JQKA2"[self.rank - 11]
    else:
      rank_string = str(self.rank)
    return rank_string

  def suit_string(self):
    if self.suit == Suit.DIAMONDS:
      return "D"  # return "♦"
    elif self.suit == Suit.CLUBS:
      return "C"  # return "♣"
    elif self.suit == Suit.HEARTS:
      return "H"  # return "♥"
    elif self.suit == Suit.SPADES:
      return "S"  # return "♠"


Card.fs = Card.from_string
