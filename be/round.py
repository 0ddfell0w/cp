from .move_factory import get_move, get_move_type


class Round:
  def __init__(self, players, player_moves):
    self.players = players
    self.player_moves = player_moves
    self.move_type = get_move_type(player_moves[0].move) if player_moves else None

  @staticmethod
  def new(players):
    return Round(players, [])

  def next_player(self):
    """
    :return: next player to move, or None if the round is over.
    """
    if not self.player_moves:
      return self.players[0] if self.players else None
    next_player_idx = (self.players.index(self.player_moves[-1].player) + 1) % len(self.players)
    pivoted = self.players[next_player_idx:] + self.players[:next_player_idx]
    try:
      player = next(player for player in pivoted if player.cards)
    except StopIteration:
      return None
    return player if player != self.player_moves[-1].player else None

  def append(self, player_move):
    if not self.player_moves:
      if player_move.move.cards:
        self.move_type = get_move_type(player_move.move)
        return self.player_moves.append(player_move)

    last_move = self.player_moves[-1].move
    if get_move_type(player_move.move) != self.move_type:
      raise ValueError("Expected {}, but got {}".format(self.move_type.__name__, player_move.move))
    if player_move.move <= last_move:
      raise ValueError("{} is not a stronger move than {}".format(player_move, last_move))
    self.player_moves.append(player_move)
