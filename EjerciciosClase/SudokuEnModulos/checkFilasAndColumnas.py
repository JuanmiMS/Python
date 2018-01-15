def checkFilas(sudoku):

    for fila in sudoku:

        posicionNumero = 0

        for numero in fila:
                # Averiguo si el numero se encuentra en el resto de la fila
                # El resto de la fila es una lista formada
                # desde la siguiente posicion del numero actual hasta la ultima
            if numero in fila[posicionNumero + 1:]:
                return False
            else:
                # incremento la posicion desde la que buscar
                posicionNumero += 1

    return True

def checkColumnas(sudoku):

    # Precondicion
    assert isinstance(sudoku, list), "la interfaz exige que sudoku debe ser una lista"

    numeroDeFilas = len(sudoku)

    indexFilaActual = 0

    for fila in sudoku:

        for numero in fila:

            indexFilaSiguiente = indexFilaActual + 1

            while indexFilaSiguiente < numeroDeFilas:

                try:
                    # El elemento puede no existir en la fila siguiente:
                    # index devuelve excepcion: ValueError = mensaje "x is not in list"
                    # Imposible alcanzar esta excepcion si checkColumnas se ejecuta
                    # despues de checkFilas
                    posicionNumeroFilaSiguiente = sudoku[indexFilaSiguiente].index(numero)

                except ValueError:
                    # Este bloque de codigo se ejecuta si sudoku[indexFilaSiguiente].index(numero)
                    # devuelve un error <=> si el numero no esta en la fila siguiente
                    # no llegaria a presentarse el caso pues checkNumerosEnRango se
                    # ejecuta antes
                    return False

                else:
                    # Este bloque de codigo se ejecuta si la sentencia sudoku[indexFilaSiguiente].index(numero)
                    # ha ido bien <=> el numero esta en la fila
                    if posicionNumeroFilaSiguiente == fila.index(numero):
                        return False
                    else:
                        # paso a buscar en la siguiente fila (dentro del while)
                        indexFilaSiguiente += 1

        # Cuando he chequeado los numeros de la fila actual
        # indico que paso a la fila siguiente.
        # El contador for fila in sudoku se encarga de esto.
        indexFilaActual += 1

    return True

if __name__ == '__main__':
    import CasosTest

    for element in list(CasosTest.__dict__.keys()):

        if not '__' in element:
                print(element,'--', checkColumnas(CasosTest.__dict__.get(element)))
                print(element, '--', checkFilas(CasosTest.__dict__.get(element)))
