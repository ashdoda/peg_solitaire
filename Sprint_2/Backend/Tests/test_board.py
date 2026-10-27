from Game.board import EnglishBoard, CellState


class TestEnglishBoard:
    def setup_method(self):
        self.board = EnglishBoard(7)

    def test_peg_count_on_new_board(self):
        assert self.board.peg_count() == 32

    def test_center_is_empty(self):
        assert self.board.get_cell(3, 3) == CellState.EMPTY

    def test_corner_is_not_part_of_board(self):
        assert self.board.get_cell(0, 0) == CellState.INVALID