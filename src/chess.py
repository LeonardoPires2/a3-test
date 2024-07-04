from enum import Enum

from src.board import Board
from src.color import Color
from src.terminal import T_FRED, T_RESET


class Chess:

  _board: Board
  _jogador: Color = Color.WHITE

  def __init__(self):
    self._board = Board()
    self._board.reset()
  
  def play(self):

    while(True):
      # mostrar o tabuleiro atual
      print(self._board)
      color = "brancas" if (self._jogador == Color.WHITE) else "pretas"
      print(T_FRED + "SYS: turno das peças " + color + T_RESET)

      # ATENÇÃO AQUI!
      # coordenadas precisam ser perguntadas "ao contrário",
      # pois o tabuleiro é impresso linha-a-linha
      
      # perguntar posição da peça a ser movida
      yo = input("Digite a origem x: ")
      xo = input("Digite a origem y: ")
  
      # perguntar para onde a peça vai
      yd = input("Digite a destino x: ")
      xd = input("Digite a destino y: ")
    
      # se for válida, mudar jogador
      valido = self._board.jogar( \
        self._jogador, \
        int(xo), int(yo), \
        int(xd), int(yd))
      
      if(valido):
        self._jogador = Color.WHITE \
          if self._jogador == Color.BLACK \
            else Color.BLACK  