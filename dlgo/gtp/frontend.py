from __future__ import absolute_import

import sys

from dlgo.gtp import command, response
from dlgo.gtp.board import gtp_position_to_coords, coords_to_gtp_position
from dlgo.goboard_fast import GameState, Move
from dlgo.agent.termination import TerminationAgent
from dlgo.utils import print_board


__all__ = [
    'GTPFrontend',
]


"""Go Text Protocol frontend for a bot.
Handles parsing GTP commands and formatting responses.
Only supports 19x19 boards and fixed handicaps.
"""