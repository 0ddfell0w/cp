from .card_collection import CardCollection
from .move_factory import get_move


class PlayerMove:
  def __init__(self, player, move):
    self.player = player
    self.move = move

  def __repr__(self):
    return "<PM {}: {}>".format(self.player.name, self.move.cards)

  @staticmethod
  def from_string(player, string):
    cards = CardCollection.from_string(string)
    invalid_cards_for_player = set(cards) - set(player.cards)
    if invalid_cards_for_player:
      raise ValueError(
        "Player {} does not have {} in their hand".format(
          player, ",".join(map(str, invalid_cards_for_player))))

    return PlayerMove(player, get_move(cards))
