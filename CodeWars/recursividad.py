listaNums = []
listaCiclosRep = []
cyc_patt_arr = []
patt_len = 0
last_term = 0 #solucionar esto
h = 0 #solucionar esto
def sum_pow_dig_seq(start, n, k):

    if k==0: #cambiar el -2 por 0 si da fallo. con el -2 el output es el mismo que en codewars

        patt_len = len(cyc_patt_arr)
        last_term = start
        #[12, [13139, 6725, 4338, 4514, 1138, 4179, 9219], 7, 1138])

        print(h, cyc_patt_arr, patt_len, last_term)

        return [h, cyc_patt_arr, patt_len, last_term]
        #cyc_patt_arr es una lista en la que aparecen los números que se repiten
        #patt_len = len(cyc_patt_arr)
    else:
        result = 0
        for number in list(map(int, str(start))):
            result = result + number ** n

        #print("start", start)
        #print("start", listaNums)

        if result in listaNums:
            if result in listaCiclosRep:
                cyc_patt_arr.append(result)
            else:
                listaCiclosRep.append(result)


        #print("Repes", listaCiclosRep)
        h[0] += 1
        listaNums.append(start)
        sum_pow_dig_seq(result, n, k-1)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(100))
#print(sum_pow_dig_seq(420, 4, 30))