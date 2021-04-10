import copy
from dlgo.gotypes import Player

class Move():
    """Class handling any action a player can play."""
    def __init__(self, point=None, is_pass=False, is_resign=False):
        """Initilize a move."""
        assert (point is nont None) ^ is_pass ^ is_resign
        self.point = point
        self.is_play = (self.point is not None)
        self.is_pass = is_pass
        self.is_resign = is_resign

    @classmethod
    def play(cls, point):
        """This move places a stone on the board."""
        return Move(point=point)

    @classmethod
    def pass_turn(cls):
        """This move passes."""
        return Move(is_pass=True)

    @classmethod
    def resign(cls):
        """This move resigns the current game."""
        return Move(is_resign=True)

class GoString():
    """A chain of connected stones of the same color."""
    def __init__(self, color, stones, liberties):
        """Initilize a GoString."""
        self.color = color
        self.stones = set(stones)
        self.liberties = set(liberties)

    def remove_liberty(self, point):
        """Remove a liberty."""
        self.liberties.remove(point)

    def add_liberty(self, point):
        """Add a liberty."""
        self.liberties.add(point)

    def merged_with(self, go_string):
        """Retrun a new GoString containing all stones in both strings."""
        assert go_string.color == self.color
        combined_stones = self.stones | go_string.stones
        return GoString(
            self.color, combined_stones,
            (self.liberties | go_string.liberties) - combined_stones)

    @property
    def num_liberties(self):
        """Return the number of liberties."""
        return len(self.liberties)

    def __eq__(self, other):
        """Check if both GoStrings are the same."""
        return isinstance(other, GoString) and \
            self.color == other.color and \
            self.stones == other.stones and \
            self.liberties == other.liberties