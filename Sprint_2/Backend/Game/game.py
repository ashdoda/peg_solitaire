from Game.board import (Board, CellState, EnglishBoard, DiamondBoard, HexagonBoard )

class Game:
    BOARD_TYPES = {
        "english": EnglishBoard,  
        "hexagon": HexagonBoard,
        "diamond": DiamondBoard
    }
    DIRECTIONS = [(-2, 0), (2, 0), (0, -2), (0, 2), (-2, -2), (-2, 2), (2, -2), (2, 2)]  # Possible move directions (up, down, left, right, and diagonals)

    def __init__(self, size=7, board_type="english"):
        self.new_game(size, board_type)

    def new_game(self, size, board_type):
        if board_type not in self.BOARD_TYPES:
            raise ValueError(f"Invalid board type: {board_type}. Valid types are: {list(self.BOARD_TYPES.keys())}")
        board = self.BOARD_TYPES[board_type](size)
        self.board = board
        self.board_type = board_type

    def _is_valid_move(self, from_row, from_col, to_row, to_col):
        board = self.board
        if (to_row - from_row, to_col - from_col) not in self.DIRECTIONS:
            return False
        if board.get_cell(from_row, from_col) != CellState.PEG:
            return False
        if board.get_cell(to_row, to_col) != CellState.EMPTY:
            return False
        mid_row = (from_row + to_row) // 2
        mid_col = (from_col + to_col) // 2
        return board.get_cell(mid_row, mid_col) == CellState.PEG

    def make_move(self, from_row, from_col, to_row, to_col):
        if not self._is_valid_move(from_row, from_col, to_row, to_col):
            return False
        mid_row = (from_row + to_row) // 2
        mid_col = (from_col + to_col) // 2
        self.board.set_cell(from_row, from_col, CellState.EMPTY)
        self.board.set_cell(mid_row, mid_col, CellState.EMPTY)
        self.board.set_cell(to_row, to_col, CellState.PEG)
        return True

    def has_valid_moves(self):
        for row in range(self.board.size):
            for col in range(self.board.size):
                for d_row, d_col in self.DIRECTIONS:
                    if self._is_valid_move(row, col, row + d_row, col + d_col):
                        return True
        return False

    def is_game_over(self):
        return not self.has_valid_moves()
    def get_result(self):
        if not self.is_game_over():
            return None
        pegs = self.board.peg_count()
        if pegs == 1:
            return "win"
        if pegs == 2:
            return "partial win"
        return "loss"