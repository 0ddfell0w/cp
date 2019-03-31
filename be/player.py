class Player:

  def __init__(self, name, cards):
    self.name = name
    self.cards = cards

  def __repr__(self):
    return "{} ({})".format(self.name, self.cards)

  def make_move(self, move_round):
    pass
