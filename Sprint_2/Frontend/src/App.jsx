import { useEffect, useState } from "react";
import "./App.css";

const API = "http://127.0.0.1:5000/api";
const SERVER_DOWN = "Cannot reach the game server. Is the Flask backend running?";

const RESULT_TEXT = {
  win: "You win! Only one peg is left.",
  "partial win": "Partial win: two pegs left and no moves remain.",
  loss: "Game over: no more moves are possible.",
};

async function post(path, body) {
  const response = await fetch(`${API}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  return { ok: response.ok, data: await response.json() };
}

export default function App() {
  const [sizeText, setSizeText] = useState("7");
  const [boardType, setBoardType] = useState("english");
  const [game, setGame] = useState(null);
  const [selected, setSelected] = useState(null);
  const [message, setMessage] = useState("");

  async function newGame(size, type) {
    try {
      const { ok, data } = await post("/new-game", { size, boardType: type });
      if (ok) {
        setGame(data);
        setSelected(null);
        setMessage("");
      } else {
        setMessage(data.error); // current board stays as it was
      }
    } catch {
      setMessage(SERVER_DOWN);
    }
  }

  // start with the defaults shown in the form: size 7, English
  useEffect(() => {
    newGame("7", "english");
  }, []);

  async function handleCellClick(row, col) {
    if (!game || game.gameOver) return;
    const cell = game.board[row][col];

    if (cell === "peg") {
      const same = selected && selected.row === row && selected.col === col;
      setSelected(same ? null : { row, col });
      setMessage("");
      return;
    }
    if (!selected) return;

    // a peg is selected and the player clicked a hole or a spot off the board
    try {
      const { data } = await post("/move", {
        fromRow: selected.row,
        fromCol: selected.col,
        toRow: row,
        toCol: col,
      });
      if (data.board) setGame(data);
      setMessage(data.valid ? "" : "Invalid move.");
    } catch {
      setMessage(SERVER_DOWN);
    }
    setSelected(null);
  }

  const cellPx = game ? Math.floor(Math.min(36, 520 / game.size)) : 36;

  return (
    <div className="app">
      <h1>Peg Solitaire</h1>
      <div className="layout">
        <fieldset className="options">
          <legend>Board Type</legend>
          {["english", "hexagon", "diamond"].map((type) => (
            <label key={type}>
              <input
                type="radio"
                name="boardType"
                value={type}
                checked={boardType === type}
                onChange={() => setBoardType(type)}
              />
              {type[0].toUpperCase() + type.slice(1)}
            </label>
          ))}
        </fieldset>

        <div className="board-area">
          {game && (
            <div
              className="board"
              style={{ gridTemplateColumns: `repeat(${game.size}, ${cellPx}px)` }}
            >
              {game.board.map((cells, row) =>
                cells.map((cell, col) => {
                  const isSelected =
                    selected && selected.row === row && selected.col === col;
                  return (
                    <button
                      key={`${row}-${col}`}
                      className={`cell ${cell}${isSelected ? " selected" : ""}`}
                      style={{ width: cellPx, height: cellPx }}
                      onClick={() => handleCellClick(row, col)}
                      aria-label={`row ${row} column ${col} ${cell}`}
                    />
                  );
                })
              )}
            </div>
          )}
          {game && <p>Pegs left: {game.pegCount}</p>}
          {message && <p className="error" role="alert">{message}</p>}
          {game && game.gameOver && (
            <p className="banner">{RESULT_TEXT[game.result]} Press New Game to play again.</p>
          )}
        </div>

        <div className="controls">
          <label>
            Board size
            <input
              type="text"
              value={sizeText}
              onChange={(e) => setSizeText(e.target.value)}
            />
          </label>
          <button onClick={() => newGame(sizeText, boardType)}>New Game</button>
        </div>
      </div>
    </div>
  );
}