#Conjunto de casos test para probar que cada uno de los modulos funcionan

correcto = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]
incorrecto = [[1, 2, 3],
              [2, 3, 1],
              [2, 3, 1]]
incorrecto1 = [[1, 2, 3, 4],
               [2, 3, 1, 3],
               [3, 1, 2, 3],
               [4, 4, 4, 4]]
incorrecto2 = [[1, 2, 3, 4],
               [2, 3, 1, 4],
               [4, 1, 2, 3],
               [3, 4, 1, 2]]
incorrecto3 = [[1, 2, 3, 4, 5],
               [2, 3, 1, 5, 6],
               [4, 5, 2, 1, 3],
               [3, 4, 5, 2, 1],
               [5, 6, 4, 3, 2]]
incorrecto4 = [['a', 'b', 'c'],
               ['b', 'c', 'a'],
               ['c', 'a', 'b']]
incorrecto5 = [[1, 1.5],
               [1.5, 1]]
incorrecto6 = [[1, 0, 0, 0],
               [0, 1, 0],
               [0, 0, 0, 1]]
incorrecto7 = [[1, 0, 0],
               [0, 1, 0],
               [0, 0, 0, 1]]
incorrecto8 = [[]]
correcto2 = [[0, 1, 2],
             [1, 2, 0],
             [2, 0, 1]]


casosTest = []
for element in dir():
    if not '__' in element:
        casosTest.append(element)

if __name__ == '__main__':
    import CasosTest

    for element in list(CasosTest.__dict__.keys()):
        if not '__' in element:
            print(CasosTest.__dict__.get(element))
