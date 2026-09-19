import { render, screen, fireEvent } from "@testing-library/react";
import Counter from "./Counter";

describe("Counter", () => {
  beforeEach(() => {
    render(<Counter />);                 // fresh counter before every test
  });

  it("starts at 0", () => {
    expect(screen.getByTestId("count")).toHaveTextContent("Count: 0");
  });

  it("increments when + is clicked", () => {
    fireEvent.click(screen.getByText("+"));
    fireEvent.click(screen.getByText("+"));
    expect(screen.getByTestId("count")).toHaveTextContent("Count: 2");
  });

  it("decrements when - is clicked", () => {
    fireEvent.click(screen.getByText("-"));
    expect(screen.getByTestId("count")).toHaveTextContent("Count: -1");
  });

  it("resets to 0 when Reset is clicked", () => {
    fireEvent.click(screen.getByText("+"));
    fireEvent.click(screen.getByText("+"));
    fireEvent.click(screen.getByText("Reset"));
    expect(screen.getByTestId("count")).toHaveTextContent("Count: 0");
  });
});
