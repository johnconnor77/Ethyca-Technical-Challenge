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

| Method | Endpoint              | Description                                       |
|--------|-----------------------|---------------------------------------------------|
| POST   | /game/new             | Create a New Game                                 |
| POST   | /game/{game_id}/moves | Make a Move                                       |
| GET    | /game/{game_id}/moves | Get Moves of a Game                               |
| GET    | /game/all             | Get All Games                                     |
| GET    | /api/docs             | Swagger Documentation Endpoint                    |



## Example

![newgame](https://github.com/johnconnor77/Ethyca-Technical-Challenge/assets/51679898/4f2bc197-e58e-443f-a3ce-cd9f64eaa665)

![movegame](https://github.com/johnconnor77/Ethyca-Technical-Challenge/assets/51679898/5e349359-bbdc-442b-8f18-9850d6ab9b7d)

![gamesall](https://github.com/johnconnor77/Ethyca-Technical-Challenge/assets/51679898/fcdab2ef-db7b-404f-8823-aec505f378dd)

![moves](https://github.com/johnconnor77/Ethyca-Technical-Challenge/assets/51679898/5dce0dab-d1d1-448f-8b71-0e211a81ecb2)


![swaggerdocs](https://github.com/johnconnor77/Ethyca-Technical-Challenge/assets/51679898/a4842792-2b6a-409a-852b-2a46a4d71565)


## API Documentation
