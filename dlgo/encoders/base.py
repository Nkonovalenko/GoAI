import importlib

__all__ = [
    'Encoder',
]

class Encoder:
    """Generic encoder class template."""

    def name(self):
        """Will allow us to save the name of encoder we are using."""
        raise NotImplementedError()

    def encode(self, game_state):
        """Turn GoBoard into numeric data."""
        raise NotImplementedError()

    def encode_point(self, point):
        """Turn GoBoard Point into integer index."""
        raise NotImplementedError()

    def decode_point_index(self, index):
        """Turn integer index back into a GoBoard point."""
        raise NotImplementedError()

    def num_points(self):
        """Number of points on the board (width * height)."""
        raise NotImplementedError()

    def shape(self):
        """Return shape of encoded board structure."""
        raise NotImplementedError()