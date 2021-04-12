import random
import math

from dlgo import agent
from dlgo.gotypes import Player
from dlgo.utils import coords_from_point

__all__ = [
    'MCTSAgent'
]

class MCTSNode(object):
    """Class to create Monte Carlo Tree Search Nodes."""
    
    def __init__(self, game_state, parent=None, move=None):
        """Initialize the node."""
        self.game_state = game_state
        self.parent = parent
        self.move = move
        self.win_counts = {
            Player.black: 0,
            Player.white: 0,
        }
        self.num_rollouts = 0
        self.children = []
        self.unvisited_moves = game_state.legal_moves()

    def add_random_child(self):
        """Add a random child node."""
        index = random.randint(0, len(self.unvisited_moves) - 1)
        new_move = self.unvisited_moves.pop(index)
        new_game_state = self.game_state.apply_move(new_move)
        new_node = MCTSNode(new_game_state, self, new_move)
        self.children.append(new_node)
        return new_node

    def record_win(self, winner):
        """Increment the win counter for position."""
        self.win_counts[winner] += 1
        self.num_rollouts += 1
