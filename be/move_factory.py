from .kind_move import KindMove
from .poker_move import PokerMove


def get_move_type(move):
  if type(move) == KindMove:
    return KindMove
  elif type(move) == PokerMove:
    return PokerMove
  raise ValueError("{} is invalid. Must be a PokerMove or KindMove".format(move))


def get_move(cards):
  poker_move = PokerMove(cards)
  if poker_move.is_valid():
    return poker_move
  kind_move = KindMove(cards)
  if kind_move.is_valid():
    return kind_move
  raise ValueError("{} is not a valid PokerMove or KindMove".format(cards))
