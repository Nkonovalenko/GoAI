import random
from dlgo.agent.base import Agent
from dlgo.agent.helpers import is_point_an_eye
from dlgo.goboard_slow import Move
from dlgo.gotypes import Point

class RandomBot(Agent):
    """Naive bot that makes random moves."""
    def select_move(self, game_state):
        """Choose a random valid move that preserves our own eyes."""
        candidates = []
        for r in range(1 , game_state.board.num_rows + 1):
            for c in range(1, game_state.board.num_cols + 1):
                candidate = Point(row=r, col=c)
                is_valid = game_state.is_valid_move(Move.play(candidate))
                is_eye = is_point_an_eye(game_state.board, candidate, 
                                         game_state.next_player)
                if is_valid and not is_eye: 
                    candidates.append(candidate)
        if not candidates:
            return Move.pass_turn()
        return Move.play(random.choice(candidates))
