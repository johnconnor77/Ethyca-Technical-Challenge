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

| Method | Endpoint                    | Description                                       |
|--------|-----------------------------|---------------------------------------------------|
| POST   | /game/new                   | Create a New Game                                 |
| POST   | /games/{game_id}/moves      | Make a Move                                       |
| GET    | /games/{game_id}/moves      | Get Moves of a Game                               |
| GET    | /games                      | Get All Games                                     |
| GET    | /api/docs                   | Swagger Documentation Endpoint                    |



## Example



