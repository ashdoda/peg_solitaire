import { useState } from "react";

export default function App() {
  const [hints, setHints] = useState(false);
  const [choice, setChoice] = useState("");
  return (
    <main>
      <h1>Testing</h1>
      <hr />
      <p>This is a simple test of the GUI.</p>
      <svg width="200" height="10">
        <line x1="0" y1="5" x2="200" y2="5" stroke="currentColor" />
      </svg>
      <div>
          <label>
          <input
            type="checkbox"
            checked={hints}
            onChange={(e) => setHints(e.target.checked)}
          />
          Test Button
        </label>
      </div>
      <div>
        <fieldset>
          <legend>Radio Buttons</legend>
          <label>
            <input
              type="radio"
              name="Pick ME!"
              value="Pick ME!"
              checked={choice === "Pick ME!"}
              onChange={(e) => setChoice(e.target.value)}
            />
            Pick Me!
          </label>
          <label>
            <input
              type="radio"
              name="No, ME!"
              value="No, ME!"
              checked={choice === "No, ME!"}
              onChange={(e) => setChoice(e.target.value)}
            />
            No, ME!
          </label>
          <label>
            <input
              type="radio"
              name="Actually, ME!"
              value="Actually, ME!"
              checked={choice === "Actually, ME!"}
              onChange={(e) => setChoice(e.target.value)}
            />
            Actually, ME!
          </label>
        </fieldset>
      </div>
    </main>
  );
}