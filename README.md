## How to run this project


### Create your new virtualenv.
- python -m venv venv 
### Then pip install all depencies in requirements.txt 
 - pip install -r requirements.txt
### run code 
 - python run.py
### run testing script
 - pytest


# Tic Tac Toe API

This is a simple RESTful API for playing Tic Tac Toe.

## How to Play

Tic Tac Toe is a two-player game where each player takes turns marking spaces in a 3x3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

## Endpoints

### Create a New Game

POST /game/new

Creates a new Tic Tac Toe game and returns the game ID.

### Make a Move

POST /games/{game_id}/moves

Makes a move in the Tic Tac Toe game with the specified game ID. The request body should include the coordinates (x, y) of the move.

### Get Moves of a Game

GET /games/{game_id}/moves

Retrieves all moves made in the Tic Tac Toe game with the specified game ID.

### Get All Games

GET /games

Retrieves information about all Tic Tac Toe games.

## Example



