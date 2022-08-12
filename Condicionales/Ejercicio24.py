# Realice un algoritmo que permita leer un tipo de vehículo: Motocicleta o Carro y su placa y luego.
# Si es Motocicleta y la placa termina en 0 ó 1 mostrar "dia de pico y placa lunes"
# Si es Motocicleta y la placa termina en 2 ó 3 mostrar "dia de pico y placa martes"
# Si es Motocicleta y la placa termina en 4 ó 5 mostrar "dia de pico y placa miércoles"
# Si es Motocicleta y la placa termina en 6 ó 7 mostrar "dia de pico y placa jueves"
# Si es Motocicleta y la placa termina en 8 ó 9 mostrar "dia de pico y placa viernes"
# Si es Carro y la placa termina en 8 ó 9 ó 0 mostrar "dia de pico y placa lunes"
# Si es Carro y la placa termina en 1 ó 2 ó 3 mostrar "dia de pico y placa martes"
# Si es Carro y la placa termina en 4 ó 5 ó 6 mostrar "dia de pico y placa miércoles"
# Si es Carro y la placa termina en 7 ó 8 ó 9 mostrar "dia de pico y placa jueves"
# Si es Carro y la placa termina en número par mostrar "dia de pico y placa viernes"
# Si es Carro y la placa termina en número impar mostrar "dia de pico y placa sábado"

tipVehiculo = input('Ingrese el tipo de vehiculo (moto o carro): ')
placa = input('Ingrese el numero de placa (moto o carro): ')

ultDigito = int(placa[-1])

if tipVehiculo == 'moto':
    if ultDigito == 0 or ultDigito == 1:
        print('El vehiculo de placas:',placa,'tiene pico y placa los días lunes')
    elif ultDigito == 2 or ultDigito == 3:
        print('El vehiculo de placas:',placa,'tiene pico y placa los días martes')
    elif ultDigito == 4 or ultDigito == 5:
        print('El vehiculo de placas:',placa,'tiene pico y placa los días miercoles')
    elif ultDigito == 6 or ultDigito == 7:
        print('El vehiculo de placas:',placa,'tiene pico y placa los días jueves')
    elif ultDigito == 8 or ultDigito == 9:
        print('El vehiculo de placas:',placa,'tiene pico y placa los días viernes')
    else:
        print('Ingrese correctamente el numero de placa')
elif tipVehiculo == 'carro':
    if ultDigito == 8 or ultDigito == 9 or ultDigito == 0:
        print('El vehiculo de placas:',placa,'tiene pico y placa los días lunes')
    elif ultDigito == 1 or ultDigito == 2 or ultDigito == 3:
        print('El vehiculo de placas:',placa,'tiene pico y placa los días martes')
    elif ultDigito == 4 or ultDigito == 5 or ultDigito == 6:
        print('El vehiculo de placas:',placa,'tiene pico y placa los días miercoles')
    elif ultDigito == 7 or ultDigito == 8 or ultDigito == 9:
        print('El vehiculo de placas:',placa,'tiene pico y placa los días jueves')
else:
    print('Ingrese un tipo de vehiculo valido')

if tipVehiculo == 'carro':
    if ultDigito % 2 == 0:
        print('Su placa finaliza en numero par por lo tanto tambien le corresponde pico y placa los viernes')
    elif ultDigito % 2 != 0:
        print('Su placa finaliza en numero impar por lo tanto tambien le corresponde pico y placa los sabados')