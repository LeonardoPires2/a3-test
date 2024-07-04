from src.board import Board
from src.color import Color
from src.part import Rock, Position, Knight, Queen, King, Bishop, Pawn

def test_part_rock_recalc_ex3():
    board = Board()
    part1 = Rock(Color.WHITE)
    part2 = Rock(Color.WHITE)
    part3 = Rock(Color.BLACK)
    board.put(0, 0, part1)
    board.put(0, 1, part2)
    board.put(1, 0, part3)
    part1.recalc(board, 0, 0)
    assert len(part1._positions) == 1


def test_part_rock_recalc_ex2():
    board = Board()
    part1 = Rock(Color.WHITE)
    part2 = Rock(Color.WHITE)
    part3 = Rock(Color.WHITE)
    board.put(0, 0, part1)
    board.put(0, 1, part2)
    board.put(1, 0, part3)
    part1.recalc(board, 0, 0)
    assert len(part1._positions) == 0


def test_part_rock_recalc_ex1():
    board = Board()
    part_w = Rock(Color.WHITE)
    part_b = Rock(Color.BLACK)
    board.put(0, 0, part_w)
    board.put(0, 1, part_b)
    part_w.recalc(board, 0, 0)
    assert len(part_w._positions) == 8


def test_part_rock_recalc_empty():
    board = Board()
    part = Rock(Color.WHITE)
    part.recalc(board, 0, 0)
    assert len(part._positions) == 14


def test_part_rock_ctor():

    colors = [Color.WHITE, Color.BLACK]

    for c in colors:
        part = Rock(c)
        assert part._mark_black == "♜"
        assert part._mark_white == "♖"
        assert part._color == c
        assert part._name == "Rock"
        assert part._positions == []


def test_verificar_se_a_classe_position_é_inicializada_corretamente():
    pos = Position(1, 2)
    assert pos._x == 1
    assert pos._y == 2


def test_verificar_representacao_da_cor_da_peca_knight():
    white_knight = Knight(Color.WHITE)
    black_knight = Knight(Color.BLACK)
    assert str(white_knight) == "♘"
    assert str(black_knight) == "♞"


def test_verificar_representacao_da_cor_da_peca_queen():
    white_queen = Queen(Color.WHITE)
    black_queen = Queen(Color.BLACK)
    assert str(white_queen) == "♕"
    assert str(black_queen) == "♛"


def test_verificar_representacao_da_cor_da_peca_king():
    white_king = King(Color.WHITE)
    black_king = King(Color.BLACK)
    assert str(white_king) == "♔"
    assert str(black_king) == "♚"


def test_verificar_representacao_da_cor_da_peca_bishop():
    white_bishop = Bishop(Color.WHITE)
    black_bishop = Bishop(Color.BLACK)
    assert str(white_bishop) == "♗"
    assert str(black_bishop) == "♝"


def test_verificar_representacao_da_cor_da_peca_rock():
    white_rock = Rock(Color.WHITE)
    black_rock = Rock(Color.BLACK)
    assert str(white_rock) == "♖"
    assert str(black_rock) == "♜"


def test_verificar_representacao_da_cor_da_peca_pawn():
    white_pawn = Pawn(Color.WHITE)
    black_pawn = Pawn(Color.BLACK)
    assert str(white_pawn) == "♙"
    assert str(black_pawn) == "♟"


def test_verifica_se_o_movimento_da_peca_rock_e_calculado_corretamente():
    board = Board()
    rock = Rock(Color.WHITE)
    board.put(3, 3, rock)
    rock.recalc(board, 3, 3)
    positions = [(pos._x, pos._y) for pos in rock._positions]
    expected_positions = [
        (2, 3),
        (1, 3),
        (0, 3),
        (4, 3),
        (5, 3),
        (6, 3),
        (7, 3),
        (3, 2),
        (3, 1),
        (3, 0),
        (3, 4),
        (3, 5),
        (3, 6),
        (3, 7),
    ]
    assert set(positions) == set(expected_positions)


def test_verifica_o_movimento_inicial_da_peca_pawn_branca():
    board = Board()
    pawn = Pawn(Color.WHITE)
    board.put(6, 3, pawn)
    pawn.recalc(board, 6, 3)
    positions = [(pos._x, pos._y) for pos in pawn._positions]
    expected_positions = [(5, 3), (4, 3)]
    assert set(positions) == set(expected_positions)


def test_verifica_o_movimento_inicial_da_peca_pawn_preta():
    board = Board()
    pawn = Pawn(Color.BLACK)
    board.put(1, 3, pawn)
    pawn.recalc(board, 1, 3)
    positions = [(pos._x, pos._y) for pos in pawn._positions]
    expected_positions = [(2, 3), (3, 3)]
    assert set(positions) == set(expected_positions)


def test_verifica_se_a_peca_pawn_pode_capturar_uma_peca_inimiga_na_diagonal():
    #test
    board = Board()
    white_pawn = Pawn(Color.WHITE)
    black_pawn = Pawn(Color.BLACK)
    board.put(4, 3, white_pawn)
    board.put(3, 2, black_pawn)
    white_pawn.recalc(board, 4, 3)
    positions = [(pos._x, pos._y) for pos in white_pawn._positions]
    expected_positions = [(3, 3), (2, 3)]
    assert set(positions) == set(expected_positions)
