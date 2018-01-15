""""
1- 1
2-2 3
3-4 5 6
4-7 8 9 10
print(numFila, '\t')
numFila = numFila + " " + str(num)
"""
def trianguloFloyd(numeroNaturalLimite):
    numeroActual = 1
    fila = 1

    while numeroActual <= numeroNaturalLimite:

        linea = ""
        columna = 1

        while columna <= fila:
            linea = linea + '\t' + str(numeroActual)
            numeroActual += 1
            columna += 1
        print(linea)
        fila += 1

trianguloFloyd(226)