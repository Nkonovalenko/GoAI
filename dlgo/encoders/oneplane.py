import numpy as np

from dlgo.encoders.base import Encoder
from dlgo.goboard import Point

class OnePlaneEncoder(Encoder):
    """Encoder that will turn GoBoard into matrix the same shape as board."""

    def __init__(self, board_size):
        """Initialize encoder."""
        self.board_width, self.board_height = board_size
        self.num_planes = 1

    def name(self):
        """Return name."""
        return 'oneplane'

    def encode(self, game_state):
        """Fill with 1 if player's stone, -1 if opponent's stone."""
        board_matrix = np.zeros(self.shape())
        next_player = game_state.next_player
        for r in range(self.board_height):
            for c in range(self.board_width):
                p = Point(row=r + 1, col=c + 1)
                go_string = game_state.board.get_go_string(p)
                if go_string is None:
                    continue
                if go_string.color == next_player:
                    board_matrix[0, r, c] = 1
                else:
                    board_matrx[0, r, c] = -1
        return board_matrix

    def encode_point(self, point):
        """Encode a single point."""
        return self.board_width * (point.row - 1) + (point.col - 1)

    def decode_point_index(self, index):
        """Decode index into point on board."""
        row = index // self.board_width
        col = index % self.board_width
        return Point(row=r + 1, col=c + 1)

    def num_points(self):
        """Return number of points on board."""
        return self.board_height * self.board_width

    def shape(self):
        """Return shape of encoder."""
        return self.num_planes, self.board_height, self.board_width

def create(board_size):
    return OnePlaneEncoder(board_size)