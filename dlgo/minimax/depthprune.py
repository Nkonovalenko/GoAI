import random

from dlgo.agent import Agent
from dlgo.scoring import GameResult

__all__ = [
    'DepthPrunedAgent'
]

MAX_SCORE = 99999
MIN_SCORE = -99999

def reverse_game_result(game_result):
    """Our result is reverse of the opponent."""
    if game_result == GameResult.loss:
        return game_result.win
    if game_result == GameResult.win:
        return game_result.loss
    return game_result.draw

def best_result(game_state, max_depth, eval_fn):
    """Find the best result from all potential moves."""
    if game_state.is_over():
        if game_state.winner() == game_state.next_player:
            return MAX_SCORE
        else:
            return MIN_SCORE

    if max_depth == 0:
        return eval_fn(game_state)

    best_so_far = MIN_SCORE
    for candidate_move in game_state.legal_moves():
        next_state = game_state.apply_move(candidate_move)
        opponent_best_result = best_result(
            next_state, max_depth - 1, eval_fn)
        our_result = -1 * opponent_best_result
        if our_result > best_so_far:
            best_so_far = our_result

    return best_so_far

class DepthPrunedAgent(Agent):
    """Minimax Agent that has applied prunning."""
    def __init__(self, max_depth, eval_fn):
        """Initialize Agent."""
        Agent.__init__(self)
        self.max_depth = max_depth
        self.eval_fn = eval_fn

    def select_move(self, game_state):
        """Select the best move based on minimax."""
        best_moves = []
        best_score = None

        # Loop through all the legal moves
        for possible_move in game_state.legal_moves():
            # Calculate the game state if this move is applied
            next_state = game_state.apply_move(possible_move)
            # Figure out opponent's best move
            opponent_best_outcome = best_result(next_state, self.max_depth, self.eval_fn)
            # Our outcome is opposite the opponent
            our_best_outcome = -1 * opponent_best_outcome
            if (not best_moves) or our_best_outcome > best_score:
                # best move so far
                best_moves = [possible_move]
                best_score = our_best_outcome
            elif our_best_outcome == best_score:
                # as good as previous best
                best_moves.append(possible_move)
        # Randomly choose from all equally best moves
        return random.choice(best_moves)