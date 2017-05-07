from card_collection import CardCollection

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
