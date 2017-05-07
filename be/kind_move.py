from move import Move
from functools import total_ordering

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
