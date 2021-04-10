from dlgo import agent
from dlgo.agent import naive
from dlgo import goboard_slow as goboard
from dlgo import gotypes
from dlgo.utils import print_board, print_move
import time

def main():
    """Main of bot versus bot match."""
    board_size = 9
    game = goboard.GameState.new_game(board_size)
    bots = {
        gotypes.Player.black: agent.naive.RandomBot(),
        gotypes.Player.white: agent.naive.RandomBot(),
    }
    while not game.is_over():
        # Set sleep timer so bot moves aren't printed too fast to observe
        time.sleep(0.3)

        # Before each move, clear the screen
        print(chr(27) + "[2J")
        print_board(game.board)
        bot_move = bots[game.next_player].select_move(game)
        print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)

if __name__ == '__main__':
    """Start main."""
    main()