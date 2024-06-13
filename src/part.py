# https://www.alt-codes.net/chess-symbols.php
from src.color import Color


class Position:
  _x : int
  _y : int

  def __str__(self):
    return "(" + str(self._x) + ", " + str(self._y) + ")"
      

# classe abstrata
class Part:

  _name : str
  _mark_white : str
  _mark_black: str
  _color : Color
  _positions: list[Position]

  def __init__(self, name, color):
    self._name = name
    self._color = color
    self._positions = []

  def __str__(self):
    return self._mark_white \
      if(self._color == Color.WHITE) \
      else self._mark_black


class Knight(Part):
  _mark_white = "♘"
  _mark_black = "♞"
  
  def __init__(self, color):
    Part.__init__(self, "Cavalo", color)

  def recalc(self, board, x, y):
    pass
  

class Queen(Part):
  _mark_white = "♕"
  _mark_black = "♛"

  def __init__(self, color):
    Part.__init__(self, "Rainha", color)

  def recalc(self, board, x, y):
    pass

class King(Part):
  _mark_white = "♔"
  _mark_black = "♚"

  def __init__(self, color):
    Part.__init__(self, "Rei", color)

  def recalc(self, board, x, y):
    pass
    
class Bishop(Part):
  _mark_white = "♗"
  _mark_black = "♝"

  def __init__(self, color):
    Part.__init__(self, "Bispo", color)

  def recalc(self, board, x, y):
    pass

class Rock(Part):
  _mark_white = "♖"
  _mark_black = "♜"

  def __init__(self, color):
    Part.__init__(self, "Rock", color)

  def recalc(self, board, x, y):

    print(self._name, x, y)
    
    self._positions = []
    
    xt = x - 1
    while(xt >= 0):
      part = board.get_peca(xt, y)
      if(part is None):
        pos = Position()
        pos._x = xt
        pos._y = y
        self._positions.append(pos)
      else:
        # peca de cores diferentes
        if(part._color != self._color):
          pos = Position()
          pos._x = xt
          pos._y = y
          self._positions.append(pos)
        break
      xt = xt -1

    xt = x + 1
    while(xt <= 7):
      part = board.get_peca(xt, y)
      if(part is None):
        pos = Position()
        pos._x = xt
        pos._y = y
        self._positions.append(pos)
      else:
        # peca de cores diferentes
        if(part._color != self._color):
          pos = Position()
          pos._x = xt
          pos._y = y
          self._positions.append(pos)
        break
      xt = xt +1

    yt = y - 1
    while(yt >= 0):
      part = board.get_peca(x, yt)
      if(part is None):
        pos = Position()
        pos._x = x
        pos._y = yt
        self._positions.append(pos)
      else:
        # peca de cores diferentes
        if(part._color != self._color):
          pos = Position()
          pos._x = x
          pos._y = yt
          self._positions.append(pos)
        break
      yt = yt -1

    yt = y + 1
    while(yt <= 7):
      part = board.get_peca(x, yt)
      if(part is None):
        pos = Position()
        pos._x = x
        pos._y = yt
        self._positions.append(pos)
      else:
        # peca de cores diferentes
        if(part._color != self._color):
          pos = Position()
          pos._x = x
          pos._y = yt
          self._positions.append(pos)
        break
      yt = yt +1
    
    for p in self._positions:
      print(str(p))

class Pawn(Part):
  _mark_white = "♙"
  _mark_black = "♟"

  def __init__(self, color):
    Part.__init__(self, "Peão", color)

  def recalc(self, board, x, y):
    pass