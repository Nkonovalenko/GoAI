import copy
from dlgo.gotypes import Player

class Move():
	"""Class handling any action a player can play."""
	def __init__(self, point=None, is_pass=False, is_resign=False):
		"""Initilize object."""
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
