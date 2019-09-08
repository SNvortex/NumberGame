from flask import Blueprint
from flask_restful import Api
from game.routes import GameResources
from .routes import PlayGame

game = Blueprint('game', __name__)
game_api = Api(game)
game_api.add_resource(GameResources, '/games')
game_api.add_resource(PlayGame, '/play_game/<int:game_id>')
