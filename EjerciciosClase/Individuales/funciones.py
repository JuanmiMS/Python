# Pasar por copia ("paso por referencia" en java y C)
# Cada bloque de código define un nuevo ámbito
X = 88

def func():
    X = 99
    return X
print (func())
print(X)

#Tranforma la variable acion en una función
action = func()
action()