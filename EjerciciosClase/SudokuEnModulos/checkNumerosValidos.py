import sonNumerosEnteros, numerosEnRango

def checkNumerosValidos(sudoku):


    return sonNumerosEnteros.sonNumerosEnteros(sudoku) and numerosEnRango.numerosEnRango(sudoku)

if __name__ == '__main__':
    import CasosTest

    for element in list(CasosTest.__dict__.keys()):
        if not '__' in element:
            print(element,'--', checkNumerosValidos(CasosTest.__dict__.get(element)))

