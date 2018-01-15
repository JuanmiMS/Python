def fun1():
    print("Bienvenido a uno de los mejores programas",
          "de Phyton")
    print("Introduzca un numero: ")
    num = int(input())
    print("Numero: ", num, "Numerox2: ", num * 2, "Numerox3:",
          num * 3)
def fun2y3():
    NUM_PI = 3.14
    print("Introduzca el radio de una circunferencia: ")
    num = int(input())

    # el método round(algo, numero) se utiliza para redondear
    print("Longitud:", round(2 * NUM_PI * num, 3))
    print("Area: ", round(NUM_PI * num ** 2, 3))
def fun4():
    print("Introduzca la altura: ")
    alto = int(input())
    print("Introduzca la anchura: ")
    ancho = int(input())
    print("Área: ", alto * ancho, "metros")
    print("Perímetro exterior: ", 2 * (alto + ancho), "metros")
def fun5():
    print("¿Cuanto cobras?: ")
    money = float(input())
    retenido = money * 0.20
    money = money - money * 0.20

    print("Dinero restante: ", money, "€. Dinero retenido: ", retenido, "€")
def fun6():
    print("¿Introduce el primer número: ")
    numUno = int(input())
    print("¿Introduce el segundo número: ")
    numDos = int(input())

    print("El primer número introducido es: ", numUno)
    print("Els egundo número introducido es: ", numDos)

    numAux = numUno
    numUno = numDos
    numDos = numAux

    print("El número 1 cambiado es: ", numUno)
    print("El número 2 cambiado es: ", numDos)
def fun7():
    print("Introduce un número: ")
    num = int(input())

    if num < 0:
        print("Es negativo")
    else:
        print("Es positivo")
def fun8():
    print("¿Cuanto cobras?: ")
    money = float(input())
    retenido = money * 0.20
    money = money - money * 0.20

    print("Dinero restante: ", money, "€. Dinero retenido: ", retenido, "€")
def fun9():
    print("Primer número entero")
    numA = int(input())
    print("Segundo número entero")
    numB = int(input())
    if numA>=0 and numB >=0:
        print("La suma de los dos números es: ", numA+numB)
    else:
        print("No se calcula la suma porque alguno de los números o los dos no son positivos")
def fun10():
    print("Primer número entero")
    numA = int(input())
    print("Segundo número entero")
    numB = int(input())

    if numA<0 and numB<0:
        print("No se calcula la suma porque los dos números son negativos.")
    else:
       if numA>=0 and numB<0:
           print("No se calcula la suma porque el segundo número es negativo")
       if numB>=0 and numA<0:
           print("No se calcula la suma porque el primer número es negativo")
       if numA>=0 and numB>=0:
           print("La suma de los dos números es: ", numA+numB)
def fun11():
    print("Primer número entero")
    numA = int(input())
    print("Segundo número entero")
    numB = int(input())
    print("Tercer número entero")
    numC = int(input())

    if numA == numB + numC:
        print("Se cumple que N1 = N2 + N3,",numA,"=", numB,"+", numC)
    elif numB == numA + numC:
        print("Se cumple que N2 = N1 + N3,",numB,"=", numA,"+", numC)
    elif numC == numB + numA:
        print("Se cumple que N3 = N1 + N2,",numC,"=", numA,"+", numB)
    else:
        print("Los números no cumplen la condición")
def fun12():
    print("Primer número entero")
    numA = int(input())
    print("Segundo número entero")
    numB = int(input())
    def intervalos(numero):
        if numero>=100 and numero <=150:
            return True
        else:
            return False

    if numA%2 == 0 and numB%2 == 0 and numA<50 and intervalos(numB)==True:
        print("La suma de ambos números es:", numA+numB)
    else:
        print("Error")
def fun13():
    print("Indique un valor de venta: ")
    numA = float(input())

    if numA <= 20:
        print("Descuento del 0%, se le queda un total de ",numA,"€")
    elif numA > 20 and numA <= 100:
        numA = numA -(numA*0.05)
        print("Descuento del 5%, se le queda un total de ", numA, "€")
    elif numA > 100:
        numA = numA - (numA * 0.10)
        print("Descuento del 10%, se le queda un total de ", numA, "€")
def fun14(): #Refactorizar
    dinero = [100, 50, 20, 10, 5, 2, 1]
    print("Introduzca una cantidad: ")
    cantidad = int(input())
    cantidadDinero = [0, 0, 0, 0, 0, 0, 0]

    index = 0
    while cantidad != 0:
        cantidad = cantidad - dinero[index]
        if cantidad < 0:
            cantidad = cantidad + dinero[index]
            index += 1
        else:
            cantidadDinero[index] = cantidadDinero[index] + 1
    i = 0
    for total in cantidadDinero:
        if total != 0:
            print(total, "billetes de ", dinero[i], "euros")
        i = i + 1
def fun15():
    index = 0
    while index < 5:
        print("estamos estudiando metodología de la programación.",)
        index += 1
def fun16():
    natural = 1
    suma = 0
    while natural <= 30:
        suma = suma + natural
        natural += 1
    print("La media aritmética es: ", suma/30)
def fun17():
    print("Introduce el primer número: ")
    numStart = int(input())
    print("Introduce el segundo número: ")
    numEnd = int(input())
    #Primera posición almacena los números pares, la segunda los impares
    parInpar = [0,0]

    #Si el primer número es mayor que el segundo, cambia los valores
    if numEnd < numStart:
        aux = numStart
        numStart = numEnd
        numEnd = aux

    while numStart <= numEnd:
        if numStart%2 == 0:
            parInpar[0] = parInpar[0]+numStart
        else:
            parInpar[1] = parInpar[1]+numStart
        numStart+=1
    print("Suma de números pares: ", parInpar[0])
    print("Suma de números impares: ", parInpar[1])
def fun18():
    print("Introduce un número: ")
    num = int(input())
    index = 1
    resultados = []
    if num < 1:
        print("Error, el número tiene que ser mínimo 1")
    else:
        while index <= num:
            resultados.append(2*index)
            index +=1
    print(resultados)
def fun19y20():
    numeros = []

    #Creamos una función que pida un número y compruebe si es positivo
    def pedirNumero():
        print("Introduzca un número: ")
        num = int(input())
        if num<0:
            print("Número negativo no permitido!!")
            pedirNumero()
        else:
            numeros.append(num)

    #Bucle para pedir los números 5 veces
    index = 0
    while index < 5:
        pedirNumero()
        index += 1
    index = 0
    for nums in numeros:
        if nums >= numeros[0]:
            numeros[0] = nums
            index +=1
    print("El numero mayor es: ", numeros[0])
def fun21():
    numeros = []

    # Creamos una función que pida un número y compruebe si es positivo
    def pedirNumero():
        print("Introduzca un número: ")
        num = int(input())
        if num < 0:
            print("Número negativo no permitido!!")
            pedirNumero()
        else:
            numeros.append(num)

    # Bucle para pedir los números 5 veces
    index = 0
    while index < 5:
        pedirNumero()
        index += 1
    index = 0
    mayor = numeros[0]
    menor = numeros[0]
    for nums in numeros:
        if nums >= mayor:
            mayor = nums
        elif nums <= menor:
            menor = nums
        index += 1
    print("Mayor: ", mayor, "Menor: ", menor)
def fun22():
    numeros = []
    # Creamos una función que pida un número y compruebe si es positivo
    def pedirNumero():
        print("Introduzca un número: ")
        num = int(input())
        if num < 0:
            print("Número negativo no permitido!!")
            pedirNumero()
        else:
            numeros.append(num)
    numN = 0
    while numN <=0:
        print("Introduzca cuántos números tienen que leerse por teclado: ")
        numN = int(input())
        if numN <=0:
            print("Numeros negativos no permitidos")

    index = 0
    while index < numN:
        pedirNumero()
        index += 1
    index = 0
    mayor = numeros[0]
    menor = numeros[0]
    for nums in numeros:
        if nums >= mayor:
            mayor = nums
        elif nums <= menor:
            menor = nums
        index += 1
    print("Mayor: ", mayor, "Menor: ", menor)


fun14()
