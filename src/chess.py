from enum import Enum

from src.board import Board
from src.color import Color
from src.part import Bishop, King, Knight, Pawn, Queen, Rock


class Chess:

  _board: Board = None
  _jogador: Color = Color.WHITE

  def __init__(self):
    self._board = Board()
    self._board.reset()
  
  def play(self):

    while(True):
      # mostrar o tabuleiro atual
      print(self._board)
  
      # perguntar posição da peça a ser movida
      xo = input("Digite a origem x: ")
      yo = input("Digite a origem y: ")
  
      # perguntar para onde a peça vai
      xd = input("Digite a destino x: ")
      yd = input("Digite a destino y: ")
    
      # se for válida, mudar jogador
      valido = self._board.jogar( \
        self._jogador, \
        int(xo), int(yo), \
        int(xd), int(yd))
      
      if(valido):
        self._jogador = Color.WHITE \
          if self._jogador == Color.BLACK \
            else Color.BLACK
        print("Agora é a vez das ", self._jogador)
      else:
        print("Jogada inválida. Tente outra vez.")
  