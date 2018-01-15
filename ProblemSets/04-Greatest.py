# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

numeros = [4, 23, 1, 12, 444]
def greatest(numeros):
    mayor = 0
    for num in numeros:
        if num > mayor:
            mayor = num
        else:
            pass
    print(mayor)

greatest(numeros)

#print greatest([4,23,1])
#>>> 23
#print greatest([])
#>>> 0