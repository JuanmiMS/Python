import random
#abre el vlc
#os.system("E:/Programas/VLC/vlc.exe")

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

#Comprueba que la librería sea mayor de 1
def lenLibrary(libreria):

    #La librería tiene que ser mayor que 1 o salta el assert
    assert int(len(libreria) > 1), "La librería tiene que contener al menos un elemento"
    assert isinstance(len(libreria), int), "no es un integer"
    return len(libreria)

def playShuffleVLC(libreria, playList):
    import subprocess
    import shlex
    import os
    print("PLAAAAAYY:", playList)
    #pathVLC = "D:\\Programas\\VLC"
    #lineaVLC = "D:\\Programas\\VLC\\vlc.exe"
    #Portatil
    lineaVLC = "E:\\Programas\\VLC\\vlc.exe"
    for songNum in sorted(playList.keys()):
        titulo = playList[songNum]
        ubicacion = libreria[titulo]['location']
        print('UBI', ubicacion)
        lineaVLC = lineaVLC + " " + str(ubicacion)
        #abre VLC
        print("ARGUMENTOS: ", lineaVLC)
    procesoVLC = subprocess.Popen(lineaVLC)




playList = {}
# playList ={ 1: "titulo cancion", 2: "titulo cancion" ... }


libreria = {"California_Uber_Alles.mp3":
                {"track-number": 3, "artist": "Dead Kennedys", "album": "Dead Kennedys", "location": ".\\biblioteca\\California_Uber_Alles.mp3"},
            "Seattle_Party":
                {"track-number": 1, "artist": "Chastity Belt", "album": "No regrets", "location": ".\\biblioteca\\Seattle_Party.flac"},
            "King_Kunta":
                {"track-number": 3, "artist": "Kendrick Lamar", "album": "To Pimp A Butterfly", "location": ".\\biblioteca\\King_Kunta.mp3"}
            }

playList = makePlaylist(libreria)
print("librería2: ", libreria)
playShuffleVLC(libreria, playList)
