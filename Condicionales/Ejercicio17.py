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
    