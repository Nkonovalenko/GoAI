import random

from dlgo.agent import Agent
from dlgo.scoring import GameResult

__all__ = [
    'AlphaBeta'
]

MAX_SCORE = 99999
MIN_SCORE = -99999

def reverse_game_result(game_result):
    """Our result is the reverse of the opponent."""
    if game_result == GameResult.loss:
        return game_result.win
    if game_result == GameResult.win:
        return game_result.loss
    return game_result.draw

def alpha_beta_result(game_state, max_depth, best_black, best_white, eval_fn):
    """Alpha Beta pruning function."""
    if game_state.is_over():
        if game_state.winner() == game_state.next_player:
            return MAX_SCORE
        else:
            return MIN_SCORE

        # Reached max depth, use heuristic to check how good sequence is
        if max_depth == 0:
            return eval_fn(game_state)

        best_so_far = MIN_SCORE
        for candidate_move in game_state.legal_moves():
            next_state = game_state.apply_move(candidate_move)