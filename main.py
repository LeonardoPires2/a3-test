from src.chess import Chess
from src.terminal import T_BGREEN, T_RESET

print(T_BGREEN, "                    ", T_RESET)
print(T_BGREEN, "Bem-vindo ao Xadrez!", T_RESET)
print(T_BGREEN, "                    ", T_RESET)
chess = Chess()
chess.play()