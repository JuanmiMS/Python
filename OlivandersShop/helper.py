def changeAtributesToInt(lista, lenLista):
    """
    :param lista: entra un lista con los objetos y sus atributos
    :param lenLista: entra el tamaño de la lista anteriormente medido
    :return: si el cambio ha sido correcto devolvera un True, en caso contrario devolvera False
    """
    try:
        assert isinstance(lista, list), 'No es una lista'
        assert isinstance(lenLista, int), 'No es un entero'
        assert len(lista) >= 2 and len(lista)==lenLista, 'Lista demasiado pequeña'

        for position in range(1, lenLista):
            lista[position] = int(lista[position])
        return True
    except:
        return False

if __name__ == "__main__":
    lista = [1,2,3,4]
    assert (fixList(lista, len(lista))), 'Fallo caso test 1'
    lista = [1, 2, 'a', 4]
    assert (fixList(lista, len(lista))) == False, 'Fallo caso test 2'
    lista = []
    assert (fixList(lista, len(lista))) == False, 'Fallo caso test 3'
    lista = 'esto es una frase'
    assert (fixList(lista, len(lista))) == False, 'Fallo caso test 4'
    lista = [1, 2]
    assert (fixList(lista, len(lista))), 'Fallo caso test 5'

    print('Casos test pasados')
