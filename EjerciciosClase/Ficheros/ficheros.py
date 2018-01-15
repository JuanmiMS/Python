import xml.etree.ElementTree as ET

myFile = ET.parse('menu_xml.xml')
root = myFile.getroot()
newFile = open('Menu.txt', 'w')

try:
    
        nombre = element.find('name').text
        precio = element.find('price').text
        description = element.find('description').text
        calories = element.find('calories').text
        print("Name: {0} | Price: {1} | Description: {2} | Calories: {3}".format(nombre, precio, nombre, calories))
        newFile.write('Name: {0} | Price: {1} | Description: {2} | Calories: {3}'.format(nombre, precio, nombre, calories)+'\n')
finally:
    print('Archivo TXT creado!')
    newFile.close()