from flask import Blueprint, render_template, request, make_response,jsonify
from application.models.model import *

bp_game = Blueprint('bp_game', __name__)
tic_tac_toe = TicTacToe()


@bp_game.route('/new', methods=['POST'])
def create_game():
    game = tic_tac_toe.create_game()
    return jsonify({'game_id': game['id']}), 201


@bp_game.route('/<int:game_id>/moves', methods=['POST'])
def make_move(game_id):
    data = request.json
    x = data.get('x')
    y = data.get('y')
    result, status_code = tic_tac_toe.make_move(game_id, x, y)
    return jsonify(result), status_code


@bp_game.route('/<int:game_id>/moves', methods=['GET'])
def get_moves(game_id):
    result, status_code = tic_tac_toe.get_moves(game_id)
    return jsonify(result), status_code


@bp_game.route('/all', methods=['GET'])
def get_games():
    result, status_code = tic_tac_toe.get_games()
    return jsonify(result), status_code