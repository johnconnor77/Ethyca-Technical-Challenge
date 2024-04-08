import random
from datetime import datetime


class TicTacToe:

    def __init__(self):
        self.games = []
        self.game_id_counter = 1

    def create_game(self):
        game = {'id': self.game_id_counter, 'board': [[' ' for _ in range(3)] for _ in range(3)], 'moves': []}
        self.games.append(game)
        self.game_id_counter += 1
        return game

    def make_move(self, game_id, x, y):
        game = self.find_game_by_id(game_id)
        if game is None:
            return {'error': 'Game not found'}, 404

        board = game['board']

        if board[y][x] != ' ':
            return {'error': 'Cell already occupied'}, 400

        board[y][x] = 'X'

        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[j][i] == ' ']
        if empty_cells:
            computer_move = random.choice(empty_cells)
            board[computer_move[1]][computer_move[0]] = 'O'
            game['moves'].append({'player': 'O', 'position': computer_move, 'timestamp': datetime.now()})

        game['moves'].append({'player': 'X', 'position': {'x': x, 'y': y}, 'timestamp': datetime.now()})

        return {'board': board}, 200

    def get_moves(self, game_id):
        game = self.find_game_by_id(game_id)
        if game is None:
            return {'error': 'Game not found'}, 404
        return {'moves': game['moves']}, 200

    def get_games(self):
        return {'games': self.games}, 200

    def find_game_by_id(self, game_id):
        return next((g for g in self.games if g['id'] == game_id), None)
