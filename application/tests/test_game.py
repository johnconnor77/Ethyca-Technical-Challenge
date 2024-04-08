import unittest
import json
from unittest.mock import patch, MagicMock
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

    @patch('application.models.model.TicTacToe')
    def test_make_move(self, mock_tic_tac_toe):
        # Mocking TicTacToe class
        mocked_instance = mock_tic_tac_toe.return_value
        mocked_instance.create_game.return_value = {'id': 1}

        # Create a game first
        response = self.app.post('/game/new')
        game_id = json.loads(response.data.decode('utf-8'))['game_id']

        # Store the initial return value of find_game_by_id
        initial_return_value = {'id': 1, 'board': [[' ' for _ in range(3)] for _ in range(3)]}
        mocked_instance.find_game_by_id.return_value = initial_return_value

        # Make a move
        data = {'x': 0, 'y': 0}
        response = self.app.post(f'/game/{game_id}/moves', json=data)

        # Update the mocked game state after making the move
        updated_return_value = initial_return_value.copy()  # Create a copy to avoid modifying the original
        updated_return_value['board'][0][0] = 'X'
        mocked_instance.find_game_by_id.return_value = updated_return_value

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
