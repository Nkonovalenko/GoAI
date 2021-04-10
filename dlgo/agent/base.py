class Agent:
    """Define the interface all bots will follow."""
    def __init__(self):
        """Initialize agent."""
        pass

    def select_move(self, game_state):
        """Select next move."""
        raise NotImplementedError()