import importlib

__all__ = [
    'Encoder',
    'get_encoder_by_name',
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

def get_encoder_by_name(name, board_size):
    """Create encoder instances by referencing name."""
    if isinstance(board_size, int):
        board_size = (board_size, board_size)
    module = importlib.import_module('dlgo.encoders.' + name)
    constructor = getattr(module, 'create')
    return constructor(board_size)