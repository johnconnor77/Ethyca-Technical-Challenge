from application import intial_app
from flask import jsonify
from flask_swagger_ui import get_swaggerui_blueprint


app = intial_app('development')

SWAGGER_URL = '/api/docs'
API_URL = '/apidocs/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Tic Tac Toe API"
    },
)

app.register_blueprint(swaggerui_blueprint)

# Generate Swagger JSON manually
swagger_json = {
    "swagger": "2.0",
    "info": {
        "title": "Tic Tac Toe API",
        "description": "API for Tic Tac Toe game",
        "version": "1.0"
    },
    "basePath": "/",
    "schemes": [
        "http",
        "https"
    ],
    "paths": {
        "/game/new": {
            "post": {
                "summary": "Create a new game",
                "responses": {
                    "201": {
                        "description": "Created",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "game_id": {
                                    "type": "integer"
                                }
                            }
                        }
                    }
                }
            },
        },
        "/game/all": {
        "get": {
            "summary": "Get all games",
            "responses": {
                "200": {
                    "description": "Successful operation",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "games": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/Game"
                                }
                            }
                        }
                    }
                }
            }
        }
        },
        "/game/{game_id}/moves": {
            "post": {
                "summary": "Make a move",
                "parameters": [
                    {
                        "name": "game_id",
                        "in": "path",
                        "required": True,
                        "type": "integer"
                    },
                    {
                        "name": "x",
                        "in": "formData",
                        "required": True,
                        "type": "integer"
                    },
                    {
                        "name": "y",
                        "in": "formData",
                        "required": True,
                        "type": "integer"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Move successful"
                    },
                    "400": {
                        "description": "Bad request"
                    },
                    "404": {
                        "description": "Game not found"
                    }
                }
            },
            "get": {
                "summary": "Get moves of a game",
                "parameters": [
                    {
                        "name": "game_id",
                        "in": "path",
                        "required": True,
                        "type": "integer"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful operation",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "moves": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/definitions/Move"
                                    }
                                }
                            }
                        }
                    },
                    "404": {
                        "description": "Game not found"
                    }
                }
            }
        }
    },
    "definitions": {
        "Game": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "board": {
                    "type": "array",
                    "items": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        "Move": {
            "type": "object",
            "properties": {
                "player": {
                    "type": "string"
                },
                "position": {
                    "type": "object",
                    "properties": {
                        "x": {
                            "type": "integer"
                        },
                        "y": {
                            "type": "integer"
                        }
                    }
                },
                "timestamp": {
                    "type": "string",
                    "format": "date-time"
                }
            }
        }
    }
}


# Route to serve Swagger JSON
@app.route('/apidocs/swagger.json')
def serve_swagger_json():
    return jsonify(swagger_json)


if __name__ == "__main__":
    app.run()

