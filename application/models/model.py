import random
from flask_api import status
from datetime import datetime


class TicTacToe:
    def __init__(self):
        self.games = []
        self.game_id_counter = 1

    def create_game(self):
        """
        Create a new Tic Tac Toe game.
        ---
        responses:
          201:
            description: Created
            schema:
              properties:
                game_id:
                  type: integer
        """
        game = {'id': self.game_id_counter, 'board': [[' ' for _ in range(3)] for _ in range(3)], 'moves': []}
        self.games.append(game)
        self.game_id_counter += 1
        return game

    def make_move(self, game_id, x, y):
        """
        Make a move in the Tic Tac Toe game.
        ---
        parameters:
          - name: game_id
            in: path
            type: integer
            required: true
          - name: x
            in: body
            type: integer
            required: true
          - name: y
            in: body
            type: integer
            required: true
        responses:
          200:
            description: Move successful
          400:
            description: Bad request
          404:
            description: Game not found
        """
        game = self.find_game_by_id(game_id)
        if game is None:
            return {'error': 'Game not found'}, status.HTTP_404_NOT_FOUND

        board = game['board']

        if board[y][x] != ' ':
            return {'error': 'Cell already occupied'}, status.HTTP_400_BAD_REQUEST

        board[y][x] = 'X'

        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[j][i] == ' ']
        if empty_cells:
            computer_move = random.choice(empty_cells)
            board[computer_move[1]][computer_move[0]] = 'O'
            game['moves'].append({'player': 'O', 'position': computer_move, 'timestamp': datetime.now()})

        game['moves'].append({'player': 'X', 'position': {'x': x, 'y': y}, 'timestamp': datetime.now()})

        return {'board': board}, status.HTTP_200_OK

    def get_moves(self, game_id):
        """
        Get moves made in the Tic Tac Toe game.
        ---
        parameters:
          - name: game_id
            in: path
            type: integer
            required: true
        responses:
          200:
            description: Successful operation
        """
        game = self.find_game_by_id(game_id)
        if game is None:
            return {'error': 'Game not found'}, status.HTTP_404_NOT_FOUND
        return {'moves': game['moves']}, status.HTTP_200_OK

    def get_games(self):
        """
        Get all Tic Tac Toe games.
        ---
        responses:
          200:
            description: Successful operation
        """
        return {'games': self.games}, status.HTTP_200_OK

    def find_game_by_id(self, game_id):
        return next((g for g in self.games if g['id'] == game_id), None)
