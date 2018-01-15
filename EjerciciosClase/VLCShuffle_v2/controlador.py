#Encargado de recibir las canciones, randomizarlas y mandarlas al archivo principal

import random
import modelo

import xml.etree.ElementTree as ET


def prepararObjetoDatos(*args):
    # (ruta acceso, parametros configuración)
    # Open Closed Principle
    # Con un diccionario simulamos el comportamiento
    # de un switch-case.
    # La extensión del archivo sirve como clave del diccionario.
    # El valor es un string con el nombre de la funcion a invocar.
    # No conseguimos un OCP estricto porque es necesario modificar
    # el diccionario (aunque solo sea extendiendolo) para incluir
    # nuevos tipos de ficheros.

    posicionExtension = args[0].index('.')
    extensionFichero = args[0][posicionExtension + 1:]
    # Hay que impedir que la funcion se ejecute al construir el diccionario
    operaciones = {"xml": "prepararXML" + str(tuple(args)),
                   "xspf": "prepararXML" + str(tuple(args)),
                   "txt": "prepararTXT" + str(tuple(args))
                   }

    # Devolvemos la funcion adecuada:
    # prepararXML(data, xmlns)
    # prepararTXT(data, argumento)
    # eval provoca que se ejecute la funcion
    return eval(operaciones[extensionFichero])


def prepararXML(data, xmlns):

    arbol = ET.parse(data)
    root = arbol.getroot()

    trackList = root.find("xmlns:trackList", xmlns)

    libreria = {track.find("xmlns:title", xmlns).text:
                {
                    "artist": track.find("xmlns:creator", xmlns).text,
                    "album": track.find("xmlns:album", xmlns).text,
                    "location": track.find("xmlns:location", xmlns).text
                }
                for track in trackList}

    return libreria


def prepararTXT(data, opciones):
    # mock function
    return "fichero de texto"



def lenLibrary(libreria):

    #La librería tiene que ser mayor que 1 o salta el assert
    assert int(len(libreria) > 1), "La librería tiene que contener al menos un elemento"
    assert isinstance(len(libreria), int), "no es un integer"
    return len(libreria)

def makePlaylist(libreria):

    assert isinstance(libreria, dict), "no es un diccionario"
    cpLib = libreria.copy()
    tam = lenLibrary(libreria)
    shuffled = {}
    index = 1

    while index <= tam:
        selectedKey = random.choice(list(cpLib.keys()))
        shuffled.update({index: selectedKey})
        index += 1
        del cpLib[selectedKey]
    return shuffled