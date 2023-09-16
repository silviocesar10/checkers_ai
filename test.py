from board import default, bprint, diagonal, brc
from move import check
#bprint(default())

#print(check(5,1,4,0,default()))
#print(check(2,1,3,0,default()))

#bprint(brc())

def test_moves(board, moves):
    for x0, y0, x, y, expected_result in moves:
        result = check(x0, y0, x, y, board)
        if result == expected_result:
            print(f"Movimento ({x0}, {y0}) para ({x}, {y}) foi validado corretamente.")
        else:
            print(f"Movimento ({x0}, {y0}) para ({x}, {y}) foi validado incorretamente. Deveria ser {expected_result} e deu {result}")
            bprint(board)

# Instância 1: Movimento válido de peão preto
board1 = [
    [0, -1, 0, -1, 0, -1, 0, -1],
    [-1, 0, -1, 0, -1, 0, -1, 0],
    [0, -1, 0, -1, 0, -1, 0, -1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1]
]
moves1 = [
    (5, 4, 4, 3, True),  # Movimento válido de peão preto
    (5, 4, 3, 2, True),  # Movimento válido de peão preto
    (5, 4, 3, 4, False),  # Movimento inválido - mesma coluna
    (5, 4, 4, 5, False),  # Movimento inválido - mesma diagonal
]

# Instância 2: Movimento válido de peão branco
board2 = [
    [0, -1, 0, -1, 0, -1, 0, -1],
    [-1, 0, -1, 0, -1, 0, -1, 0],
    [0, -1, 0, -1, 0, -1, 0, -1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0]
]
moves2 = [
    (2, 3, 3, 4, True),  # Movimento válido de peão branco
    (2, 3, 4, 5, True),  # Movimento válido de peão branco
    (2, 3, 1, 4, False),  # Movimento inválido - mesma coluna
    (2, 3, 3, 3, False),  # Movimento inválido - mesma diagonal
]

# Instância 3: Movimento inválido - célula ocupada
board3 = [
    [0, -1, 0, -1, 0, -1, 0, -1],
    [-1, 0, -1, 0, -1, 0, -1, 0],
    [0, -1, 0, -1, 0, -1, 0, -1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0]
]
moves3 = [
    (0, 1, 1, 2, False),  # Movimento inválido - célula ocupada por peça branca
    (5, 4, 4, 3, True),  # Movimento válido de peão preto
]

# Você pode adicionar mais instâncias de teste conforme necessário


# Você pode adicionar mais instâncias de teste conforme necessário


test_moves(board1, moves1)
test_moves(board2, moves2)
test_moves(board3, moves3)