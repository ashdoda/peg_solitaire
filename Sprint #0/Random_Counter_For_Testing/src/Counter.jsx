import { useState } from "react";

export default function Counter() {
  const [count, setCount] = useState(0);

  return (
    <main style={{ fontFamily: "sans-serif", textAlign: "center", marginTop: "3rem" }}>
      <h1>Counter</h1>
      <p data-testid="count">Count: {count}</p>
      <button onClick={() => setCount(count - 1)}>-</button>
      <button onClick={() => setCount(0)}>Reset</button>
      <button onClick={() => setCount(count + 1)}>+</button>
    </main>
  );
}
