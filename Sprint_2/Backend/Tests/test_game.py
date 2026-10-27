import pytest

from Game.board import CellState
from Game.game import Game


def clear_board(game):
    for r in range(game.board.size):
        for c in range(game.board.size):
            if game.board.get_cell(r, c) == CellState.PEG:
                game.board.set_cell(r, c, CellState.EMPTY)


class TestNewGame:
    @pytest.mark.parametrize("board_type", ["english", "hexagon", "diamond"])
    def test_new_game_has_only_center_empty(self, board_type):
        game = Game(9, board_type)
        assert game.board.size == 9
        assert game.board.get_cell(4, 4) == CellState.EMPTY

    def test_invalid_size_leaves_current_game_unchanged(self):
        game = Game(9, "english")
        with pytest.raises(ValueError):
            game.new_game(8, "diamond")
        assert game.board.size == 9 and game.board_type == "english"

    def test_invalid_board_type_rejected(self):
        with pytest.raises(ValueError):
            Game(7, "triangle")


class TestMakeMove:
    def setup_method(self):
        self.game = Game(7, "english")

    def test_valid_orthogonal_jump(self):
        assert self.game.make_move(3, 1, 3, 3) is True
        b = self.game.board
        assert b.get_cell(3, 1) == CellState.EMPTY
        assert b.get_cell(3, 2) == CellState.EMPTY
        assert b.get_cell(3, 3) == CellState.PEG
        assert b.peg_count() == 31

    def test_valid_diagonal_jump(self):
        b = self.game.board
        b.set_cell(3, 3, CellState.PEG)
        b.set_cell(4, 4, CellState.EMPTY)
        assert self.game.make_move(2, 2, 4, 4) is True
        assert b.get_cell(3, 3) == CellState.EMPTY
        assert b.get_cell(4, 4) == CellState.PEG

    def test_destination_occupied_is_rejected(self):
        assert self.game.make_move(3, 1, 3, 2) is False
        assert self.game.board.peg_count() == 32

    def test_no_peg_to_jump_is_rejected(self):
        self.game.make_move(3, 1, 3, 3)
        assert self.game.make_move(3, 0, 3, 2) is False

    def test_wrong_distance_is_rejected(self):
        assert self.game.make_move(3, 2, 3, 3) is False

    def test_off_board_is_rejected(self):
        assert self.game.make_move(3, 1, 3, -1) is False
        assert self.game.board.peg_count() == 32


class TestGameOver:
    def test_new_game_is_not_over(self):
        game = Game(7, "english")
        assert game.is_game_over() is False
        assert game.get_result() is None

    def test_one_peg_is_a_win(self):
        game = Game(7, "english")
        clear_board(game)
        game.board.set_cell(3, 3, CellState.PEG)
        assert game.get_result() == "win"

    def test_two_pegs_no_moves_is_partial_win(self):
        game = Game(7, "english")
        clear_board(game)
        game.board.set_cell(3, 0, CellState.PEG)
        game.board.set_cell(3, 6, CellState.PEG)
        assert game.get_result() == "partial win"

    def test_three_pegs_no_moves_is_a_loss(self):
        game = Game(7, "english")
        clear_board(game)
        for r, c in [(3, 0), (3, 6), (0, 3)]:
            game.board.set_cell(r, c, CellState.PEG)
        assert game.get_result() == "loss"