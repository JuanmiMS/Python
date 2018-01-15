def namelist(names):
    print(0, names)
    if len(names) < 1:
        nameList = []
        for name in names:
            nameList.append(name['name'])

        return nameList[0]
    else:
        returnedString = ''
        nameList = []
        for name in names:
            nameList.append(name['name'])

        for name in range(0, len(nameList) - 1):
            returnedString += nameList[name] + ', '

        return returnedString[:-2] + ' & ' + nameList[len(nameList) - 1]

print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]))
print(namelist([{'name': 'Bart'}]))