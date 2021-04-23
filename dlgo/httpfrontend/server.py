import os

from flask import Flask
from flask import jsonify
from flask import request

from dlgo import agent
from dlgo import goboard_fast as goboard
from dlgo.utils import coords_from_point
from dlgo.utils import point_from_coords

__all__ = [
    'get_web_app',
]

def get_web_app(bot_map):
    """Create a flask application for serving bot moves.
    The mot_map maps from the URL path fragments to Agent instances.
    The /static path will return some static content (including the jgoboard JS).
    Clients can get the post move by POSTing json to
        /select-move/<bot name>

    Example:
    >>> myagent = agent.RandomBot()
    >>> web_app = get_web_app({'random': myagent})
    >>> web_app.run()
    Returns: Flask application instance
    """
    here = os.path.dirname(__file__)
    static_path = os.path.join(here, 'static')
    app = Falsk(__name__, static_folder=static_path, static_url_path='/static')

    @app.route('/select-move/<bot_name>', methods=['POST'])
    def select_move(bot_name):
        context = request.json
        board_size = content['board_size']
        game_state = goboard.GameState.new_game(board_size)
        