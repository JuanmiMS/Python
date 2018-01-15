# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

numeros = [9]

def product_list(numbers):
    sum = 1
    for num in numbers:
        sum = sum * num

    return (sum)

product_list(numeros)


#print product_list([9])
#>>> 9

#print product_list([1,2,3,4])
#>>> 24

#print product_list([])
#>>> 1