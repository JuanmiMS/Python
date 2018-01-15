def sonNumerosEnteros(sudoku):

    for fila in sudoku:

        for numero in fila:

            if not isinstance(numero, int):
                return False

    return True

if __name__ == '__main__':
    import CasosTest

    for element in list(CasosTest.__dict__.keys()):
        if not '__' in element:
            print(element,'--', sonNumerosEnteros(CasosTest.__dict__.get(element)))