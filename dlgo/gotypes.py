import enum
from collections import namedtuple

class Player(enum.Enum):
	"""This class represents the player."""
	black = 1
	white = 2

	@property
	def other(self):
		return Player.black if self == Player.white else Player.white
