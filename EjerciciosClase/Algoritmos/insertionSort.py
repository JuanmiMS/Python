import matplotlib.pyplot as plt
from random import shuffle

def createRandomList(length):
    assert isinstance(length, int), 'Length tiene que ser un entero'
    # recibe como parametro la longitud de la lista
    # crea una lista de numero enteros
    # la "mezcla" = desordena
    lenLista = [number for number in range(1, length+1)]

    assert len(lenLista) == length, 'La longitud no coincide'
    # devuelve la lista
    shuffle(lenLista)

    return lenLista

def display(lista, index):

    plt.clf()
    plt.bar(range(len(lista)), lista)
    plt.savefig("imgs/img" + '%04d' % index + ".png")
    plt.draw()


def less(a, b):
    # comprueba si a es menor que b
    # devuelve un boolean
    # recibe dos elementos
    # ojo a si el algoritmo de ordenacion es estable o inestable
    return a < b



def exchange(lista, i, j):
    # intercambia dos elementos de posicion en la lista
    # recibe la lista, la posicion i y la posicion j
    # devuelve None
    # comprueba que se han intercambiado los elementos
    lista[i], lista[j] = lista[j], lista[i]
    assert lista[i] <= lista[j], 'No se han intercambiado los valores'



def isExchanged(lista, i, j):
    # comprueba si el elemento en la posicion i
    # es menor que el elemento en la posicion j
    # devuelve un boolean
    assert less(lista[i], lista[j]), 'El primer elemento es mayor que el segundo'
    return less(lista[i], lista[j])


def isSorted(lista):
    # comprueba si la lista esta oredenada
    # devuelve un boolean
    return sorted(lista) == lista


def insertionSort(lista):
    import time
    # ordena la lista segun el algoritmo de ordenacion
    # bubble sort
    # cada vez que se intercambian dos elementos se dibuja la lista:
    # llama a display(lista)
    # devuelve None
    # Comprueba que la lista esta ordenada

    #Por si la lista que se pasa ya está ordenada
    if isSorted(lista):
        display(lista)
    else:
        index = 0
        #print('Lista inicial: ', lista)
        while not isSorted(lista):
            for index in range(1, len(lista)):

                currentvalue = lista[index]
                position = index

                while position > 0 and lista[position - 1] > currentvalue:
                    lista[position] = lista[position - 1]
                    position = position - 1


                lista[position] = currentvalue
                display(lista, index)


#Casos Test
if __name__ == "__main__":

    plt.ion()
    lista = createRandomList(15)
    insertionSort(lista)
    isSorted(lista)
    plt.show(block=True)

    # Listas de strings como casos test #
    # desactivar display() en bubbleSort()

    for test in open("stringTestCases.txt", 'r'):
        testList = list(test.replace(' ', ''))
        insertionSort(testList)
        assert isSorted(testList), "Test %s " % (str(test))

    print("string test cases passed")
