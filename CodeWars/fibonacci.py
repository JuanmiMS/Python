def fib(n):
    fiboDics = {0: 0, 1: 1}

    def fiboMemoization(n):

        nonlocal fiboDics

        if n in fiboDics:
            return fiboDics[n]
        else:
            fiboDics[n] = fiboMemoization(n - 1) + fiboMemoization(n - 2)
            return fiboDics[n]

    return fiboMemoization(n)


#Otra manera de hacer fibonacci
def fib2(n):
    return 1 if n == 1 else fib(n-1)+fib(n-2)



print(fib2(100))

# Casos test
fiboNumbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

for num in range(0, len(fiboNumbers)):
    assert fib(num) == fiboNumbers[num], 'hey'

assert fib2(100) == 354224848179261915075, 'fib(100) failed'
assert fib2(251) == 12776523572924732586037033894655031898659556447352249, 'fib(251) failed'
#fin casos test