from move import Move
from functools import total_ordering

@total_ordering
class KindMove(Move):

  def __init__(self, cards):
    return super(KindMove, self).__init__(self.cards)

  def is_valid(self):
    if len(self.cards) not in [1, 2, 3]:
        return False
    num_unique_ranks = len({c.rank for c in self.cards})
    return num_unique_ranks == 1

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
