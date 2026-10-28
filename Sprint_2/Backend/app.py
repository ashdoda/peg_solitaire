from flask import Flask, jsonify, request
from flask_cors import CORS

from Game.game import Game

app = Flask(__name__)
CORS(app) # lets the react frontend access the backend

game = Game()  # Initialize a default game

def parse_size(raw):
    """Turn a raw input into an integer size. Anything that isn't plain digits is passed through untouched and board rejects it."""
    if isinstance(raw, str) and raw.isascii() and raw.isdigit():
        return int(raw)
    return raw

def state():
    board = game.board
    return {
        "size": board.size,
        "boardType": game.board_type,
        "board":[[board.get_cell(r, c).name.lower()
                   for c in range(board.size)]
                  for r in range(board.size)],
        "pegCount": board.peg_count(),
        "gameOver": game.is_game_over(),
        "result": game.get_result()
    }

@app.get("/api/state")
def get_state():
    return jsonify(state())

@app.post("/api/new-game")
def new_game():
    data = request.get_json(silent=True) or {}
    try:
        game.new_game(parse_size(data.get("size")), data.get("boardType")) #ask if it should be ,english
    except ValueError as error:
        return jsonify({"error": str(error)}), 400
    return jsonify(state())

@app.post("/api/move")
def move():
    data = request.get_json(silent=True) or {}
    keys = ["fromRow", "fromCol", "toRow", "toCol"]
    values = [data.get(key) for key in keys]
    if not all(isinstance(v, int) and not isinstance(v, bool) for v in values):
        return jsonify({"error": "Move needs integer fromRow, fromCol, toRow, and toCol"}), 400
    valid = game.make_move(*values)
    return jsonify({"valid": valid, **state()})

if __name__ == "__main__":
    app.run(debug=True)