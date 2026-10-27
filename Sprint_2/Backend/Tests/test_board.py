from Game.board import EnglishBoard, CellState, DiamondBoard, HexagonBoard


class TestEnglishBoard:
    def setup_method(self):
        self.board = EnglishBoard(7)

    def test_peg_count_on_new_board(self):
        assert self.board.peg_count() == 32

    def test_center_is_empty(self):
        assert self.board.get_cell(3, 3) == CellState.EMPTY

    def test_corner_is_not_part_of_board(self):
        assert self.board.get_cell(0, 0) == CellState.INVALID

import pytest

ERROR_MESSAGE = "Size must be an odd number from 7 to 21"


class TestBoardSizeValidation:
    @pytest.mark.parametrize("size", [7, 9, 15, 21])
    def test_valid_odd_size_is_accepted(self, size):
        board = EnglishBoard(size)
        assert board.size == size

    @pytest.mark.parametrize("size", [8, 10, 20])
    def test_even_size_is_rejected(self, size):
        with pytest.raises(ValueError, match=ERROR_MESSAGE):
            EnglishBoard(size)

    @pytest.mark.parametrize("size", [-7, 1, 5, 23, 101])
    def test_out_of_range_odd_size_is_rejected(self, size):
        with pytest.raises(ValueError, match=ERROR_MESSAGE):
            EnglishBoard(size)

    def test_non_integer_float_is_rejected(self):
        with pytest.raises(ValueError, match=ERROR_MESSAGE):
            EnglishBoard(9.5)

    @pytest.mark.parametrize("size", ["9", "abc"])
    def test_string_is_rejected(self, size):
        with pytest.raises(ValueError, match=ERROR_MESSAGE):
            EnglishBoard(size)

    def test_none_is_rejected(self):
        with pytest.raises(ValueError, match=ERROR_MESSAGE):
            EnglishBoard(None)

    def test_empty_string_is_rejected(self):
        with pytest.raises(ValueError, match=ERROR_MESSAGE):
            EnglishBoard("")

class TestBoardShapes:
    def test_diamond_has_24_pegs_at_size_7(self):
        assert DiamondBoard(7).peg_count() == 24

    def test_hexagon_has_32_pegs_at_size_7(self):
        assert HexagonBoard(7).peg_count() == 32

    def test_hexagon_differs_from_diamond(self):
        # (0, 2) is on the hexagon's wide top edge but outside the diamond
        assert HexagonBoard(7).get_cell(0, 2) == CellState.PEG
        assert DiamondBoard(7).get_cell(0, 2) == CellState.INVALID