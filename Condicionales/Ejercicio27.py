import math

a = float(input('Ingrese el valor de "a": '))
b = float(input('Ingrese el valor de "b": '))
c = float(input('Ingrese el valor de "c": '))
signo = input('Ingrese el signo que desea usar en la operación(+ o -): ')

if signo == '+':
    resultadoSuma = (-b + math.sqrt((b**2) - (4*a*c))) / 2*a
    print('El resultado de la operación con el signo suma es:', resultadoSuma)
elif signo == '-':
    resultadoResta = (-b - math.sqrt((b**2) - (4*a*c))) / 2*a
    print('El resultado de la operación con el signo resta es:', resultadoResta)
else:
    print('Ingrese el signo + o -')