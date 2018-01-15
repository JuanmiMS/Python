#Lista2 apunta a la dirección de memoria a la que apunta lista1

lista1 = [10, 20, 30]
#Lista2 apunta a la dirección de memoria a la que apunta lista1
lista2 = lista1
print (lista2)
lista1 = [3, 5, 7]
print (lista1)
print (lista2)
lista2 = lista1
print (lista1)
print (lista2)

