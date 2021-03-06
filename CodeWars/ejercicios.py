#Devuelve el número de años, días, horas, minutos y segundos para
#la cantidad de segundos introducida.
def tiempo(seconds):
    restante = seconds
    time = [['year', 365 * 3600 * 24, 0], ['day', 3600 * 24, 0], ['hour', 3600, 0], ['minute', 60, 0],
            ['second', 1, 0]]
    index = 0
    final = []
    #Si los segundos != 0, significa que no es ahora y entra a calcularlos
    if seconds != 0:
        while restante != 0:
            restante = restante - time[index][1]
            if restante < 0:
                restante = restante + time[index][1]
                index += 1
            else:
                time[index][2] += 1
        #Ahora ya tenemos la cantidad de H,M y S calculados y metidos en la lista time.
        i = 0
        for dates in time:
            if time[i][2] != 0:
                if time[i][2] > 1:
                    final.append(str(time[i][2]) + ' ' + time[i][0] + 's')
                else:
                    final.append(str(time[i][2]) + ' ' + time[i][0])
            i += 1
        #Devolvemos el resultado, pero bonito ;D
        if len(final) == 1:
            return ''.join(final)
        else:
            return ', '.join(final[:-1]) + ' & ' + final[-1]
    else:
       return 'now'
    return final

#buscar a neo dentro de Matrix

"""
Esto es matrix
1  5  10 19 21
7  9  13 23 24
11 12 30 35 36
33 40 50 55 57
58 59 60 61 62 

Neo es el 12, ¿En qué fila y columna está?
PD: el mundo es correcto (sin fallos a propósito)
"""

def makeMatrixCuadrada():
    num = 100
    columna = 0
    fila = 0
    matriz = []
    numero = 0

    #crea una matriz de 100x100
    for i in range(0, num):
        new = []
        for j in range(0, num):
            new.append(numero)
            numero+=1
        matriz.append(new)
    return matriz
#makeMatrixCuadrada()

def finding_neo(neo, matrix):
    print(matrix)
    fila = 0
    columna = 0
    for mundo in matrix:
        columna = 0
        for lugar in mundo:
            if lugar == neo:
                found = 'Encontrado!!! Fila:' + str(fila) +' Columna: ' + str(columna)
                return found
            columna+=1
        fila +=1

    return neo

#print(finding_neo(133, makeMatrixCuadrada()))    

def count_positives_sum_negatives(arr):
    # Creamos una lista, la posición 0 serán los números positivos
    # La posición 1 serán los negativos
    final = [0, 0]
    # Si la lista que nos dan es diferente a "vacía"
    if len(arr) != 0:
        # En este caso es mejor usar el bule For y no el While, ya que sabemos
        # cuantas veces recorremos la lista.
        for number in arr:
            if number <= 0:
                final[1] = final[1] + number
            else:
                final[0] += 1
        return final
    # Si pasa a este else es por que está vacía, entonces la devolvemos tal y como nos viene
    else:
        return arr