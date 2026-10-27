from enum import Enum

class CellState(Enum):
    INVALID = 0 #not part of the board shape  
    EMPTY = 1 #does not contain a peg
    PEG = 2 #contains a peg

class Board:
    MIN_SIZE = 7
    MAX_SIZE = 21
    SIZE_ERROR = f"Size must be an odd number from {MIN_SIZE} to {MAX_SIZE}"

    def __init__(self, size):
        if (not isinstance(size, int)
                or isinstance(size, bool)
                or size % 2 == 0
                or size < self.MIN_SIZE
                or size > self.MAX_SIZE):
            raise ValueError(self.SIZE_ERROR)
        self.size = size
        self._build_grid()

    def _is_valid_cell(self, row, col):
        raise NotImplementedError("is_valid_cell method is not implemented yet.")

    def _build_grid(self):
        self.grid = [
            [
                CellState.PEG if self._is_valid_cell(row, col) else CellState.INVALID
                for col in range(self.size)
            ]
            for row in range(self.size)
        ]
        center = self.size // 2
        self.grid[center][center] = CellState.EMPTY
    
    def get_cell(self, row, col):
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            return CellState.INVALID
        return self.grid[row][col]

    def peg_count(self):
        return sum(row.count(CellState.PEG) for row in self.grid)

    def set_cell(self, row, col, state):
        self.grid[row][col] = state


class EnglishBoard(Board):
    def _is_valid_cell(self, row, col):
        center = self.size // 2
        return abs(row - center) <= 1 or abs(col - center) <= 1

class DiamondBoard(Board):
    def _is_valid_cell(self, row, col):
        center = self.size // 2
        return abs(row - center) + abs(col - center) <= center

class HexagonBoard(Board):
    def _is_valid_cell(self, row, col):
        center = self.size // 2
        row_offset = abs(row - center)
        col_offset = abs(col - center)
        return row_offset <= center and col_offset <= center - (row_offset + 1) // 2