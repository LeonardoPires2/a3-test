from src.color import Color
from src.part import Bishop, King, Knight, Pawn, Queen, Rock


class Board:

    _NUM_LINES = 8
    _NUM_COLUMNS = 8

    _removed = []
    _board = []

    def __init__(self):
        self._board = [
            [None for j in range(Board._NUM_LINES)] for i in range(Board._NUM_COLUMNS)
        ]
        self._removed = []

    def put(self, i, j, part):
        if self._board is not None and i >= 0 and j >= 0 and i < 8 and j < 8:
            self._board[i][j] = part

    def __str__(self):
        ss = []

        for p in self._removed:
            ss.append(str(p))
        ss.append("\n")

        if self._board is not None:
            for i in self._board:
                for j in i:
                    if j is None:
                        ss.append("  | ")
                    else:
                        ss.append(str(j) + " | ")
                ss.append("\n\n")
            return "".join(ss)
        else:
            return ""

    def set_peca(self, part, xd, yd):
        self._board[xd][yd] = part

    def clear_board(self):
        self._board = []

    def get_peca(self, xo, yo):
        if xo >= 0 and yo >= 0 and xo <= 7 and yo <= 7:
            return self._board[xo][yo]
        else:
            return None

    def jogar(self, jogador, xo, yo, xd, yd):

        # verifica se há uma
        # peça na coordenada de origem
        part = self.get_peca(xo, yo)
        if part is None:
            return False

        # verifica se a cor da
        # peça é a mesma do jogador
        # print(part._color, jogador)
        if part._color != jogador:
            return False

        # verifica se é possível mover aquela peça
        for p in part._positions:
            if p._x == xd and p._y == yd:
                # se estive ocupado, remove peça
                # inimiga do jogo
                target = self.get_peca(xd, yd)

                # atualizar posição da peça
                if target is None:
                    print("Movida para espaço vazio")
                    self.set_peca(part, xd, yd)
                    self.set_peca(None, xo, yo)
                    return True
                elif target._color != jogador:
                    print("Removida ", str(target))
                    self.set_peca(part, xd, yd)
                    self.set_peca(None, xo, yo)
                    self._removed.append(target)
                    return True

        return False

    def calcula_posicoes(self):
        for i in range(Board._NUM_LINES):
            for j in range(Board._NUM_COLUMNS):

                part = self.get_peca(i, j)

                if part is not None:
                    part.recalc(self, i, j)

    def reset(self):
        knight_white1 = Knight(Color.WHITE)
        knight_white2 = Knight(Color.WHITE)
        knight_black1 = Knight(Color.BLACK)
        knight_black2 = Knight(Color.BLACK)

        rock_white1 = Rock(Color.WHITE)
        rock_white2 = Rock(Color.WHITE)
        rock_black1 = Rock(Color.BLACK)
        rock_black2 = Rock(Color.BLACK)

        bishop_white1 = Bishop(Color.WHITE)
        bishop_white2 = Bishop(Color.WHITE)
        bishop_black1 = Bishop(Color.BLACK)
        bishop_black2 = Bishop(Color.BLACK)

        king_white = King(Color.WHITE)
        king_black = King(Color.BLACK)

        queen_white = Queen(Color.WHITE)
        queen_black = Queen(Color.BLACK)

        self.put(0, 0, rock_black1)
        self.put(0, 7, rock_black2)
        self.put(7, 0, rock_white1)
        self.put(7, 7, rock_white2)

        self.put(0, 1, knight_black1)
        self.put(0, 6, knight_black2)
        self.put(7, 1, knight_white1)
        self.put(7, 6, knight_white2)

        self.put(0, 2, bishop_black1)
        self.put(0, 5, bishop_black2)
        self.put(7, 2, bishop_white1)
        self.put(7, 5, bishop_white2)

        self.put(0, 3, queen_black)
        self.put(0, 4, king_black)
        self.put(7, 3, queen_white)
        self.put(7, 4, king_white)

        for i in range(8):
            pawn = Pawn(Color.BLACK)
            self.put(1, i, pawn)
            pawn = Pawn(Color.WHITE)
            self.put(6, i, pawn)

        rock_white3 = Rock(Color.WHITE)
        self.put(5, 5, rock_white3)

        self.calcula_posicoes()
