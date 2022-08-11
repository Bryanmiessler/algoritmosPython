# Realice un algoritmo que lea el número de un documento y 
# muestre un mensaje indicando el día de atención de acuerdo a los siguientes criterios.
# Si termina en 0 ó 1 el día de atención es lunes.
# Si termina en 2 ó 3 el día de atención es martes.
# Si termina en 4 ó 5 el día de atención es miércoles
# Si termina en 6 ó 7 el día de atención es jueves.
# Si termina en 8 ó 9 el día de atención es viernes.
numDoc = input('Introduzca su documento de identidad:')
ultNumero = numDoc[-1]

if ultNumero == '0' or ultNumero == '1':
    print('El día destinado para su atención son los lunes')
elif ultNumero == '2' or ultNumero == '3':
    print('El día destinado para su atención son los martes')
elif ultNumero == '4' or ultNumero == '5':
    print('El día destinado para su atención son los miercoles')
elif ultNumero == '6' or ultNumero == '7':
    print('El día destinado para su atención son los jueves')
elif ultNumero == '8' or ultNumero == '9':
    print('El día destinado para su atención son los viernes')
else:
    print('Ingrese solo numeros')