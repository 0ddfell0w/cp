from functools import total_ordering
from collections import defaultdict

from .move import Move


@total_ordering
class PokerMove(Move):
  STRAIGHT_FLUSH = 5
  FOUR_OF_A_KIND = 4
  FULL_HOUSE = 3
  FLUSH = 2
  STRAIGHT = 1
  INVALID = 0

  def __init__(self, cards):
    super(PokerMove, self).__init__(cards)

  def __eq__(self, other):
    # not checking if it's valid for now
    return sorted(self.cards) == sorted(other.cards)

  def __lt__(self, other):
    strength = self.get_move_strength()
    other_strength = other.get_move_strength()
    if strength < other_strength:
      return True
    elif strength > other_strength:
      return False
    return sorted(self.cards, reverse=True) < sorted(other.cards, reverse=True)

  def get_move_strength(self):
    if not self.is_valid():
      return PokerMove.INVALID
    if self.is_straight_flush():
      return PokerMove.STRAIGHT_FLUSH
    elif self.is_four_of_a_kind():
      return PokerMove.FOUR_OF_A_KIND
    elif self.is_full_house():
      return PokerMove.FULL_HOUSE
    elif self.is_flush():
      return PokerMove.FLUSH
    elif self.is_straight():
      return PokerMove.STRAIGHT

  def is_valid(self):
    if len(self.cards) < 5:
      return False
    return any(check() for check in [
      self.is_straight,
      self.is_flush,
      self.is_full_house,
      self.is_four_of_a_kind,
      # self.is_straight_flush,
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
    rank_to_suits = defaultdict(set)
    for card in self.cards:
      rank_to_suits[card.rank].add(card.suit)
    lens = sorted(len(unique_suits) for unique_suits in rank_to_suits.values())
    return lens == [1, 4]

  def is_full_house(self):
    rank_to_suits = defaultdict(set)
    for card in self.cards:
      rank_to_suits[card.rank].add(card.suit)
    lens = sorted(len(unique_suits) for unique_suits in rank_to_suits.values())
    return lens == [2, 3]
