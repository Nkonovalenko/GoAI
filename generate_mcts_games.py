import argparse
import numpy as np

from dlgo.encoders import get_encoder_by_name
from dlgo import goboard
from dlgo import mcts
from dlgo.utils import print_board, print_move
