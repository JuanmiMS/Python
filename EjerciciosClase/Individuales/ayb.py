A = ["spam"]
# Con A[:] copia toda la lista sin modificarla.
B = A[:]
# Con A asigna la dirección de memoria a B, pudiendo modificar la lista
#B = A
B[0] = "shrubbery"
print(A)
