def group_by_commas(n):

    stringReturned = ''
    print('{:,.0f}'.format(n))
    numsLeft = len(str(n))

    for number in str(n):
        print(number)
        if str(n).index(number)%2 == 0:
            stringReturned = stringReturned + ',' + number
        else:
            stringReturned = stringReturned + number

    return stringReturned

#print('1,000,253 : ',group_by_commas(1000253))


def velocidad_ram(mh, cl):
    result = round(((1/mh)* cl)*1000, 4)
    #Mas alto = peor.
    return 'Resultado: '+str(result)+' NS'

print(velocidad_ram(1866, 9))