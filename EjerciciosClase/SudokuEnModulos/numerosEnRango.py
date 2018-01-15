def numerosEnRango(sudoku):

    numerosValidos = range(0, len(sudoku) + 1)

    for fila in sudoku:

        for numero in fila:

            if numero not in numerosValidos:
                return False

    return True
"""
if __name__ == '__main__':
    import CasosTest
    CasosTest.ejecutarCasosTest(numerosEnRango)

"""

if __name__ == '__main__':
    import CasosTest

    for element in list(CasosTest.__dict__.keys()):
        if not '__' in element:
            print(element,'--', numerosEnRango(CasosTest.__dict__.get(element)))
