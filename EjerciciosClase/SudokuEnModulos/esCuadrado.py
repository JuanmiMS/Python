def esCuadrado(sudoku):

    numeroFilas = len(sudoku)

    for fila in sudoku:

        if len(fila) != numeroFilas:
            return False

    return True

"""
if __name__ == '__main__':
    import CasosTest
    CasosTest.ejecutarCasosTest(esCuadrado)
"""

if __name__ == '__main__':
    import CasosTest

    for element in list(CasosTest.__dict__.keys()):
        if not '__' in element:
            print(element,'--', esCuadrado(CasosTest.__dict__.get(element)))
