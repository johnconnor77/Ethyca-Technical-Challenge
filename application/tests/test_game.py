import unittest
import json
from unittest.mock import patch
from application.models.model import TicTacToe
from application import intial_app


class TicTacToeTestCase(unittest.TestCase):
    def setUp(self):
        self.app = intial_app().test_client()

    def tearDown(self):
        pass

    @patch('application.models.model.TicTacToe')
    def test_create_game(self, mock_tic_tac_toe):
        # Mocking TicTacToe class
        mocked_instance = mock_tic_tac_toe.return_value
        mocked_instance.create_game.return_value = {'id': 1}

        # Make a request to create a new game
        response = self.app.post('/game/new')
        data = json.loads(response.data.decode('utf-8'))

        # Assertions
        self.assertEqual(response.status_code, 201)
        self.assertIn('game_id', data)

    def side_effect_find_game_by_id(self, game_id):
        if game_id == 1:
            # Simulate a game state with the player's move
            return {'id': 1, 'board': [['X' for _ in range(3)] for _ in range(3)]}
        else:
            return None

    @patch('application.models.model.TicTacToe')
    def test_make_move(self, mock_tic_tac_toe):
        # Mocking TicTacToe class
        mocked_instance = mock_tic_tac_toe
        mocked_instance.create_game.return_value = {'id': 1}
        mocked_instance.find_game_by_id.side_effect = self.side_effect_find_game_by_id

        # Create a game first
        response = self.app.post('/game/new')
        game_id = json.loads(response.data.decode('utf-8'))['game_id']

        # Make a move
        data = {'x': 0, 'y': 0}
        response = self.app.post(f'/game/{game_id}/moves', json=data)

        # Assertions
        self.assertEqual(response.status_code, 200)

        # Test if the move is made correctly
        game = mocked_instance.find_game_by_id(game_id)
        self.assertEqual(game['board'][0][0], 'X')

    def test_get_moves(self):
        # Create a game first
        response = self.app.post('/game/new')
        game_id = json.loads(response.data.decode('utf-8'))['game_id']

        # Get moves
        response = self.app.get(f'/game/{game_id}/moves')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertIn('moves', data)


if __name__ == '__main__':
    unittest.main()
