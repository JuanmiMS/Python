# encoding: utf-8
#Creacin de un programa para la comprobar si un sudoku es correcto

import esCuadrado, checkNumerosValidos, checkFilasAndColumnas

def check_sudoku(sudoku):

    return esCuadrado.esCuadrado(sudoku) and checkNumerosValidos.checkNumerosValidos(sudoku) \
           and checkFilasAndColumnas.checkFilas(sudoku) and checkFilasAndColumnas.checkColumnas(sudoku)


if __name__ == '__main__':
    import CasosTest


    for element in list(CasosTest.__dict__.keys()):
        if not '__' in element:
            print(element,'--', check_sudoku(CasosTest.__dict__.get(element)))
