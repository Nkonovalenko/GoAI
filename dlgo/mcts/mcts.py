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

