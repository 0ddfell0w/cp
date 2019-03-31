import bisect

from .card import Card, Rank, Suit
from .card_collection import CardCollection
from .hand import Hand


class Deck(CardCollection):

  @staticmethod
  def get_default_deck():
    """Get a 52 card deck in sorted order"""
    return Deck([Card(rank, suit)
                 for rank in Rank.VALID_RANKS
                 for suit in Suit.VALID_SUITS])

  def get_hands(self, num_hands, remove_cards=True):
    """get num_hands-many hands from the deck"""
    if remove_cards:
      self.remove_lowest_cards(len(self.cards) % num_hands)
    hands = [Hand([]) for _ in range(num_hands)]
    for idx, card in enumerate(self.cards):
      hand = hands[idx % num_hands]
      bisect.insort_left(hand.cards, card)
    return hands
