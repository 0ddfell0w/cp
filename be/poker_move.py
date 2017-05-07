from collections import defaultdict
from move import Move

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

