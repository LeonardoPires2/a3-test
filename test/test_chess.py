from src.chess import Chess
from src.color import Color
from src.part import Pawn, Knight, Rock, Bishop, Queen, King
from src.board import Board


class TestClass:

    def test_verificar_inicializacao_do_tabuleiro(self):
        """
        Verifica se o tabuleiro é inicializado corretamente.
        """
        board = Board()
        for i in range(8):
            for j in range(8):
                assert board.get_peca(i, j) is None

    def test_verificar_se_o_movimento_do_peao_preto_é_invalida(self):
        chess = Chess()
        player: Color = Color.BLACK
        valid = chess._board.jogar(player, 1, 1, 1, 2)
        assert not valid

    def test_verificar_se_o_movimento_do_peao_branco_é_valida(self):
        chess = Chess()
        player: Color = Color.WHITE
        valid = chess._board.jogar(player, 6, 1, 5, 1)
        assert valid

    def test_verificar_movimento_invalido_cavalo_branco(self):
        chess = Chess()
        player: Knight = Color.WHITE
        valid = chess._board.jogar(player, 7, 1, 5, 1)
        assert not valid

    def test_verificar_espaco_que_nao_tem_nenhuma_peca(self):
        chess = Chess()
        position = chess._board.get_peca(4, 5)
        assert position is None, f"Esperado None, mas retornou {position}"

    def test_vericar_se_a_peca_foi_colocada_corretamente_na_posicao(self):
        board = Board()
        knight = Knight(Color.WHITE)
        board.set_peca(knight, 3, 3)
        assert board.get_peca(3, 3) == knight, "A peça deveria estar na posição (3, 3)"
        assert board.get_peca(0, 0) is None, "A posição (0, 0) deveria estar vazia"
        assert board.get_peca(7, 7) is None, "A posição (7, 7) deveria estar vazia"

    def test_verificar_se_uma_peca_pode_ser_colocada_fora_dos_limites_do_tabuleiro(
        self,
    ):
        board = Board()
        knight = Knight(Color.WHITE)
        limit = board.put(10, 10, knight)
        assert limit is None

    def test_verificar_se_o_reset_aconteceu_e_as_pecas_voltaram_pro_seu_lugar_(self):
        board = Board()
        board.reset()
        assert isinstance(board.get_peca(0, 0), Rock)
        assert isinstance(board.get_peca(0, 1), Knight)
        assert isinstance(board.get_peca(0, 2), Bishop)
        assert isinstance(board.get_peca(0, 3), Queen)
        assert isinstance(board.get_peca(0, 4), King)
        assert isinstance(board.get_peca(0, 5), Bishop)
        assert isinstance(board.get_peca(0, 6), Knight)
        assert isinstance(board.get_peca(0, 7), Rock)
        for i in range(8):
            assert isinstance(board.get_peca(1, i), Pawn)
            assert isinstance(board.get_peca(6, i), Pawn)
        assert isinstance(board.get_peca(7, 0), Rock)
        assert isinstance(board.get_peca(7, 1), Knight)
        assert isinstance(board.get_peca(7, 2), Bishop)
        assert isinstance(board.get_peca(7, 3), Queen)
        assert isinstance(board.get_peca(7, 4), King)
        assert isinstance(board.get_peca(7, 5), Bishop)
        assert isinstance(board.get_peca(7, 6), Knight)
        assert isinstance(board.get_peca(7, 7), Rock)

    def test_verificar_movimentacao_sobre_peca_aliada(self):
        board = Board()
        white_knight_1 = Knight(Color.WHITE)
        white_knight_2 = Knight(Color.WHITE)
        board.put(0, 1, white_knight_1)
        board.put(2, 2, white_knight_2)
        resultado = board.jogar(Color.WHITE, 0, 1, 2, 2)
        assert not resultado
        assert board.get_peca(0, 1) == white_knight_1
        assert board.get_peca(2, 2) == white_knight_2

    def test_verificar_movimentacao_de_uma_peca_invalida_e_ignorada(self):
        board = Board()
        knight = Knight(Color.WHITE)
        board.put(0, 1, knight)
        resultado = board.jogar(Color.WHITE, 0, 1, 5, 5)
        assert not resultado
        assert board.get_peca(0, 1) == knight
        assert board.get_peca(5, 5) is None

    def test_verificar_jogada_invalida_posicao_original(self):
        board = Board()
        knight = Knight(Color.WHITE)
        board.put(0, 1, knight)
        result = board.jogar(Color.WHITE, 0, 1, 0, 1)
        assert not result
        assert board.get_peca(0, 1) == knight

    def test_verificar_jogada_invalida_sem_peca(self):
        chess = Chess()
        player: Color = Color.WHITE
        valid = chess._board.jogar(player, 3, 4, 3, 5)
        assert not valid
        assert chess._board.get_peca(3, 4) is None

    def test_verificar_o_primeiro_movimento_do_peao_branco(self):
        chess = Chess()
        player: Color = Color.WHITE
        valid = chess._board.jogar(player, 6, 1, 4, 1)
        assert valid

    def test_verificar_promocao_peao_branco(self):
        board = Board()
        peao = Pawn(Color.WHITE)
        promovida = board.promocao(peao, 0, 0)
        assert isinstance(promovida, King)
        assert promovida._color == Color.WHITE

    def test_verificar_promocao_peao_preto(self):
        board = Board()
        peao = Pawn(Color.BLACK)
        promovida = board.promocao(peao, 7, 7)
        assert isinstance(promovida, King)
        assert promovida._color == Color.BLACK

    def test_verificar_nao_promocao(self):
        board = Board()
        peao = Pawn(Color.WHITE)
        promovida = board.promocao(peao, 2, 2)
        assert promovida is None
