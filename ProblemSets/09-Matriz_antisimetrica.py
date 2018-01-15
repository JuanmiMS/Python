# Define una rutina que devuelve True si una matriz es
# atisimetrica y False en otro caso.
# Una matriz n*n es antisimetrica si se verifica que
# sus elementos mantienen la relación:
# matriz[i][j] = - matriz[j][i]
# para cada i=0,1,...,n-1 y para cada j=0,1,...,n-1.

def esCuadrada(matriz):
    return len(matriz) == len(matriz[0])

def esAntisimetrica(matriz):
    try:
        if len(matriz) == 0:
            return 'Matriz vacía'
        for row in range(0, len(matriz)):
            for column in range(0, len(matriz[row])):
                if not esCuadrada(matriz) or matriz[row][column] != -matriz[column][row]:
                    return False
        return True
    except TypeError:
        return False





# Casos Test:
print(esAntisimetrica([5]))
print(esAntisimetrica ([[0, 1, 2],
                       [-1, 0, 3],
                       [-2, -3, 0]]))
    # >>> True

print(esAntisimetrica ([[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]))
#>>> True

print(esAntisimetrica ([[0, 1, 2],
                        [-1, 0, -2],
                        [2, 2,  3]]))
#>>> False

print(esAntisimetrica([[1, 2, 5],
                        [0, 1, -9],
                        [0, 0, 1]]))
#>>> False

# casos test que no satisfacen la precondicion de que la matriz sea cuadrada (assert)

matriz4 = [[1, 0, 0, 0],
           [0, 1, 1, 0],
           [0, 0, 0, 1]]

print(esAntisimetrica(matriz4))
#>>>False

matriz5 = [[1, 0, 0, 0, 0, 0, 0, 0, 0]]

print(esAntisimetrica(matriz5))
#>>>False"""