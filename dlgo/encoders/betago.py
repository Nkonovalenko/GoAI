import numpy as np

from dlgo.encoders.base import Encoder
from dlgo.goboard import Move, Point

class BetaGoEncoder(Encoder):
    """7 plane encoder as used in betago."""
    def __init__(self, board_size):
        self.board_width, self.board_height = board_size
        # 0 - 2. our stone with 1, 2, 3+ liberties
        # 3 - 5. opponent stone with 1, 2, 3+ liberties
        # 6. move would be illegal due to ko
        self.num_planes = 7