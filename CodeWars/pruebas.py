import time

print(time.strftime("%d days, %H hours, %M minutes and %S seconds", time.gmtime(3662)))


#Casos test
""""
print("1 second : ", ejer1(1))
print("1 minute : ", ejer1(120))
print("1 hour, 1 minute and 2 seconds : ", ejer1(3662))
print("11231231 ", ejer1(365*24*3600))
"""