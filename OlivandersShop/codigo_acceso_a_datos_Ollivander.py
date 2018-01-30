import helper

def accesoCasosTexttest(matrizCasosTest, rutaAccesoFichero):
    """
    :param matrizCasosTest: recibe una matriz vacia.
    :param rutaAccesoFichero: indica la ruta del fichero que se desea leer
    :return: devuelve una lista vacia en caso de error y un mensaje.
    En caso de que todo este correcto devuelve una matriz con todos los objetos de la tienda
    separados por coma.
    """
    try:
        if not isinstance(rutaAccesoFichero, str):
            raise ValueError
        fichero = open(rutaAccesoFichero, 'r')
    except FileNotFoundError:
        print("Fichero no encontrado")
        return []
    except ValueError:
        print("El nombre del fichero ha de ser un string")
        return []
    else:
        matrizCasosTest = []
        numeroPropiedadesItem = 0
        for linea in fichero:
            if linea.find("day") != -1:
                casosTestDia = []
            elif linea == "\n":
                matrizCasosTest.append(casosTestDia)
            elif linea.find("name") != -1:
                numeroPropiedadesItem = len(linea.split(','))
            else:
                item = linea.rstrip().rsplit(',', maxsplit=numeroPropiedadesItem - 1)

                if helper.changeAtributesToInt(item, numeroPropiedadesItem):
                    casosTestDia.append(item)
                else:
                    assert False, 'No se ha podido añadir el objeto'

        fichero.close()
        return matrizCasosTest


def crearFicheroCasosTest(ficheroVolcadoCasosTest, matrizCasosTest):

    """
    :param ficheroVolcadoCasosTest:El Fichero que se crea con la informacion de los objetos
    :param matrizCasosTest:Contiene una Matriz con los datos del fichero que forman los casos test.
    :return:no devuelve nada, crea un fichero ".gr" con los objetos de la tienda transformados
    """
    try:
        if not isinstance(ficheroVolcadoCasosTest, str):
            raise ValueError
        stdout = open(ficheroVolcadoCasosTest, 'w')
    except ValueError:
            print("La ruta de acceso al fichero ha de ser un string")
    else:
        for (offset, casosTestDia) in enumerate(matrizCasosTest):
            stdout.write('-' * 5 + " Dia %d: " % offset + '-' * 5 + '\n')
            for item in casosTestDia:
                stdout.write(','.join(str(item)) + '\n')
        stdout.close()


def mostrarCasosTest(matrizCasosTest):
    """
    :param matrizCasosTest: matriz con los elementos de de la tienda separados por ','
    :return: no devuelve nada, imprime por pantalla los articulos de la tienda en forma de lista
    """
    for (offset, casosTestDia) in enumerate(matrizCasosTest):
        print('-' * 5 + " Dia %d: " % offset + '-' * 5)
        for item in casosTestDia:
            print(item)


if __name__ == "__main__":

    #rutaAccesoFichero = "E:/Ejercicios-Programacion/Python/OlivandersShop/casos_test.txt"
    rutaAccesoFichero = "./casos_test.txt"
    # rutaAccesoFichero = "./stdout.gr"
    # rutaAccesoFichero = "stdout_bug_conjured.gr"

    matrizCasosTest = []

    matrizCasosTest = accesoCasosTexttest(matrizCasosTest, rutaAccesoFichero)

    mostrarCasosTest(matrizCasosTest)

    ficheroVolcadoCasosTest = "stdout.txt"

    crearFicheroCasosTest(ficheroVolcadoCasosTest, matrizCasosTest)
