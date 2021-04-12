import random

from dlgo.agent import Agent
from dlgo.gotypes import Player

__all__ = [
    'AlphaBetaAgent'
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
        opponent_best_result = alpha_beta_result(
            next_state, max_depth - 1, best_black, best_white, eval_fn)
        our_result = -1 *  opponent_best_result
        if our_result > best_so_far:
            best_so_far = our_result

        # Update benchmark for white
        if game_state.next_player == Player.white:
            if best_so_far > best_white:
                outcome_for_black = -1 * best_so_far
                if outcome_for_black < best_black:
                    return best_so_far
        # Update benchmark for black
        elif game_state.next_player == Player.black:
            if best_so_far > best_black:
                outcome_for_white = -1 * best_so_far
                if outcome_for_white < best_white:
                    return best_so_far
    return best_so_far

class AlphaBetaAgent(Agent):
    """Create agent that uses alpha beta pruning."""
    def __init__(self, max_depth, eval_fn):
        """Initialize the agent."""
        Agent.__init__(self)
        self.max_depth = max_depth
        self.eval_fn = eval_fn

    def select_move(self, game_state):
        """Select a move based on Alpha/Beta Minimax."""
        best_moves = []
        best_score = None
        best_black = MIN_SCORE
        best_white = MAX_SCORE

        # Loop through all legal moves
        print("Legal Moves: ", len(game_state.legal_moves()))
        ctr = 0
        for possible_move in game_state.legal_moves():
            print("Considering move: ", ctr)
            ctr += 1
            next_state = game_state.apply_move(possible_move)
            opponent_best_outcome = alpha_beta_result(
                next_state, self.max_depth, best_black, best_white, self.eval_fn)

            our_best_outcome = -1 * opponent_best_outcome
            if (not best_moves) or our_best_outcome > best_score:
                # best move so far
                best_moves = [possible_move]
                best_score = our_best_outcome
                if game_state.next_player == Player.black:
                    best_black = best_score
                elif game_state.next_player == Player.white:
                    best_white = best_score
            elif our_best_outcome == best_score:
                # as good as previous best move
                best_moves.append(possible_move)

        # Choose random move from best moves
        return random.choice(best_moves)