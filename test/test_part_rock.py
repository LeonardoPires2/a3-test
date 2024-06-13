from src.board import Board
from src.color import Color
from src.part import Rock


def test_part_rock_recalc_ex2():
    board = Board()
    part1 = Rock(Color.WHITE)
    part2 = Rock(Color.BLACK)
    part3 = Rock(Color.BLACK)


def test_part_rock_recalc_exi():
    board = Board()
    part_w = Rock(Color.WHITE)
    part_b = Rock(Color.BLACK)
    board.put(0, 0, part_w)
    board.put(0, 1, part_b)
    part_w.recalc(board, 0, 0)
    assert len(part_w._positions) == 8


# def test_part_rock_recalc_empty():
#     board = Board()
#     part = Rock(Color.WHITE)
#     part.recalc(board, 2, 2)

#     expected_positions = 4
#     assert part == expected_positions


def test_part_rock_ctor_w():

    colors = [Color.WHITE, Color.BLACK]

    for c in colors:
        part = Rock(c)
        assert part._mark_black == "♜"
        assert part._mark_white == "♖"
        assert part._color == c
        assert part._name == "Rock"
        assert part._positions == []


def test_empty_board():
    board = Board()
    board.clear_board()
    board.calcula_posicoes()

    assert not any(piece.recalc_called for piece in board.get_all_pieces())
