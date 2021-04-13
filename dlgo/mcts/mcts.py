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

    def can_add_child(self):
        """Check if any moves can still be made."""
        return len(self.unvisited_moves) > 0

    def is_terminal(self):
        """Check is game is over."""
        return self.game_state.is_over()

    def winning_frac(self, player):
        """Return the win rate of a position."""
        return float(self.win_counts[player]) / float(self.num_rollouts)

class MCTSAgent(agent.Agent):
    """Class for Monte Carlo Search Tree Agent."""

    def __init__(self, num_rounds, temperature):
        agent.Agent.__init__(self)
        self.num_rounds = num_rounds
        self.temperature = temperature

    def select_move(self, game_state):
        """Select next move."""
        root = MCTSNode(game_state)

        for i in range(self.num_rounds):
            node = root
            while (not node.can_add_child()) and (not node.is_terminal()):
                node = self.select_child(node)

            # Add new child node to tree
            if node.can_add_child():
                node = node.add_random_child()

            # simulate a random game
            winner = self.simulate_random_game(node.game_state)

            while node is not None:
                # propogate score back up tree
                node.record_win(winner)
                node = node.parent

        # select best move
        best_move = None
        best_pct = -1.0
        for child in root.children:
            child_pct = child.winning_frac(game_state.next_player)
            if child_pct > best_pct:
                best_pct = child_pct
                best_move = child.move

        return best_move

    def select_child(self, node):
        """Select a child using the upper confidence bound for trees (UCT)."""
        total_rollouts = sum(child.num_rollouts for child in node.children)
        log_rollouts = math.log(total_rollouts)

        best_score = -1
        best_chld = None

        # Loop through all children
        for child in node.children:
            # calculate UCT score
            win_pct = child.winning_frac(node.game_state.next_player)
            exploration_factor = math.sqrt(log_rollouts / child.num_rollouts)
            uct_score = win_pct + self.temperature * exploration_factor

            # check if this is best score
            if uct_score > best_score:
                best_score = uct_score
                best_child = child

        return best_child

    @staticmethod
    def simulate_random_game(game):
        """Simulate game using random bot."""
        bots = {
        Player.black: agent.RandomBot(),
        Player.white: agent.RandomBot(),
        }

        while not game.is_over():
            bot_move = bots[game.next_player].select_move(game)
            game = game.apply_move(bot_move)

        return game.winner()