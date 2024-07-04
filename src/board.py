from src.color import Color
from src.part import Bishop, King, Knight, Part, Pawn, Queen, Rock
from src.terminal import T_BBLACK, T_BCYAN, T_BWHITE, T_FBLUE, T_FRED, T_RESET


class Board:

    _NUM_LINES: int = 8
    _NUM_COLUMNS: int = 8

    _removed: list[Part] = []
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
        # mostra as peças brancas que foram capturadas
        for p in self._removed:
            if p._color == Color.WHITE:
                ss.append(str(p) + " ")
        ss.append("\n")

        if self._board is not None:

            # mostra os número superiores (coordenadas do tabuleiro)
            ss.append(T_BCYAN + "   ")
            ss.append("".join([str(i) + " " for i in range(8)]))
            ss.append("   " + T_RESET + "\n")

            endrow = T_BCYAN + "   " + T_RESET

            # imprime cada linha do tabuleiro
            for i in range(len(self._board)):
                row = self._board[i]

                # mostra o número à esquerda de cada linha
                ss.append(T_BCYAN + " " + str(i) + " " + T_RESET)

                # imprime cada célula
                for j in range(len(row)):

                    cell = row[j]
                    color = T_BBLACK if ((i + j) % 2 != 0) else T_BWHITE

                    if cell is None:
                        ss.append(color + "  " + T_RESET)
                    else:
                        ss.append(color + str(cell) + " " + T_RESET)
                ss.append(endrow + "\n")
            ss.append(T_BCYAN + "                      " + T_RESET + "\n")

        # mostra as peças pretas que foram capturadas
        for p in self._removed:
            if p._color == Color.BLACK:
                ss.append(str(p) + " ")
        ss.append("\n")

        return "".join(ss)

    def set_peca(self, part, xd, yd):
        self._board[xd][yd] = part

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
            ss = T_FRED + "SYS: não existe peça na casa " + str(xo) + " "
            ss = ss + str(yo) + T_RESET
            print(ss)
            return False
        else:
            print(T_FRED + "SYS: selecionada peça " + str(part) + "")

        if len(part._positions) == 0:
            print(T_FRED + "SYS: peça " + str(part) + " não possui jogadas válidas")
            return False

        # verifica se a cor da
        # peça é a mesma do jogador
        if part._color != jogador:
            ss = T_FRED + "SYS: peça selecionada não pertence ao jogador, casa "
            ss = ss + str(xo) + " " + str(yo) + T_RESET
            print(ss)
            return False

        # verifica se é possível mover aquela peça
        for p in part._positions:
            if p._x == xd and p._y == yd:
                # se estive ocupado, remove peça
                # inimiga do jogo
                target = self.get_peca(xd, yd)

                # atualizar posição da peça
                if target is None:
                    print(T_FRED + "SYS: peça movida para casa vazia" + T_RESET)
                    self.set_peca(part, xd, yd)
                    self.set_peca(None, xo, yo)
                    return True
                elif target._color != jogador:
                    print(
                        T_FRED + "SYS: peça inimiga capturada " + str(target) + T_RESET
                    )
                    self.set_peca(part, xd, yd)
                    self.set_peca(None, xo, yo)
                    self._removed.append(target)
                    return True
                else:
                    ss = T_FRED + "SYS: impossível mover sobre outra peça aliada "
                    ss = ss + str(target) + T_RESET
                    print(ss)
                    return False

        print(T_FRED + "SYS: jogada inválida!" + T_RESET)
        ss = T_FRED + "SYS: movimentos possíveis de " + str(part) + T_RESET
        print(ss)
        for p in part._positions:
            print(T_FRED + str(p) + T_RESET)
        return False

    def calcula_posicoes(self):
        for i in range(Board._NUM_LINES):
            for j in range(Board._NUM_COLUMNS):

                part = self.get_peca(i, j)

                if part is not None:
                    part.recalc(self, i, j)

    def promocao(self, part, xd, yd):
      if part == Pawn(Color.BLACK) or Pawn(Color.WHITE):
        if xd == 0 or xd == 7 & yd == 0 or yd == 7:
            return King(part._color)
        return None

    def reset(self):
        # adiciona 4 cavalos no tabuleiro
        knight_white1 = Knight(Color.WHITE)
        knight_white2 = Knight(Color.WHITE)
        knight_black1 = Knight(Color.BLACK)
        knight_black2 = Knight(Color.BLACK)

        self.put(0, 1, knight_black1)
        self.put(0, 6, knight_black2)
        self.put(7, 1, knight_white1)
        self.put(7, 6, knight_white2)

        # adiciona 4 torres no tabuleiro
        rock_white1 = Rock(Color.WHITE)
        rock_white2 = Rock(Color.WHITE)
        rock_black1 = Rock(Color.BLACK)
        rock_black2 = Rock(Color.BLACK)

        self.put(0, 0, rock_black1)
        self.put(0, 7, rock_black2)
        self.put(7, 0, rock_white1)
        self.put(7, 7, rock_white2)

        # adiciona 4 bispos no tabuleiro
        bishop_white1 = Bishop(Color.WHITE)
        bishop_white2 = Bishop(Color.WHITE)
        bishop_black1 = Bishop(Color.BLACK)
        bishop_black2 = Bishop(Color.BLACK)

        self.put(0, 2, bishop_black1)
        self.put(0, 5, bishop_black2)
        self.put(7, 2, bishop_white1)
        self.put(7, 5, bishop_white2)

        # adiciona 2 reais no tabuleiro
        king_white = King(Color.WHITE)
        king_black = King(Color.BLACK)

        self.put(0, 4, king_black)
        self.put(7, 4, king_white)

        # adiciona duas rainhas no tabuleiro
        queen_white = Queen(Color.WHITE)
        queen_black = Queen(Color.BLACK)

        self.put(0, 3, queen_black)
        self.put(7, 3, queen_white)

        # adiciona 16 peões no tabuleiro
        for i in range(8):
            pawn = Pawn(Color.BLACK)
            self.put(1, i, pawn)
            pawn = Pawn(Color.WHITE)
            self.put(6, i, pawn)

        self.calcula_posicoes()
