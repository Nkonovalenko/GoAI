import enum
import random

from dlgo.agent import Agent

__all__ = [
    'MinimaxAgent',
]

class GameResult(enum.Enum):
    """Result of game."""
    loss = 1
    draw = 2
    win = 3

def reverse_game_result(game_result):
    """Reverse result for opponent."""
    if game_result == GameResult.loss:
        return game_result.win
    elif game_result == GameResult.win:
        return game_result.loss
    return GameResult.draw

def best_result(game_start):
    """Return the result."""
    if game_state.is_over():
        if game_state.winner() == game_state.next_player:
            return GameResult.win
        elif game_state.winner() is None:
            return GameResult.draw
        else:
            return GameResult.loss

    best_result_so_far = GameResult.loss

    for candidate_move in game_state.legal_moves():
        next_state = game_state.apply_move(candidate_move)
        opponent_best_result = best_result(next_state)
        our_result = reverse_game_result(opponent_best_result)
        if our_result.value > best_result_so_far.value:
            best_result_so_far = our_result
    return best_result_so_far

class MinimaxAgent(Agent):
    """Minimax Agent class."""
    def select_move(self, game_state):
        """Select a move using minimax."""
        winning_moves = []
        draw_moves = []
        losing_moves = []

        # loop through all the legal moves
        for possible_move in game_state.legal_moves():
            # Calculate state if we make the move
            next_state = game_state.apply_move(possible_move)
            # figure our opponent's next best outcome
            opponent_best_outcome = best_result(next_state)
            # Our outcome is opposite of the opponent's
            our_best_outcome = reverse_game_result(opponent_best_outcome)

            if our_best_outcome == GameResult.win:
                winning_moves.append(possible_move)
            elif our_best_outcome == GameResult.loss:
                losing_moves.append(possible_move)
            else:
                draw_moves.append(GameResult.draw)

        if winning_moves:
            return random.choice(winning_moves)
        if draw_moves:
            return random.choice(draw_moves)
        return random.choice(losing_moves)