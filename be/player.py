class Player:

  def __init__(self, name, cards):
    self.name = name
    self.cards = cards

  def __repr__(self):
    return "<Player {}: ({})>".format(self.name, self.cards)

  def __eq__(self, other):
    return self.name == other.name and self.cards == other.cards

  def __hash__(self):
    return hash(tuple([self.name] + self.cards))

  def make_move(self, move_round):
    pass
