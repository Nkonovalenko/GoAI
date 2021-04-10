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

class Board():
    """Handle Board object."""
    def __init__(selfl, num_rows, num_cols):
        """Initialize an empty grid with specified rows and cols."""
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._grid = {}

    def place_stone(self, player, point):
        """Place stone after inspecting if given point has liberties."""
        # Define variables
        assert self.is_on_grid(point)
        assert self._grid.get(point) is None
        adjecent_same_color = []
        adjacent_opposite_color = []
        liberties = []

        # Check neighbors and add to lists
        for neighbor in point.neighbors():
            if not self.is_on_grid(neighbor):
                # Check if invalid point
                continue
            neighbor_string = self._grid.get(neighbor)
            if neighbor_string is None:
                liberties.append(neighbor)
            elif neighbor_string.color == player:
                if neighbor_string not in adjecent_same_color:
                    adjecent_same_color.append(neighbor_string)
            else:
                if neighbor_string not in adjacent_opposite_color:
                    adjacent_opposite_color.append(neighbor_string)
        new_string = GoString(player, [point], liberties)

        # Merge any adjacent strings of the same color and add to grid
        for adjecent_same_color in adjecent_same_color:
            new_string = new_string.merged_with(adjecent_same_color)
        for new_string_point in new_string.stones:
            self._grid[new_string_point] = new_string

        # Reduce liberties of any adjacent strings of opposite color
        for other_color_string in adjacent_opposite_color:
            other_color_string.remove_liberty(point)

        # Remove any opposite-color strings with zero liberties
        for other_color_string in adjacent_opposite_color:
            if other_color_string.num_liberties == 0:
                self._remove_string(other_color_string)

    def is_on_grid(self, point):
        """Check if given point is on the grid."""
        return 1 <= point.row <= self.num_rows and \
            1 <= point.col <= self.num_cols

    def get(self, point):
        """Return the content of a point on the board."""
        string = self._grid.get(point)
        if string is None:
            return None
        return string.color

    def get_go_string(self, point):
        """Return entire string of stones at a point."""
        string = self._grid.get(point)
        if string is None:
            return None
        return string

    def _remove_string(self, string):
        """Check if removing string creates liberties."""
        for point in string.stones:
            for neighbor in point.neighbors():
                neighbor_string = self._grid.get(neighbor)
                if neighbor_string is None:
                    continue
                if neighbor_string is not string:
                    neighbor_string.add_liberty(point)
            self._grid[point] = None

class GameState():
    """Handle the state of the game."""
    def __init__(self, board, next_player, previous, move):
        """Initialize game state,"""
        self.board = board
        self.next_player = next_player
        self.previous_state = previous
        self.last_move = move

    def apply_move(self, move):
        """Return the new GameState after applying the move."""
        if move.is_play:
            next_board = copy.deepcopy(self.board)
            next_board.place_stone(self.next_player, move.point)
        else:
            next_board = self.board
        return GameState(next_board, self.next_player.other, self, move)

    @classmethod
    def new_game(cls, board_size):
        """Return GameState for new game."""
        if isinstance(board_size, int):
            board_size = (board_size, board_size)
        board = Board(*board_size)
        return GameState(board, Player.black, None, None)

    def is_over(self):
        """Determine when game is over."""
        if self.last_move is None:
            return False
        if self.last_move.is_resign:
            return True
        second_last_move = self.previous_state.last_move
        if second_last_move is None:
            return False
        return self.last_move.is_pass and second_last_move.is_pass