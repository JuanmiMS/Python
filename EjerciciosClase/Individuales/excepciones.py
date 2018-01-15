sep = '-' * 45 + '\n'
print(sep + 'NO EXCEPTION RAISED')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')
#-----------------------
print(sep + 'EXCEPTION RAISED BUT NOT CAUGHT')
try:
    x = 1 / 0
except ZeroDivisionError:
    print('yeah boi')
finally:
    print('finally run')
print('after run')