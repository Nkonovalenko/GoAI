import enum
from collections import namedtuple

class Player(enum.Enum):
	"""This class represents the player."""
	black = 1
	white = 2

	@property
	def other(self):
		return Player.black if self == Player.white else Player.white

class Point(namedtuple('Point', 'row col')):
	"""This class represents a point on the board."""
	# namedtuple allows us to access point.row and point.col
	# 	instead of point[0] and point[1]
	def neighbors(self):
		return [
			Point(self.row - 1, self.col),
			Point(self.row + 1, self.col),
			Point(self.row, self.col - 1),
			Point(self.row, self.col + 1),
		]