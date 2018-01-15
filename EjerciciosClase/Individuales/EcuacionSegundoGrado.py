# Ejercicio 3
import math
# variables de la ecuación de segundo grado
a = int(input())
b = int(input())
c = int(input())

# comprobar si la raiz es negativo
inRaiz = b * b - 4 * a * c
if inRaiz >= 0 and a != 0:
    outRaiz = math.sqrt(inRaiz)  # Raiz hecha :D

    # Imprimir resultados
    print('Primer resultado: ', round(((-b + outRaiz) / (2 * a)), 2))
    print('Segundo resultado: ', round(((-b - outRaiz) / (2 * a)), 2))
else:
    print("Imposible su solución")
