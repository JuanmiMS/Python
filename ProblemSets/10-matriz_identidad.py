# Dada una lista de lista representando una matriz n*n:
# Define una rutina que devuelve True si la entrada es una matriz indentidad
# y False en otro caso.

# Una matriz identidad es una matriz cuadrada en la que todos los elementos
# en la diagonal principal son 1 y el resto de elementos fuera de la
# diagonal principal son 0.
# (Una matriz cuadrada es una matriz con el numero de filas
# igual al numero de columnas)
def esCuadrada(matriz):
    if len(matriz) == len(matriz[0]):
        return len(matriz) == len(matriz[0])
def esMatrizIdentidad(matriz):
    try:
        if len(matriz) == 0 or not esCuadrada(matriz):
            return False
        for row in range(0, len(matriz)):
            for column in range(0, len(matriz[row])):
                if row == column and matriz[row][column] != 1:
                    return False
                elif row != column and matriz[row][column] != 0:
                    return False
        return True

    except TypeError:
        return False

    # Escribe tu codigo aqui



# Casos test:

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
print ("True:", esMatrizIdentidad(matrix1))
#>>>True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print("False:", esMatrizIdentidad(matrix2))
#>>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

print ("False:", esMatrizIdentidad(matrix3))
#>>>False

matrix6 = [[1,0,0,0],
           [0,1,0,2],
           [0,0,1,0],
           [0,0,0,1]]

print ("False:", esMatrizIdentidad(matrix6))
#>>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print ("False:", esMatrizIdentidad(matrix7))
#>>>False


# casos test que no satisfacen la precondicion de que la matriz sea cuadrada (assert):

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print ("False:",esMatrizIdentidad(matrix4))
#>>>False

matrix5 = [[1,0,0,0,0,0,0,0,0]]

print ("False:", esMatrizIdentidad(matrix5))
#>>>False
