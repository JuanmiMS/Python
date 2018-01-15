#Números primos hasta N

def esPrimo(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def numerosPrimos(numero):
    numsPrimos = []
    for i in range(2, numero+1):
        if esPrimo(i):
            numsPrimos.append(i)

    print(numsPrimos)

print(esPrimo(2))
numerosPrimos(13)