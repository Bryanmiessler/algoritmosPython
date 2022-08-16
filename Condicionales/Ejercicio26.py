edad = int(input('Indicanos tu edad: '))

if edad >= 0 and edad <= 9:
    print('Para las edades entre 0 y 9 años la tasa de letalidad es de 0.0')
elif edad >= 10 and edad <= 19:
    print('Para las edades entre 10 y 19 años la tasa de letalidad es de 0.2')
elif edad >= 20 and edad <= 29:
    print('Para las edades entre 20 y 29 años la tasa de letalidad es de 0.2')
elif edad >= 30 and edad <= 39:
    print('Para las edades entre 30 y 39 años la tasa de letalidad es de 0.2')
elif edad >= 40 and edad <= 49:
    print('Para las edades entre 40 y 49 años la tasa de letalidad es de 0.4')
elif edad >= 50 and edad <= 59:
    print('Para las edades entre 50 y 59 años la tasa de letalidad es de 1.3')
elif edad >= 60 and edad <= 69:
    print('Para las edades entre 60 y 69 años la tasa de letalidad es de 3.6')
elif edad >= 70 and edad <= 79:
    print('Para las edades entre 70 y 79 años la tasa de letalidad es de 8.0')
elif edad > 80:
    print('Para las edades mayores a 80 años la tasa de letalidad es de 14.8')
else:
    print('Introduzca una edad valida')