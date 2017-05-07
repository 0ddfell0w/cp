from card import Card

class CardCollection(object):
  def __init__(self, cards):
    self.cards = cards

  def __len__(self):
    return len(self.cards)

  def __ne__(self, other):
    if not isinstance(other, CardCollection):
      raise NotImplemented()  # TODO(Zack): helpful message? type error?
    return len(self) != len(other) or sorted(self.cards) != sorted(other.cards)

  def __eq__(self, other):
    if not isinstance(other, CardCollection):
      raise NotImplemented()  # TODO(Zack): helpful message? type error?
    return (len(self) == len(other) and
      sorted(self.cards) == sorted(other.cards))

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
